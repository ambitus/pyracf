"""Test password sanitization in user debug logging."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import SecurityRequestError, UserAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestUserDebugLogging(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    user_admin = UserAdmin(debug=True)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    test_password = "GIyTTqdF"
    test_passphrase = "PassPhrasesAreCool!"
    simple_password = "PASSWORD"

    # ============================================================================
    # Add User
    # ============================================================================
    def test_add_user_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_SUCCESS_XML
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.user_admin.add(
                "squidwrd",
                traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(success_log, TestUserConstants.TEST_ADD_USER_SUCCESS_LOG)

    def test_add_user_request_debug_log_works_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_ERROR_XML
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.user_admin.add(
                    "squidwrd",
                    traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(error_log, TestUserConstants.TEST_ADD_USER_ERROR_LOG)

    # ============================================================================
    # Secrets Redaction
    # ============================================================================
    def test_add_user_request_debug_log_passwords_get_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_ADD_USER_PASSWORD_RESULT_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.user_admin.add(
                "squidwrd",
                traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSWORD,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestUserConstants.TEST_ADD_USER_PASSWORD_SUCCESS_LOG
        )
        self.assertNotIn(self.test_password, success_log)

    def test_add_user_request_debug_log_passwords_get_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_ADD_USER_PASSWORD_RESULT_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.user_admin.add(
                    "squidwrd",
                    traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSWORD,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(error_log, TestUserConstants.TEST_ADD_USER_PASSWORD_ERROR_LOG)
        self.assertNotIn(self.test_password, error_log)

    def test_add_user_request_debug_log_passphrases_get_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_ADD_USER_PASSPHRASE_RESULT_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.user_admin.add(
                "squidwrd",
                traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSPHRASE,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestUserConstants.TEST_ADD_USER_PASSPHRASE_SUCCESS_LOG
        )
        self.assertNotIn(self.test_passphrase, success_log)

    def test_add_user_request_debug_log_passphrases_get_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_ADD_USER_PASSPHRASE_RESULT_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.user_admin.add(
                    "squidwrd",
                    traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSPHRASE,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log, TestUserConstants.TEST_ADD_USER_PASSPHRASE_ERROR_LOG
        )
        self.assertNotIn(self.test_passphrase, error_log)

    def test_add_user_request_debug_log_passphrases_and_passwords_get_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_ADD_USER_PASSPHRASE_AND_PASSWORD_RESULT_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.user_admin.add(
                "squidwrd",
                traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSPHRASE_AND_PASSWORD,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestUserConstants.TEST_ADD_USER_PASSPHRASE_AND_PASSWORD_SUCCESS_LOG,
        )
        self.assertNotIn(self.test_passphrase, success_log)
        self.assertNotIn(self.test_password, success_log)

    def test_add_user_request_debug_log_passphrases_and_passwords_get_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_ADD_USER_PASSPHRASE_AND_PASSWORD_RESULT_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.user_admin.add(
                    "squidwrd",
                    traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSPHRASE_AND_PASSWORD,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log, TestUserConstants.TEST_ADD_USER_PASSPHRASE_AND_PASSWORD_ERROR_LOG
        )
        self.assertNotIn(self.test_passphrase, error_log)
        self.assertNotIn(self.test_password, error_log)

    def test_add_user_request_debug_log_password_xml_tags_not_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_ADD_USER_PASSWORD_RESULT_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.user_admin.add(
                "squidwrd",
                traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSWORD_SIMPLE,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestUserConstants.TEST_ADD_USER_PASSWORD_SUCCESS_LOG
        )
        self.assertEqual(success_log.count("********"), 4)
        self.assertIn(self.simple_password, success_log)

    def test_add_user_request_debug_log_password_xml_tags_not_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_ADD_USER_PASSWORD_RESULT_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.user_admin.add(
                    "squidwrd",
                    traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSWORD_SIMPLE,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(error_log, TestUserConstants.TEST_ADD_USER_PASSWORD_ERROR_LOG)
        self.assertEqual(error_log.count("********"), 4)
        self.assertIn(self.simple_password, error_log)

    # ============================================================================
    # Add Additional Secrets
    # ============================================================================
    def test_add_user_request_debug_log_additional_secret_added_get_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, additional_secret_traits=["omvs:uid"])
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_SUCCESS_XML
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.add(
                "squidwrd",
                traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestUserConstants.TEST_ADD_USER_ADDITIONAL_SECRET_ADDED_SUCCESS_LOG,
        )
        self.assertNotIn(
            TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS["omvs:uid"], success_log
        )

    def test_add_user_request_debug_log_additional_secret_added_get_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, additional_secret_traits=["omvs:uid"])
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_ERROR_XML
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                user_admin.add(
                    "squidwrd",
                    traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log, TestUserConstants.TEST_ADD_USER_ADDITIONAL_SECRET_ADDED_ERROR_LOG
        )
        self.assertNotIn(
            TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS["omvs:uid"], error_log
        )

    # ============================================================================
    # Extract User
    # ============================================================================
    def test_extract_user_base_omvs_request_debug_log_works_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.user_admin.extract("squidwrd", segments=["omvs"])
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestUserConstants.TEST_EXTRACT_USER_BASE_OMVS_SUCCESS_LOG
        )

    def test_extract_user_base_omvs_request_debug_log_works_on_error(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.user_admin.extract("squidwrd", segments=["omvs"])
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log, TestUserConstants.TEST_EXTRACT_USER_BASE_OMVS_ERROR_LOG
        )
