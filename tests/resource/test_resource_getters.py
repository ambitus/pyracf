"""Test general resource profile getter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin, SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestResourceGetters(unittest.TestCase):
    maxDiff = None
    resource_admin = ResourceAdmin()

    # ============================================================================
    # Universal Access
    # ============================================================================
    def test_resource_admin_get_universal_access_returns_valid_when_read(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_universal_access("TESTING", "ELIJTEST"), "read"
        )

    def test_resource_admin_get_universal_access_returns_valid_when_none(
        self,
        call_racf_mock: Mock,
    ):
        resource_extract_no_universal_access = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_no_universal_access = resource_extract_no_universal_access.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          NONE               READ    NO</message>",
        )
        call_racf_mock.return_value = resource_extract_no_universal_access
        self.assertIsNone(
            self.resource_admin.get_universal_access("TESTING", "ELIJTEST")
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_get_universal_access_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.resource_admin.get_universal_access("TESTING", "ELIJTEST")

    # ============================================================================
    # My Access
    # ============================================================================
    def test_resource_admin_get_my_access_read(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_my_access("TESTING", "ELIJTEST"), "read"
        )

    def test_resource_admin_get_my_access_none(
        self,
        call_racf_mock: Mock,
    ):
        resource_extract_no_your_access = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_no_your_access = resource_extract_no_your_access.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          READ               NONE    NO</message>",
        )
        call_racf_mock.return_value = resource_extract_no_your_access
        self.assertIsNone(self.resource_admin.get_my_access("TESTING", "ELIJTEST"))

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_get_my_access_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.resource_admin.get_my_access("TESTING", "ELIJTEST")

    # ============================================================================
    # Auditing Rules
    # ============================================================================
    def test_resource_admin_get_audit_rules(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_audit_rules("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_GET_AUDIT_RULES,
        )

    def test_resource_admin_get_audit_rules_single(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_GENERIC_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_audit_rules("TEST*", "ELIJTEST"),
            TestResourceConstants.TEST_GET_AUDIT_RULES_SINGLE,
        )

    def test_resource_admin_get_audit_rules_none(
        self,
        call_racf_mock: Mock,
    ):
        profile_with_none_auditing = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        profile_with_none_auditing = profile_with_none_auditing.replace(
            "<message>SUCCESS(UPDATE),FAILURES(READ)</message>",
            "<message>NONE</message>",
        )
        call_racf_mock.return_value = profile_with_none_auditing
        self.assertIsNone(self.resource_admin.get_audit_rules("TESTING", "ELIJTEST"))

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_get_audit_rules_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.resource_admin.get_audit_rules("TESTING", "ELIJTEST")
