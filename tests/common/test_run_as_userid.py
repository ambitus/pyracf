"""Test functions for run as userid."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.common.test_common_constants as TestCommonConstants
import tests.user.test_user_constants as TestUserConstants
from pyracf import UserAdmin, UserIdError

# Resolves F401
__init__


class TestRunAsUserId(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_set_run_as_userid_on_object_creation(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, run_as_userid="ESWIFT")
        call_racf_mock.side_effect = [
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestUserConstants.TEST_ALTER_USER_RESULT_SUCCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.alter(
                "squidwrd",
                traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestCommonConstants.TEST_ALTER_USER_SUCCESS_AS_ESWIFT_LOG
        )

    def test_set_run_as_userid_on_object_creation_raises_userid_error(self):
        userid = "ESWIFTTEST"
        with self.assertRaises(UserIdError) as exception:
            UserAdmin(debug=True, run_as_userid=userid)
        self.assertEqual(
            exception.exception.message,
            f"Unable to run as userid '{userid}'. Userid must "
            + "be a string value between 1 to 8 characters in length.",
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_set_running_userid_after_object_creation(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True)
        user_admin.set_running_userid("ESWIFT")
        call_racf_mock.side_effect = [
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestUserConstants.TEST_ALTER_USER_RESULT_SUCCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.alter(
                "squidwrd",
                traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestCommonConstants.TEST_ALTER_USER_SUCCESS_AS_ESWIFT_LOG
        )

    def test_set_running_userid_after_object_creation_raises_userid_error(
        self,
    ):
        userid = "ESWIFTTEST"
        user_admin = UserAdmin(debug=True)
        with self.assertRaises(UserIdError) as exception:
            user_admin.set_running_userid(userid)
        self.assertEqual(
            exception.exception.message,
            f"Unable to run as userid '{userid}'. Userid must "
            + "be a string value between 1 to 8 characters in length.",
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_clear_running_userid(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, run_as_userid="ESWIFT")
        user_admin.set_running_userid(userid=None)
        call_racf_mock.side_effect = [
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestUserConstants.TEST_ALTER_USER_RESULT_SUCCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.alter(
                "squidwrd",
                traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(success_log, TestUserConstants.TEST_ALTER_USER_SUCCESS_LOG)

    def test_get_running_userid(self):
        user_admin = UserAdmin(run_as_userid="ESWIFT")
        running_user = user_admin.get_running_userid()
        self.assertEqual(running_user, TestCommonConstants.TEST_RUNNING_USERID)
