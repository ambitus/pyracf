"""Test general resource profile result parser."""

import copy
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
            "Refusing to make security request to IRRSMO00."
            + "\n\nTarget profile "
            + f"'{profile_name}' already exists as a profile in the '{class_name}' class.",
        )

    def test_resource_admin_add_surfaces_error_from_preliminary_extract(
        self,
        call_racf_mock: Mock,
    ):
        profile_name = "TESTING"
        class_name = "ELIJTEST"
        extract_resource_xml = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        extract_resource_xml = extract_resource_xml.replace(
            "<message>ICH13003I TESTING NOT FOUND</message>",
            "<message>ICH13002I NOT AUTHORIZED TO LIST TESTING</message>",
        )
        call_racf_mock.side_effect = [
            extract_resource_xml,
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_SUCCESS_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            self.resource_admin.add(
                profile_name,
                class_name,
                traits=TestResourceConstants.TEST_ADD_RESOURCE_REQUEST_TRAITS,
            )
        extract_resource_error_json = copy.deepcopy(
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_DICTIONARY
        )
        extract_resource_error_json["securityResult"]["resource"]["commands"][0][
            "messages"
        ] = ["ICH13002I NOT AUTHORIZED TO LIST TESTING"]
        self.assertEqual(
            exception.exception.result,
            extract_resource_error_json,
        )

    def test_resource_admin_avoids_error_on_add_covered_profile(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_GENERIC_SUCCESS_XML,
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_SUCCESS_XML,
        ]
        self.assertEqual(
            self.resource_admin.add("TESTING", "ELIJTEST"),
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_SUCCESS_DICTIONARY,
        )

    # Error: bad Entity Name ELIXTEST
    def test_resource_admin_can_parse_add_resource_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BAD_CLASS_ERROR_XML,
            TestResourceConstants.TEST_ADD_RESOURCE_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            self.resource_admin.add("TESTING", "ELIXTEST")
        self.assertEqual(
            exception.exception.result,
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BAD_CLASS_ERROR_DICTIONARY,
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
            "Refusing to make security request to IRRSMO00."
            + "\n\nTarget profile "
            + f"'{profile_name}' does not exist as a profile in the '{class_name}' class.",
        )

    def test_resource_admin_throws_error_on_alter_covered_profile(
        self,
        call_racf_mock: Mock,
    ):
        profile_name = "TESTING"
        class_name = "ELIJTEST"
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_GENERIC_SUCCESS_XML,
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
            "Refusing to make security request to IRRSMO00."
            + "\n\nTarget profile "
            + f"'{profile_name}' does not exist as a profile in the '{class_name}' class.",
        )

    # Error: bad Universal Access ALL
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
