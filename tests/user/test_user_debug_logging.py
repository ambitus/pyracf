"""Test password sanitization in user debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import UserAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestUserDebugLogging(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    test_password = "GIyTTqdF"

    def boilerplate(self, irrsmo00_init_mock: Mock) -> UserAdmin:
        irrsmo00_init_mock.return_value = None
        self.stdout = io.StringIO()
        return UserAdmin(debug=True)

    # ============================================================================
    # Add User
    # ============================================================================
    def test_add_user_request_debug_log_passwords_get_redacted_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_SUCCESS_XML
        with contextlib.redirect_stdout(self.stdout):
            user_admin.add("squidwrd", traits={"base:password": self.test_password})
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(success_log, TestUserConstants.TEST_ADD_USER_SUCCESS_LOG)
        self.assertNotIn(self.test_password, success_log)

    def test_add_user_request_debug_log_passwords_get_redacted_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_ERROR_XML
        with contextlib.redirect_stdout(self.stdout):
            try:
                user_admin.add("squidwrd", traits={"base:password": self.test_password})
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(error_log, TestUserConstants.TEST_ADD_USER_ERROR_LOG)
        self.assertNotIn(self.test_password, error_log)

    # ============================================================================
    # Extract User
    # ============================================================================
    def test_extract_user_base_omvs_request_debug_log_works_on_success(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            user_admin.extract("squidwrd", segments={"omvs": True})
        success_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            success_log, TestUserConstants.TEST_EXTRACT_USER_BASE_OMVS_SUCCESS_LOG
        )

    def test_extract_user_base_omvs_request_debug_log_works_on_error(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with contextlib.redirect_stdout(self.stdout):
            try:
                user_admin.extract("squidwrd", segments={"omvs": True})
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", self.stdout.getvalue())
        self.assertEqual(
            error_log, TestUserConstants.TEST_EXTRACT_USER_BASE_OMVS_ERROR_LOG
        )
