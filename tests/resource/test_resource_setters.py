"""Test general resource profile setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin

# Resolves F401
__init__


class TestResourceSetters(unittest.TestCase):
    maxDiff = None
    resource_admin = ResourceAdmin(generate_requests_only=True)

    # ============================================================================
    # Universal Access
    # ============================================================================
    def test_resource_admin_build_set_universal_access_request(self):
        result = self.resource_admin.set_universal_access(
            "TESTING", "ELIJTEST", "ALTER"
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_RESOURCE_SET_UNIVERSAL_ACCESS_XML
        )

    # ============================================================================
    # Auditing Rules
    # ============================================================================
    def test_resource_admin_build_remove_all_audit_rules_request(self):
        result = self.resource_admin.remove_all_audit_rules("TESTING", "ELIJTEST")
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_REMOVE_ALL_AUDIT_RULES_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_access_level_request(self):
        result = self.resource_admin.overwrite_audit_rules_by_access_level(
            "TESTING", "ELIJTEST", alter="success"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_RULES_BY_ACCESS_LEVEL_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_access_level_none_request(
        self,
    ):
        result = self.resource_admin.overwrite_audit_rules_by_access_level(
            "TESTING", "ELIJTEST"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_NONE_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_access_level_multiple_request(
        self,
    ):
        result = self.resource_admin.overwrite_audit_rules_by_access_level(
            "TESTING", "ELIJTEST", alter="success", control="all"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_MULT_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_access_level_all_request(
        self,
    ):
        result = self.resource_admin.overwrite_audit_rules_by_access_level(
            "TESTING",
            "ELIJTEST",
            alter="success",
            control="all",
            update="success",
            read="failure",
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_ALL_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_attempt_request(self):
        result = self.resource_admin.overwrite_audit_rules_by_attempt(
            "TESTING", "ELIJTEST", failure="control"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_attempt_none_request(self):
        result = self.resource_admin.overwrite_audit_rules_by_attempt(
            "TESTING", "ELIJTEST"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_NONE_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_attempt_multiple_request(
        self,
    ):
        result = self.resource_admin.overwrite_audit_rules_by_attempt(
            "TESTING", "ELIJTEST", success="alter", all="read"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_MULT_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_attempt_all_request(self):
        result = self.resource_admin.overwrite_audit_rules_by_attempt(
            "TESTING", "ELIJTEST", success="alter", all="read", failure="update"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_RULES_BY_ATTEMPT_ALL_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_attempt_value_error(self):
        bad_success = "problem"
        with self.assertRaises(ValueError) as exception:
            self.resource_admin.overwrite_audit_rules_by_attempt(
                "TESTING", "ELIJTEST", success=bad_success
            )
        error_string = (
            f"'{bad_success}' is not a valid access level. Valid access levels include "
            + "'alter', 'control', 'read', and 'update'."
        )
        self.assertEqual(
            str(exception.exception),
            error_string,
        )

    def test_resource_admin_build_overwrite_audit_rules_by_attempt_value_duplicates(
        self,
    ):
        success = "alter"
        failure = "alter"
        with self.assertRaises(ValueError) as exception:
            self.resource_admin.overwrite_audit_rules_by_attempt(
                "TESTING", "ELIJTEST", success=success, failure=failure
            )
        error_string = (
            f"'{success}' is provided as an 'Access Level' multiple times, which is not "
            + "allowed."
        )
        self.assertEqual(
            str(exception.exception),
            error_string,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.get_audit_rules")
    def test_resource_admin_build_alter_audit_rules_by_access_level_request(
        self,
        resource_admin_get_audit_rules_mock: Mock,
    ):
        resource_admin_get_audit_rules_mock.return_value = (
            TestResourceConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_rules_by_access_level(
                "TESTING", "ELIJTEST", alter="success"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.get_audit_rules")
    def test_resource_admin_build_alter_audit_rules_by_access_level_none_request(
        self,
        resource_admin_get_audit_rules_mock: Mock,
    ):
        resource_admin_get_audit_rules_mock.return_value = (
            TestResourceConstants.TEST_GET_AUDIT_RULES_WITH_ALL
        )
        self.assertEqual(
            self.resource_admin.alter_audit_rules_by_access_level(
                "TESTING", "ELIJTEST"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_NONE_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.get_audit_rules")
    def test_resource_admin_build_alter_audit_rules_by_access_level_multiple_request(
        self,
        resource_admin_get_audit_rules_mock: Mock,
    ):
        resource_admin_get_audit_rules_mock.return_value = (
            TestResourceConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_rules_by_access_level(
                "TESTING", "ELIJTEST", alter="success", control="failure"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_MULT_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.get_audit_rules")
    def test_resource_admin_build_alter_audit_rules_by_access_level_all_request(
        self,
        resource_admin_get_audit_rules_mock: Mock,
    ):
        resource_admin_get_audit_rules_mock.return_value = (
            TestResourceConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_rules_by_access_level(
                "TESTING",
                "ELIJTEST",
                alter="success",
                control="failure",
                update="all",
                read="all",
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_RULES_BY_ACCESS_LEVEL_ALL_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.get_audit_rules")
    def test_resource_admin_build_alter_audit_rules_by_attempt_request(
        self,
        resource_admin_get_audit_rules_mock: Mock,
    ):
        resource_admin_get_audit_rules_mock.return_value = (
            TestResourceConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_rules_by_attempt(
                "TESTING", "ELIJTEST", failure="control"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_RULES_BY_ATTEMPT_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.get_audit_rules")
    def test_resource_admin_build_alter_audit_rules_by_attempt_none_request(
        self,
        resource_admin_get_audit_rules_mock: Mock,
    ):
        resource_admin_get_audit_rules_mock.return_value = (
            TestResourceConstants.TEST_GET_AUDIT_RULES_WITH_ALL
        )
        self.assertEqual(
            self.resource_admin.alter_audit_rules_by_attempt("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_RULES_BY_ATTEMPT_NONE_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.get_audit_rules")
    def test_resource_admin_build_alter_audit_rules_by_attempt_multiple_request(
        self,
        resource_admin_get_audit_rules_mock: Mock,
    ):
        resource_admin_get_audit_rules_mock.return_value = (
            TestResourceConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_rules_by_attempt(
                "TESTING", "ELIJTEST", failure="control", all="read"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_RULES_BY_ATTEMPT_MULT_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.get_audit_rules")
    def test_resource_admin_build_alter_audit_rules_by_attempt_all_request(
        self,
        resource_admin_get_audit_rules_mock: Mock,
    ):
        resource_admin_get_audit_rules_mock.return_value = (
            TestResourceConstants.TEST_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_rules_by_attempt(
                "TESTING", "ELIJTEST", failure="control", success="alter", all="read"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_RULES_BY_ATTEMPT_ALL_REQUEST_XML,
        )

    def test_resource_admin_build_alter_audit_rules_by_attempt_value_error(self):
        bad_success = "problem"
        bad_all = "value"
        with self.assertRaises(ValueError) as exception:
            self.resource_admin.overwrite_audit_rules_by_attempt(
                "TESTING",
                "ELIJTEST",
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

    def test_resource_admin_build_alter_audit_rules_by_attempt_value_error_all(self):
        bad_success = "problem"
        bad_failure = ["improper"]
        bad_all = 1234
        with self.assertRaises(ValueError) as exception:
            self.resource_admin.overwrite_audit_rules_by_attempt(
                "TESTING",
                "ELIJTEST",
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
