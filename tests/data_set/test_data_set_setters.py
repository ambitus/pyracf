"""Test data set setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.data_set.test_data_set_constants as TestDataSetConstants
from pyracf import DataSetAdmin

# Resolves F401
__init__


class TestDataSetSetters(unittest.TestCase):
    maxDiff = None
    data_set_admin = DataSetAdmin(generate_requests_only=True)

    def test_data_set_admin_build_set_uacc_request(self):
        result = self.data_set_admin.set_universal_access(
            "ESWIFT.TEST.T1136242.P3020470", "ALTER"
        )
        self.assertEqual(
            result, TestDataSetConstants.TEST_DATA_SET_SET_UNIVERSAL_ACCESS_XML
        )

    # ============================================================================
    # Auditing Rules
    # ============================================================================
    def test_data_set_admin_build_remove_all_audit_rules_request(self):
        result = self.data_set_admin.remove_all_audit_rules(
            "ESWIFT.TEST.T1136242.P3020470"
        )
        self.assertEqual(
            result,
            TestDataSetConstants.TEST_DATA_SET_REMOVE_ALL_AUDIT_RULES_REQUEST_XML,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_access_level_request(self):
        result = self.data_set_admin.overwrite_audit_rules_by_access_level(
            "ESWIFT.TEST.T1136242.P3020470", alter="success"
        )
        self.assertEqual(
            result,
            TestDataSetConstants.TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ACCESS_LEVEL_REQUEST_XML,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_access_level_none_request(
        self,
    ):
        result = self.data_set_admin.overwrite_audit_rules_by_access_level(
            "ESWIFT.TEST.T1136242.P3020470"
        )
        self.assertEqual(
            result,
            TestDataSetConstants.TEST_DATA_SET_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_NONE_REQUEST_XML,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_access_level_multiple_request(
        self,
    ):
        result = self.data_set_admin.overwrite_audit_rules_by_access_level(
            "ESWIFT.TEST.T1136242.P3020470", alter="success", control="all"
        )
        self.assertEqual(
            result,
            TestDataSetConstants.TEST_DATA_SET_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_MULT_REQUEST_XML,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_access_level_all_request(
        self,
    ):
        result = self.data_set_admin.overwrite_audit_rules_by_access_level(
            "ESWIFT.TEST.T1136242.P3020470",
            alter="success",
            control="all",
            update="success",
            read="failure",
        )
        self.assertEqual(
            result,
            TestDataSetConstants.TEST_DATA_SET_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_ALL_REQUEST_XML,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_attempt_request(self):
        result = self.data_set_admin.overwrite_audit_rules_by_attempt(
            "ESWIFT.TEST.T1136242.P3020470", failure="control"
        )
        self.assertEqual(
            result,
            TestDataSetConstants.TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_REQUEST_XML,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_attempt_none_request(self):
        result = self.data_set_admin.overwrite_audit_rules_by_attempt(
            "ESWIFT.TEST.T1136242.P3020470"
        )
        self.assertEqual(
            result,
            TestDataSetConstants.TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_NONE_REQUEST_XML,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_attempt_multiple_request(
        self,
    ):
        result = self.data_set_admin.overwrite_audit_rules_by_attempt(
            "ESWIFT.TEST.T1136242.P3020470", success="alter", all="read"
        )
        self.assertEqual(
            result,
            TestDataSetConstants.TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_MULT_REQUEST_XML,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_attempt_all_request(self):
        result = self.data_set_admin.overwrite_audit_rules_by_attempt(
            "ESWIFT.TEST.T1136242.P3020470",
            success="alter",
            all="read",
            failure="update",
        )
        self.assertEqual(
            result,
            TestDataSetConstants.TEST_DATA_SET_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_ALL_REQUEST_XML,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_attempt_value_error(self):
        bad_success = "problem"
        with self.assertRaises(ValueError) as exception:
            self.data_set_admin.overwrite_audit_rules_by_attempt(
                "ESWIFT.TEST.T1136242.P3020470", success=bad_success
            )
        error_string = (
            f"'{bad_success}' is not a valid access level. Valid access levels include "
            + "'alter', 'control', 'read', and 'update'."
        )
        self.assertEqual(
            str(exception.exception),
            error_string,
        )

    def test_data_set_admin_build_overwrite_audit_rules_by_attempt_value_duplicates(
        self,
    ):
        success = "alter"
        failure = "alter"
        with self.assertRaises(ValueError) as exception:
            self.data_set_admin.overwrite_audit_rules_by_attempt(
                "ESWIFT.TEST.T1136242.P3020470", success=success, failure=failure
            )
        error_string = (
            f"'{success}' is provided as an 'Access Level' multiple times, which is not "
            + "allowed."
        )
        self.assertEqual(
            str(exception.exception),
            error_string,
        )

    @patch("pyracf.data_set.data_set_admin.DataSetAdmin.get_audit_rules")
    def test_data_set_admin_build_alter_audit_rules_by_access_level_request(
        self,
        data_set_admin_get_audit_rules_mock: Mock,
    ):
        data_set_admin_get_audit_rules_mock.return_value = (
            TestDataSetConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.data_set_admin.alter_audit_rules_by_access_level(
                "ESWIFT.TEST.T1136242.P3020470", alter="success"
            ),
            TestDataSetConstants.TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_REQUEST_XML,
        )

    @patch("pyracf.data_set.data_set_admin.DataSetAdmin.get_audit_rules")
    def test_data_set_admin_build_alter_audit_rules_by_access_level_none_request(
        self,
        data_set_admin_get_audit_rules_mock: Mock,
    ):
        data_set_admin_get_audit_rules_mock.return_value = (
            TestDataSetConstants.TEST_GET_AUDIT_RULES_WITH_ALL
        )
        self.assertEqual(
            self.data_set_admin.alter_audit_rules_by_access_level(
                "ESWIFT.TEST.T1136242.P3020470"
            ),
            TestDataSetConstants.TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_NONE_REQUEST_XML,
        )

    @patch("pyracf.data_set.data_set_admin.DataSetAdmin.get_audit_rules")
    def test_data_set_admin_build_alter_audit_rules_by_access_level_multiple_request(
        self,
        data_set_admin_get_audit_rules_mock: Mock,
    ):
        data_set_admin_get_audit_rules_mock.return_value = (
            TestDataSetConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.data_set_admin.alter_audit_rules_by_access_level(
                "ESWIFT.TEST.T1136242.P3020470", alter="success", control="failure"
            ),
            TestDataSetConstants.TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_MULT_REQUEST_XML,
        )

    @patch("pyracf.data_set.data_set_admin.DataSetAdmin.get_audit_rules")
    def test_data_set_admin_build_alter_audit_rules_by_access_level_all_request(
        self,
        data_set_admin_get_audit_rules_mock: Mock,
    ):
        data_set_admin_get_audit_rules_mock.return_value = (
            TestDataSetConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.data_set_admin.alter_audit_rules_by_access_level(
                "ESWIFT.TEST.T1136242.P3020470",
                alter="success",
                control="failure",
                update="all",
                read="all",
            ),
            TestDataSetConstants.TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_ALL_REQUEST_XML,
        )

    @patch("pyracf.data_set.data_set_admin.DataSetAdmin.get_audit_rules")
    def test_data_set_admin_build_alter_audit_rules_by_attempt_request(
        self,
        data_set_admin_get_audit_rules_mock: Mock,
    ):
        data_set_admin_get_audit_rules_mock.return_value = (
            TestDataSetConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.data_set_admin.alter_audit_rules_by_attempt(
                "ESWIFT.TEST.T1136242.P3020470", failure="control"
            ),
            TestDataSetConstants.TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ATTEMPT_REQUEST_XML,
        )

    @patch("pyracf.data_set.data_set_admin.DataSetAdmin.get_audit_rules")
    def test_data_set_admin_build_alter_audit_rules_by_attempt_none_request(
        self,
        data_set_admin_get_audit_rules_mock: Mock,
    ):
        data_set_admin_get_audit_rules_mock.return_value = (
            TestDataSetConstants.TEST_GET_AUDIT_RULES_WITH_ALL
        )
        self.assertEqual(
            self.data_set_admin.alter_audit_rules_by_attempt(
                "ESWIFT.TEST.T1136242.P3020470"
            ),
            TestDataSetConstants.TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ATTEMPT_NONE_REQUEST_XML,
        )

    @patch("pyracf.data_set.data_set_admin.DataSetAdmin.get_audit_rules")
    def test_data_set_admin_build_alter_audit_rules_by_attempt_multiple_request(
        self,
        data_set_admin_get_audit_rules_mock: Mock,
    ):
        data_set_admin_get_audit_rules_mock.return_value = (
            TestDataSetConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.data_set_admin.alter_audit_rules_by_attempt(
                "ESWIFT.TEST.T1136242.P3020470", failure="control", all="read"
            ),
            TestDataSetConstants.TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ATTEMPT_MULT_REQUEST_XML,
        )

    @patch("pyracf.data_set.data_set_admin.DataSetAdmin.get_audit_rules")
    def test_data_set_admin_build_alter_audit_rules_by_attempt_all_request(
        self,
        data_set_admin_get_audit_rules_mock: Mock,
    ):
        data_set_admin_get_audit_rules_mock.return_value = (
            TestDataSetConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.data_set_admin.alter_audit_rules_by_attempt(
                "ESWIFT.TEST.T1136242.P3020470",
                failure="control",
                success="alter",
                all="read",
            ),
            TestDataSetConstants.TEST_DATA_SET_ALTER_AUDIT_RULES_BY_ATTEMPT_ALL_REQUEST_XML,
        )

    def test_data_set_admin_build_alter_audit_rules_by_attempt_value_error(self):
        bad_success = "problem"
        bad_all = "value"
        with self.assertRaises(ValueError) as exception:
            self.data_set_admin.overwrite_audit_rules_by_attempt(
                "ESWIFT.TEST.T1136242.P3020470",
                success=bad_success,
                all=bad_all,
            )
        error_string = (
            f"'{bad_success}' and '{bad_all}' are not valid access levels. Valid "
            + "access levels include 'alter', 'control', 'read', and 'update'."
        )
        self.assertEqual(
            str(exception.exception),
            error_string,
        )

    def test_data_set_admin_build_alter_audit_rules_by_attempt_value_error_all(self):
        bad_success = "problem"
        bad_failure = ["improper"]
        bad_all = 1234
        with self.assertRaises(ValueError) as exception:
            self.data_set_admin.overwrite_audit_rules_by_attempt(
                "ESWIFT.TEST.T1136242.P3020470",
                success=bad_success,
                failure=bad_failure,
                all=bad_all,
            )
        error_string = (
            f"'{bad_success}', '{bad_failure}', and '{bad_all}' are not valid access levels. "
            + "Valid access levels include 'alter', 'control', 'read', and 'update'."
        )
        self.assertEqual(
            str(exception.exception),
            error_string,
        )
