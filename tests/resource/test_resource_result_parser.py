"""Test general resource profile result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import (
    AddOperationError,
    AlterOperationError,
    ResourceAdmin,
    SecurityRequestError,
)
from pyracf.common.irrsmo00 import IRRSMO00

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
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_SUCCESS_XML,
        ]
        self.assertEqual(
            self.resource_admin.add("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_SUCCESS_DICTIONARY,
        )

    def test_resource_admin_throws_error_on_add_existing_profile(
        self,
        call_racf_mock: Mock,
    ):
        profile_name = "TESTING"
        class_name = "ELIJTEST"
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_SUCCESS_XML,
        ]
        with self.assertRaises(AddOperationError) as exception:
            self.resource_admin.add(
                profile_name,
                class_name,
                traits=TestResourceConstants.TEST_ADD_RESOURCE_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.message,
            "Security request made to IRRSMO00 failed."
            + "\n\nTarget profile "
            + f"'{profile_name}' already exists as a profile in the {class_name} class.",
        )

    # Error: Invalid Entity Name ELIXTEST
    def test_resource_admin_can_parse_add_resource_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_INVALID_CLASS_ERROR_XML,
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            self.resource_admin.add("TESTING", "ELIXTEST")
        self.assertEqual(
            exception.exception.result,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_INVALID_CLASS_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter Resource
    # ============================================================================
    def test_resource_admin_can_parse_alter_resource_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_SUCCESS_XML,
        ]
        self.assertEqual(
            self.resource_admin.alter(
                "TESTING",
                "ELIJTEST",
                traits=TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_TRAITS,
            ),
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_SUCCESS_DICTIONARY,
        )

    def test_resource_admin_throws_error_on_alter_new_profile(
        self,
        call_racf_mock: Mock,
    ):
        profile_name = "TESTING"
        class_name = "ELIJTEST"
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML,
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_SUCCESS_XML,
        ]
        with self.assertRaises(AlterOperationError) as exception:
            self.resource_admin.alter(
                profile_name,
                class_name,
                traits=TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.message,
            "Security request made to IRRSMO00 failed."
            + "\n\nTarget profile "
            + f"'{profile_name}' does not exist as a profile in the {class_name} class.",
        )

    # Error: Invalid Universal Access ALL
    def test_resource_admin_can_parse_alter_resource_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            self.resource_admin.alter(
                "TESTING",
                "ELIJTEST",
                traits=TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_ERROR_TRAITS,
            )
        self.assertEqual(
            exception.exception.result,
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
            exception.exception.result,
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
            exception.exception.result,
            TestResourceConstants.TEST_DELETE_RESOURCE_RESULT_ERROR_DICTIONARY,
        )
