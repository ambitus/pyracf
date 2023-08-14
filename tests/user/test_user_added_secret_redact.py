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
class TestUserAddedSecretRedact(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    # ============================================================================
    # Add User
    # ============================================================================
    def test_add_user_request_debug_log_added_secrets_get_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        self.user_admin_local = UserAdmin(
            debug=True, additional_secret_traits={"omvs:uid": "uid"}
        )
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_SUCCESS_XML
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            self.user_admin_local.add(
                "squidwrd",
                traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestUserConstants.TEST_ADD_USER_ADDED_SECRET_SUCCESS_LOG,
        )
        self.assertNotIn(
            TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS["omvs:uid"], success_log
        )

    def test_add_user_request_debug_log_added_secrets_get_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        self.user_admin_local = UserAdmin(
            debug=True, additional_secret_traits={"omvs:uid": "uid"}
        )
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_ERROR_XML
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            try:
                self.user_admin_local.add(
                    "squidwrd",
                    traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS,
                )
            except SecurityRequestError:
                pass
        error_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            error_log, TestUserConstants.TEST_ADD_USER_ADDED_SECRET_ERROR_LOG
        )
        self.assertNotIn(
            TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS["omvs:uid"], error_log
        )
