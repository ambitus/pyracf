"""Test general resource profile result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin
from pyracf.common.irrsmo00 import IRRSMO00
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestResourceResultParser(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    resource_admin = ResourceAdmin()

    # ============================================================================
    # Add Resource
    # ============================================================================
    def test_resource_admin_can_parse_add_resource_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.add("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_SUCCESS_DICTIONARY,
        )

    # Error: Invalid Entity Name ELIXTEST
    def test_resource_admin_can_parse_add_resource_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.resource_admin.add("TESTING", "ELIXTEST")
        self.assertEqual(
            exception.exception.results,
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter Resource
    # ============================================================================
    def test_resource_admin_can_parse_alter_resource_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.alter(
                "TESTING",
                "ELIJTEST",
                traits=TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_TRAITS,
            ),
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_SUCCESS_DICTIONARY,
        )

    # Error: Invalid Universal Access ALL
    def test_resource_admin_can_parse_alter_resource_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.resource_admin.alter(
                "TESTING",
                "ELIJTEST",
                traits=TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_ERROR_TRAITS,
            )
        self.assertEqual(
            exception.exception.results,
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Extract Resource
    # ============================================================================
    def test_resource_admin_can_parse_extract_resource_base_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.extract("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_DICTIONARY,
        )

    # Successful parse of multiple profiles in one command
    def test_resource_admin_can_parse_extract_resource_multi_base_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_MULTI_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.extract("*", "XFACILIT"),
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_MULTI_BASE_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_can_parse_extract_resource_base_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.resource_admin.extract("TESTING", "ELIJTEST")
        self.assertEqual(
            exception.exception.results,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Resource
    # ============================================================================
    def test_resource_admin_can_parse_delete_resource_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_DELETE_RESOURCE_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.delete("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_DELETE_RESOURCE_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_can_parse_delete_resource_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_DELETE_RESOURCE_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.resource_admin.delete("TESTING", "ELIJTEST")
        self.assertEqual(
            exception.exception.results,
            TestResourceConstants.TEST_DELETE_RESOURCE_RESULT_ERROR_DICTIONARY,
        )
