"""Test general resource profile setter functions."""

import unittest
from unittest.mock import Mock

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
    def test_resource_admin_build_clear_all_audit_rules_request(self):
        result = self.resource_admin.clear_all_audit_rules("TESTING", "ELIJTEST")
        self.assertEqual(
            result, TestResourceConstants.TEST_RESOURCE_CLEAR_ALL_AUDIT_RULES_XML
        )

    def test_resource_admin_build_overwrite_audit_by_audit_alter_access_request(self):
        result = self.resource_admin.overwrite_audit_by_audit_alter_access(
            "TESTING", "ELIJTEST", "SUCCESS"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_AUDIT_ALTER_ACCESS_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_audit_control_access_request(self):
        result = self.resource_admin.overwrite_audit_by_audit_control_access(
            "TESTING", "ELIJTEST", "FAILURE"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_AUDIT_CONTROL_ACCESS_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_audit_read_access_request(self):
        result = self.resource_admin.overwrite_audit_by_audit_read_access(
            "TESTING", "ELIJTEST", "SUCCESS"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_AUDIT_READ_ACCESS_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_audit_update_access_request(self):
        result = self.resource_admin.overwrite_audit_by_audit_update_access(
            "TESTING", "ELIJTEST", "ALL"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_AUDIT_UPDATE_ACCESS_XML,
        )

    def test_resource_admin_build_overwrite_audit_by_successes_request(self):
        result = self.resource_admin.overwrite_audit_by_successes(
            "TESTING", "ELIJTEST", "alter"
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_SUCCESSES_XML
        )

    def test_resource_admin_build_overwrite_audit_by_failures_request(self):
        result = self.resource_admin.overwrite_audit_by_failures(
            "TESTING", "ELIJTEST", "control"
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_FAILURES_XML
        )

    def test_resource_admin_build_overwrite_audit_by_both_successes_and_failures_request(
        self,
    ):
        result = self.resource_admin.overwrite_audit_by_both_successes_and_failures(
            "TESTING", "ELIJTEST", "update"
        )
        self.assertEqual(
            result,
            TestResourceConstants.TEST_RESOURCE_OVERWRITE_AUDIT_BY_BOTH_SUCCESSES_AND_FAILURES_XML,
        )
