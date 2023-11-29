"""Test functions for run as userid."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.common.test_common_constants as TestCommonConstants
from pyracf import ResourceAdmin, UserAdmin, UserIdError
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestRunAsUserId(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_set_run_as_userid_on_object_creation(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(debug=True, run_as_userid="ESWIFT")
        call_racf_mock.side_effect = [
            TestCommonConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestCommonConstants.TEST_ALTER_USER_RESULT_SUCCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.alter(
                "squidwrd",
                traits=TestCommonConstants.TEST_ALTER_USER_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestCommonConstants.TEST_ALTER_USER_SUCCESS_AS_ESWIFT_LOG
        )

    def test_set_run_as_userid_on_object_creation_raises_improper_userid_error(self):
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
            TestCommonConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestCommonConstants.TEST_ALTER_USER_RESULT_SUCCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.alter(
                "squidwrd",
                traits=TestCommonConstants.TEST_ALTER_USER_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log, TestCommonConstants.TEST_ALTER_USER_SUCCESS_AS_ESWIFT_LOG
        )

    def test_set_running_userid_after_object_creation_raises_improper_userid_error(
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
        user_admin.clear_running_userid()
        call_racf_mock.side_effect = [
            TestCommonConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestCommonConstants.TEST_ALTER_USER_RESULT_SUCCESS_XML,
        ]
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            user_admin.alter(
                "squidwrd",
                traits=TestCommonConstants.TEST_ALTER_USER_REQUEST_TRAITS,
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(success_log, TestCommonConstants.TEST_ALTER_USER_SUCCESS_LOG)

    def test_get_running_userid(self):
        user_admin = UserAdmin(run_as_userid="ESWIFT")
        running_user = user_admin.get_running_userid()
        self.assertEqual(running_user, TestCommonConstants.TEST_RUNNING_USERID)

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_get_user_access(
        self,
        call_racf_mock: Mock,
    ):
        precheck_profile_as_squidwrd = (
            TestCommonConstants.TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_SUCCESS_XML
        )
        precheck_profile_as_squidwrd = precheck_profile_as_squidwrd.replace(
            "<message> 00    ESWIFT          READ              ALTER    NO</message>",
            "<message> 00    ESWIFT          READ               READ    NO</message>",
        )
        resource_admin = ResourceAdmin(debug=True, run_as_userid="ESWIFT")
        call_racf_mock.return_value = precheck_profile_as_squidwrd
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            access = resource_admin.get_user_access(
                "IRR.IRRSMO00.PRECHECK", "XFACILIT", "squidwrd"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestCommonConstants.TEST_EXTRACT_RESOURCE_PRECHECK_AS_SQUIDWRD_LOG,
        )
        self.assertEqual(access, "read")

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_get_user_access_raises_improper_userid_error(
        self,
        call_racf_mock: Mock,
    ):
        userid = "squidwrdtest"
        precheck_profile_as_squidwrd = (
            TestCommonConstants.TEST_EXTRACT_RESOURCE_RESULT_PRECHECK_SUCCESS_XML
        )
        precheck_profile_as_squidwrd = precheck_profile_as_squidwrd.replace(
            "<message> 00    ESWIFT          READ              ALTER    NO</message>",
            "<message> 00    ESWIFT          READ               READ    NO</message>",
        )
        resource_admin = ResourceAdmin(debug=True, run_as_userid="ESWIFT")
        call_racf_mock.return_value = precheck_profile_as_squidwrd
        with self.assertRaises(UserIdError) as exception:
            resource_admin.get_user_access("IRR.IRRSMO00.PRECHECK", "XFACILIT", userid)
        self.assertEqual(
            exception.exception.message,
            f"Unable to run as userid '{userid}'. Userid must "
            + "be a string value between 1 to 8 characters in length.",
        )
