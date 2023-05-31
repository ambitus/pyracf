"""Test password sanitization in connection debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestConnectionDebugLogging(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ConnectionAdmin:
        irrsmo00_init_mock.return_value = None
        self.stdout = io.StringIO()
        return ConnectionAdmin(debug=True)

    # ============================================================================
    # Add Connection
    # ============================================================================
    def test_add_connection_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_ADD_CONNECTION_RESULT_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            connection_admin.add(
                TestConnectionConstants.TEST_ADD_CONNECTION_REQUEST_TRAITS
            )
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestConnectionConstants.TEST_ADD_CONNECTION_SUCCESS_LOG
        )

    def test_add_connection_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_ADD_CONNECTION_RESULT_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                connection_admin.add(
                    TestConnectionConstants.TEST_ADD_CONNECTION_REQUEST_TRAITS
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            error_log, TestConnectionConstants.TEST_ADD_CONNECTION_ERROR_LOG
        )
