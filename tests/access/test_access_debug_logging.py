"""Test password sanitization in access debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.access.test_access_constants as TestAccessConstants
from pyracf import AccessAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestAccessDebugLogging(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def boilerplate(self, irrsmo00_init_mock: Mock) -> AccessAdmin:
        irrsmo00_init_mock.return_value = None
        self.stdout = io.StringIO()
        return AccessAdmin(debug=True)

    # ============================================================================
    # Add Access
    # ============================================================================
    def test_add_access_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        access_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_ADD_ACCESS_RESULT_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            access_admin.add(TestAccessConstants.TEST_ADD_ACCESS_REQUEST_TRAITS)
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(success_log, TestAccessConstants.TEST_ADD_ACCESS_SUCCESS_LOG)

    def test_add_access_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        access_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_ADD_ACCESS_RESULT_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                access_admin.add(
                    TestAccessConstants.TEST_ADD_ACCESS_REQUEST_TRAITS
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(error_log, TestAccessConstants.TEST_ADD_ACCESS_ERROR_LOG)
