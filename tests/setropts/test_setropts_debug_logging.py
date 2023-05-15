"""Test password sanitization in setropts debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.setropts.test_setropts_constants as TestSetroptsConstants
from pyracf import SetroptsAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestSetroptsDebugLogging(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    def boilerplate(self, irrsmo00_init_mock: Mock) -> SetroptsAdmin:
        irrsmo00_init_mock.return_value = None
        self.stdout = io.StringIO()
        return SetroptsAdmin(debug=True)

    # ============================================================================
    # Setropts Command
    # ============================================================================
    def test_command_setropts_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_SUCCESS_XML
        with contextlib.redirect_stdout(self.stdout):
            setropts_admin.command({"raclist": "ELIJTEST"})
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(success_log, TestSetroptsConstants.TEST_COMMAND_SETROPTS_SUCCESS_LOG)

    def test_command_setropts_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_ERROR_XML
        with contextlib.redirect_stdout(self.stdout):
            try:
                setropts_admin.command({"raclist": "ELIXTEST"})
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(error_log, TestSetroptsConstants.TEST_COMMAND_SETROPTS_ERROR_LOG)

    # ============================================================================
    # List Racf Options
    # ============================================================================
    def test_list_setropts_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            setropts_admin.list_ropts()
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestSetroptsConstants.TEST_LIST_SETROPTS_SUCCESS_LOG
        )
