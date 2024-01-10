"""Test general resource profile setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestResourceSetters(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
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

    def test_resource_admin_build_overwrite_audit_by_access_level_request(self):
        result = self.resource_admin.overwrite_audit_by_access_level(
            "TESTING", "ELIJTEST", alter="success"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_access_level_none_request(self):
        result = self.resource_admin.overwrite_audit_by_access_level(
            "TESTING", "ELIJTEST"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_NONE_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_access_level_multiple_request(
        self,
    ):
        result = self.resource_admin.overwrite_audit_by_access_level(
            "TESTING", "ELIJTEST", alter="success", control="all"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ACCESS_LEVEL_MULT_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_access_level_all_request(self):
        result = self.resource_admin.overwrite_audit_by_access_level(
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

    def test_resource_admin_build_overwrite_audit_by_attempt_request(self):
        result = self.resource_admin.overwrite_audit_by_attempt(
            "TESTING", "ELIJTEST", failure="control"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ATTEMPT_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_attempt_none_request(self):
        result = self.resource_admin.overwrite_audit_by_attempt("TESTING", "ELIJTEST")
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ATTEMPT_NONE_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_attempt_multiple_request(self):
        result = self.resource_admin.overwrite_audit_by_attempt(
            "TESTING", "ELIJTEST", success="alter", all="read"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ATTEMPT_MULT_REQUEST_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_attempt_all_request(self):
        result = self.resource_admin.overwrite_audit_by_attempt(
            "TESTING", "ELIJTEST", success="alter", all="read", failure="update"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_ATTEMPT_ALL_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.extract")
    def test_resource_admin_build_alter_audit_by_access_level_request(
        self,
        resource_admin_extract_mock: Mock,
    ):
        resource_admin_extract_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_by_access_level(
                "TESTING", "ELIJTEST", alter="success"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_ACCESS_LEVEL_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.extract")
    def test_resource_admin_build_alter_audit_by_access_level_none_request(
        self,
        resource_admin_extract_mock: Mock,
    ):
        resource_admin_extract_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_by_access_level("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_ACCESS_LEVEL_NONE_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.extract")
    def test_resource_admin_build_alter_audit_by_access_level_multiple_request(
        self,
        resource_admin_extract_mock: Mock,
    ):
        resource_admin_extract_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_by_access_level(
                "TESTING", "ELIJTEST", alter="success", control="failure"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_ACCESS_LEVEL_MULT_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.extract")
    def test_resource_admin_build_alter_audit_by_access_level_all_request(
        self,
        resource_admin_extract_mock: Mock,
    ):
        resource_admin_extract_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_by_access_level(
                "TESTING",
                "ELIJTEST",
                alter="success",
                control="failure",
                update="all",
                read="all",
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_ACCESS_LEVEL_ALL_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.extract")
    def test_resource_admin_build_alter_audit_by_attempt_request(
        self,
        resource_admin_extract_mock: Mock,
    ):
        resource_admin_extract_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_by_attempt(
                "TESTING", "ELIJTEST", failure="control"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_ATTEMPT_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.extract")
    def test_resource_admin_build_alter_audit_by_attempt_none_request(
        self,
        resource_admin_extract_mock: Mock,
    ):
        resource_admin_extract_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_by_attempt("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_ATTEMPT_NONE_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.extract")
    def test_resource_admin_build_alter_audit_by_attempt_multiple_request(
        self,
        resource_admin_extract_mock: Mock,
    ):
        resource_admin_extract_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_by_attempt(
                "TESTING", "ELIJTEST", failure="control", all="read"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_ATTEMPT_MULT_REQUEST_XML,
        )

    @patch("pyracf.resource.resource_admin.ResourceAdmin.extract")
    def test_resource_admin_build_alter_audit_by_attempt_all_request(
        self,
        resource_admin_extract_mock: Mock,
    ):
        resource_admin_extract_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_GET_AUDIT_RULES
        )
        self.assertEqual(
            self.resource_admin.alter_audit_by_attempt(
                "TESTING", "ELIJTEST", failure="control", success="alter", all="read"
            ),
            TestResourceConstants.TEST_RESOURCE_ALTER_AUDIT_BY_ATTEMPT_ALL_REQUEST_XML,
        )
