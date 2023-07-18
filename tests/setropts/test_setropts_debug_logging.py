"""Test password sanitization in setropts debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.setropts.test_setropts_constants as TestSetroptsConstants
from pyracf import SecurityRequestError, SetroptsAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestSetroptsDebugLogging(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    setropts_admin = SetroptsAdmin(debug=True)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    # ============================================================================
    # Setropts Alter
    # ============================================================================
    def test_alter_setropts_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.setropts_admin.alter(options={"base:raclist": "ELIJTEST"})
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestSetroptsConstants.TEST_ALTER_SETROPTS_SUCCESS_LOG
        )

    def test_alter_setropts_request_debug_log_works_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.setropts_admin.alter(options={"base:raclist": "ELIXTEST"})
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(error_log, TestSetroptsConstants.TEST_ALTER_SETROPTS_ERROR_LOG)

    # ============================================================================
    # List Racf Options
    # ============================================================================
    def test_list_racf_options_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.setropts_admin.list_racf_options()
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestSetroptsConstants.TEST_LIST_SETROPTS_SUCCESS_LOG
        )

    def test_list_racf_options_request_debug_log_works_on_success_2(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_2_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.setropts_admin.list_racf_options()
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestSetroptsConstants.TEST_LIST_SETROPTS_SUCCESS_2_LOG
        )

    def test_list_racf_options_request_debug_log_works_on_success_3(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_3_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.setropts_admin.list_racf_options()
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestSetroptsConstants.TEST_LIST_SETROPTS_SUCCESS_3_LOG
        )
