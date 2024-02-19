"""Test data set profile getter functions."""

import contextlib
import io
import re
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.data_set.test_data_set_constants as TestDataSetConstants
from pyracf import DataSetAdmin, SecurityRequestError, UserIdError

# Resolves F401
__init__


class TestDataSetGetters(unittest.TestCase):
    maxDiff = None
    ansi_escape = re.compile(r"\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])")
    data_set_admin = DataSetAdmin()

    # ============================================================================
    # Universal Access
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_universal_access_returns_valid_when_read(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertEqual(
            self.data_set_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470"),
            "read",
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_universal_access_returns_valid_when_none(
        self,
        call_racf_mock: Mock,
    ):
        data_set_extract_no_universal_access = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        data_set_extract_no_universal_access = (
            data_set_extract_no_universal_access.replace(
                "<message> 00    ESWIFT          READ          NO      NO</message>",
                "<message> 00    ESWIFT          NONE          NO      NO</message>",
            )
        )
        call_racf_mock.return_value = data_set_extract_no_universal_access
        self.assertIsNone(
            self.data_set_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470")
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_universal_access_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.data_set_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470")

    # ============================================================================
    # Individual Access
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_my_access_returns_valid_when_alter(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertEqual(
            self.data_set_admin.get_my_access("ESWIFT.TEST.T1136242.P3020470"), "alter"
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_my_access_returns_valid_when_none(
        self,
        call_racf_mock: Mock,
    ):
        data_set_extract_no_my_access = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        data_set_extract_no_my_access = data_set_extract_no_my_access.replace(
            "<message> ALTER        SYS1           NON-VSAM</message>",
            "<message> NONE         SYS1           NON-VSAM</message>",
        )
        call_racf_mock.return_value = data_set_extract_no_my_access
        self.assertIsNone(
            self.data_set_admin.get_my_access("ESWIFT.TEST.T1136242.P3020470")
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_my_access_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.data_set_admin.get_my_access("ESWIFT.TEST.T1136242.P3020470")

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_get_user_access_data_set(
        self,
        call_racf_mock: Mock,
    ):
        precheck_profile_as_squidwrd = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        precheck_profile_as_squidwrd = precheck_profile_as_squidwrd.replace(
            "<message> ALTER        SYS1           NON-VSAM</message>",
            "<message> READ         SYS1           NON-VSAM</message>",
        )
        data_set_admin = DataSetAdmin(debug=True, run_as_userid="ESWIFT")
        call_racf_mock.return_value = precheck_profile_as_squidwrd
        stdout = io.StringIO()
        with contextlib.redirect_stdout(stdout):
            access = data_set_admin.get_user_access(
                "ESWIFT.TEST.T1136242.P3020470", "squidwrd"
            )
        success_log = self.ansi_escape.sub("", stdout.getvalue())
        self.assertEqual(
            success_log,
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_BASE_AS_SQUIDWRD_SUCCESS,
        )
        self.assertEqual(access, "read")

    def test_get_user_access_dataset_raises_userid_error(self):
        userid = "squidwrdtest"
        data_set_admin = DataSetAdmin(debug=True, run_as_userid="ESWIFT")
        with self.assertRaises(UserIdError) as exception:
            data_set_admin.get_user_access("ESWIFT.TEST.T1136242.P3020470", userid)
        self.assertEqual(
            exception.exception.message,
            f"Unable to run as userid '{userid}'. Userid must "
            + "be a string value between 1 to 8 characters in length.",
        )

    # ============================================================================
    # Auditing Rules
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_audit_rules(
        self,
        call_racf_mock: Mock,
    ):
        profile_with_success_and_failure_auditing = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        profile_with_success_and_failure_auditing = (
            profile_with_success_and_failure_auditing.replace(
                "<message>FAILURES(READ)</message>",
                "<message>SUCCESS(UPDATE),FAILURES(READ)</message>",
            )
        )

        call_racf_mock.return_value = profile_with_success_and_failure_auditing
        self.assertEqual(
            self.data_set_admin.get_audit_rules("ESWIFT.TEST.T1136242.P3020470"),
            TestDataSetConstants.TEST_GET_AUDIT_RULES,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_audit_rules_single(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertEqual(
            self.data_set_admin.get_audit_rules("ESWIFT.TEST.T1136242.P3020470"),
            TestDataSetConstants.TEST_GET_AUDIT_RULES_SINGLE,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_audit_rules_none(
        self,
        call_racf_mock: Mock,
    ):
        profile_with_none_auditing = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        profile_with_none_auditing = profile_with_none_auditing.replace(
            "<message>FAILURES(READ)</message>",
            "<message>NONE</message>",
        )
        call_racf_mock.return_value = profile_with_none_auditing
        self.assertIsNone(
            self.data_set_admin.get_audit_rules("ESWIFT.TEST.T1136242.P3020470")
        )

    # Error in environment, TESTING already deleted/not added
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_get_audit_rules_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.data_set_admin.get_audit_rules("ESWIFT.TEST.T1136242.P3020470")
