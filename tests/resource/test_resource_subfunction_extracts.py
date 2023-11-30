"""Test general resource profile setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin, SecurityResponseError
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestResourceSubfunctionExtracts(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    resource_admin = ResourceAdmin()

    # ============================================================================
    # Class Administration
    # ============================================================================
    def test_resource_admin_extract_resource_class_returns_valid_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_CDTINFO_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.extract_resource_class("SHELCITY"),
            TestResourceConstants.TEST_EXTRACT_RESOURCE_CLASS_PROFILE,
        )

    def test_resource_admin_extract_resource_class_raises_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_CDTINFO_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.resource_admin.extract_resource_class("SHELCITY")

    # ============================================================================
    # Started Task Administration
    # ============================================================================
    def test_resource_admin_build_extract_started_task_returns_valid_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_STDATA_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.extract_started_task("TSTTSKEL"),
            TestResourceConstants.TEST_EXTRACT_STARTED_TASK_PROFILE,
        )

    def test_resource_admin_build_extract_started_task_raises_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_STDATA_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.resource_admin.extract_started_task("TSTTSKEL")

    # ============================================================================
    # Custom Field Administration
    # ============================================================================
    def test_resource_admin_build_extract_custom_field_returns_valid_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_CFDEF_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.extract_custom_field("TVSHOW", "user"),
            TestResourceConstants.TEST_EXTRACT_CUSTOM_FIELD_PROFILE,
        )

    def test_resource_admin_build_extract_custom_field_raises_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_CFDEF_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.resource_admin.extract_custom_field("TVSHOW", "user")

    # ============================================================================
    # Kerberos Realm Administration
    # ============================================================================
    def test_resource_admin_build_extract_kerberos_realm_returns_valid_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_KERB_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.extract_kerberos_realm("TSTREALM"),
            TestResourceConstants.TEST_EXTRACT_KERBEROS_REALM_PROFILE,
        )

    def test_resource_admin_build_extract_kerberos_realm_raises_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_KERB_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.resource_admin.extract_kerberos_realm("TSTREALM")

    # ============================================================================
    # Signed Program Administration
    # ============================================================================
    def test_resource_admin_build_extract_signed_program_returns_valid_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SIGVER_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.extract_signed_program("TESTPRGM"),
            TestResourceConstants.TEST_EXTRACT_SIGNED_PROGRAM_PROFILE,
        )

    def test_resource_admin_build_extract_signed_program_raises_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SIGVER_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.resource_admin.extract_signed_program("TESTPRGM")

    # ============================================================================
    # APPC Session Administration
    # ============================================================================
    def test_resource_admin_build_extract_appc_session_returns_valid_on_success(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SESSION_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.extract_appc_session("TSTNET", "TSTLOCLU", "TSTPRTLU"),
            TestResourceConstants.TEST_EXTRACT_APPC_SESSION_PROFILE,
        )

    def test_resource_admin_build_extract_appc_session_raises_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SESSION_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.resource_admin.extract_appc_session("TSTNET", "TSTLOCLU", "TSTPRTLU")
