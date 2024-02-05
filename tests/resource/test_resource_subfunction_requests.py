"""Test general resource profile setter functions."""

import unittest

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin

# Resolves F401
__init__


class TestResourceSubfunctionRequests(unittest.TestCase):
    maxDiff = None
    resource_admin = ResourceAdmin(generate_requests_only=True)

    # ============================================================================
    # Class Administration
    # ============================================================================
    def test_resource_admin_build_add_resource_class_request(self):
        result = self.resource_admin.add_resource_class(
            "SHELCITY", TestResourceConstants.TEST_ADD_RESOURCE_CLASS_REQUEST_TRAITS
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_ADD_RESOURCE_CLASS_REQUEST_XML
        )

    def test_resource_admin_build_alter_resource_class_request(self):
        result = self.resource_admin.alter_resource_class(
            "SHELCITY", TestResourceConstants.TEST_ALTER_RESOURCE_CLASS_REQUEST_TRAITS
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_ALTER_RESOURCE_CLASS_REQUEST_XML
        )

    def test_resource_admin_build_delete_resource_class_request(self):
        result = self.resource_admin.delete_resource_class("SHELCITY")
        self.assertEqual(
            result, TestResourceConstants.TEST_DELETE_RESOURCE_CLASS_REQUEST_XML
        )

    # ============================================================================
    # Started Task Administration
    # ============================================================================
    def test_resource_admin_build_add_started_task_request(self):
        result = self.resource_admin.add_started_task("TSTTSKEL")
        self.assertEqual(
            result, TestResourceConstants.TEST_ADD_STARTED_TASK_REQUEST_XML
        )

    def test_resource_admin_build_alter_started_task_request(self):
        result = self.resource_admin.alter_started_task(
            "TSTTSKEL", {"stdata:trusted": True}
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_ALTER_STARTED_TASK_REQUEST_XML
        )

    def test_resource_admin_build_delete_started_task_request(self):
        result = self.resource_admin.delete_started_task("TSTTSKEL")
        self.assertEqual(
            result, TestResourceConstants.TEST_DELETE_STARTED_TASK_REQUEST_XML
        )

    # ============================================================================
    # Custom Field Administration
    # ============================================================================
    def test_resource_admin_build_add_custom_field_request(self):
        result = self.resource_admin.add_custom_field("TVSHOW", "user")
        self.assertEqual(
            result, TestResourceConstants.TEST_ADD_CUSTOM_FIELD_REQUEST_XML
        )

    def test_resource_admin_build_alter_custom_field_request(self):
        result = self.resource_admin.alter_custom_field(
            "TVSHOW",
            "user",
            traits=TestResourceConstants.TEST_ALTER_CUSTOM_FIELD_REQUEST_TRAITS,
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_ALTER_CUSTOM_FIELD_REQUEST_XML
        )

    def test_resource_admin_build_delete_custom_field_request(self):
        result = self.resource_admin.delete_custom_field("TVSHOW", "user")
        self.assertEqual(
            result, TestResourceConstants.TEST_DELETE_CUSTOM_FIELD_REQUEST_XML
        )

    # ============================================================================
    # Kerberos Realm Administration
    # ============================================================================
    def test_resource_admin_build_add_kerberos_realm_request(self):
        result = self.resource_admin.add_kerberos_realm("TSTREALM")
        self.assertEqual(
            result, TestResourceConstants.TEST_ADD_KERBEROS_REALM_REQUEST_XML
        )

    def test_resource_admin_build_alter_kerberos_realm_request(self):
        result = self.resource_admin.alter_kerberos_realm(
            "TSTREALM", traits={"kerb:encryption_algorithms": "AES128"}
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_ALTER_KERBEROS_REALM_REQUEST_XML
        )

    def test_resource_admin_build_delete_kerberos_realm_request(self):
        result = self.resource_admin.delete_kerberos_realm("TSTREALM")
        self.assertEqual(
            result, TestResourceConstants.TEST_DELETE_KERBEROS_REALM_REQUEST_XML
        )

    # ============================================================================
    # Signed Program Administration
    # ============================================================================
    def test_resource_admin_build_add_signed_program_request(self):
        result = self.resource_admin.add_signed_program("TESTPRGM")
        self.assertEqual(
            result, TestResourceConstants.TEST_ADD_SIGNED_PROGRAM_REQUEST_XML
        )

    def test_resource_admin_build_alter_signed_program_request(self):
        result = self.resource_admin.alter_signed_program(
            "TESTPRGM", traits={"sigver:log_signature_verification_events": "SUCCESS"}
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_ALTER_SIGNED_PROGRAM_REQUEST_XML
        )

    def test_resource_admin_build_delete_signed_program_request(self):
        result = self.resource_admin.delete_signed_program("TESTPRGM")
        self.assertEqual(
            result, TestResourceConstants.TEST_DELETE_SIGNED_PROGRAM_REQUEST_XML
        )

    # ============================================================================
    # APPC Session Administration
    # ============================================================================
    def test_resource_admin_build_add_appc_session_request(self):
        result = self.resource_admin.add_appc_session("TSTNET", "TSTLOCLU", "TSTPRTLU")
        self.assertEqual(
            result, TestResourceConstants.TEST_ADD_APPC_SESSION_REQUEST_XML
        )

    def test_resource_admin_build_alter_appc_session_request(self):
        result = self.resource_admin.alter_appc_session(
            "TSTNET", "TSTLOCLU", "TSTPRTLU", traits={"session:locked": True}
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_ALTER_APPC_SESSION_REQUEST_XML
        )

    def test_resource_admin_build_delete_appc_session_request(self):
        result = self.resource_admin.delete_appc_session(
            "TSTNET", "TSTLOCLU", "TSTPRTLU"
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_DELETE_APPC_SESSION_REQUEST_XML
        )
