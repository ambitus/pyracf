"""Test password sanitization in access debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.access.test_access_constants as TestAccessConstants
from pyracf import AccessAdmin, SecurityRequestError
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestAccessDebugLogging(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    access_admin = AccessAdmin(debug=True)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    # ============================================================================
    # Add Access
    # ============================================================================
    def test_add_access_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_ADD_ACCESS_RESULT_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.access_admin.add(
                "TESTING", "ELIJTEST", "ESWIFT", traits={"base:access": "READ"}
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(success_log, TestAccessConstants.TEST_ADD_ACCESS_SUCCESS_LOG)

    def test_add_access_request_debug_log_works_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_ADD_ACCESS_RESULT_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.access_admin.add(
                    "TESTING", "ELIJTEST", "ESWIFT", traits={"base:access": "READ"}
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(error_log, TestAccessConstants.TEST_ADD_ACCESS_ERROR_LOG)
