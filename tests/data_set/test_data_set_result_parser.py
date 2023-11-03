"""Test data set profile result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.data_set.test_data_set_constants as TestDataSetConstants
from pyracf import (
    AddOperationError,
    AlterOperationError,
    DataSetAdmin,
    SecurityRequestError,
)
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestDataSetResultParser(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    data_set_admin = DataSetAdmin()

    # ============================================================================
    # Add Data Set
    # ============================================================================
    def test_data_set_admin_can_parse_add_data_set_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_XML,
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_SUCCESS_XML,
        ]
        self.assertEqual(
            self.data_set_admin.add(
                "ESWIFT.TEST.T1136242.P3020470",
                traits=TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
            ),
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_SUCCESS_DICTIONARY,
        )

    def test_data_set_admin_thows_error_on_add_existing_data_set_profile(
        self,
        call_racf_mock: Mock,
    ):
        profile_name = "ESWIFT.TEST.T1136242.P3020470"
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML,
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_SUCCESS_XML,
        ]
        with self.assertRaises(AddOperationError) as exception:
            self.data_set_admin.add(
                profile_name,
                traits=TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.message,
            "Refusing to make security request to IRRSMO00."
            + "\n\nTarget profile "
            + f"'{profile_name}' already exists as a "
            + f"'{self.data_set_admin._profile_type}' profile.",
        )

    def test_dataset_admin_avoids_error_on_add_covered_profile(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_GENERIC_BASE_ONLY_SUCCESS_XML,
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_SUCCESS_XML,
        ]
        self.assertEqual(
            self.data_set_admin.add(
                "ESWIFT.TEST.T1136242.P3020470",
                traits=TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
            ),
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in command, ESWIFTTESTT1136242P3020470 is not a valid DATASET
    def test_data_set_admin_can_parse_add_data_set_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BAD_ATTRIBUTE_ERROR_XML,
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            self.data_set_admin.add(
                "ESWIFTTESTT1136242P3020470",
                traits=TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.result,
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BAD_ATTRIBUTE_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter Data Set
    # ============================================================================
    def test_data_set_admin_can_parse_alter_data_set_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_SUCCESS_XML,
        ]
        self.assertEqual(
            self.data_set_admin.alter(
                "ESWIFT.TEST.T1136242.P3020470",
                traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
            ),
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_SUCCESS_DICTIONARY,
        )

    def test_data_set_admin_thows_error_on_alter_new_data_set_profile(
        self,
        call_racf_mock: Mock,
    ):
        profile_name = "ESWIFT.TEST.T1136242.P3020470"
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_XML,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_SUCCESS_XML,
        ]
        with self.assertRaises(AlterOperationError) as exception:
            self.data_set_admin.alter(
                profile_name,
                traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.message,
            "Refusing to make security request to IRRSMO00."
            + "\n\nTarget profile "
            + f"'{profile_name}' does not exist as a "
            + f"'{self.data_set_admin._profile_type}' profile.",
        )

    def test_dataset_admin_throws_error_on_alter_covered_profile(
        self,
        call_racf_mock: Mock,
    ):
        profile_name = "ESWIFT.TEST.T1136242.P3020470"
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_GENERIC_BASE_ONLY_SUCCESS_XML,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_SUCCESS_XML,
        ]
        with self.assertRaises(AlterOperationError) as exception:
            self.data_set_admin.alter(
                profile_name,
                traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.message,
            "Refusing to make security request to IRRSMO00."
            + "\n\nTarget profile "
            + f"'{profile_name}' does not exist as a "
            + f"'{self.data_set_admin._profile_type}' profile.",
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 data set does not exist
    def test_data_set_admin_can_parse_alter_data_set_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            self.data_set_admin.alter(
                "ESWIFT.TEST.T1136242.P3020470",
                traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.result,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Extract Data Set
    # ============================================================================
    def test_data_set_admin_can_parse_extract_data_set_base_only_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertEqual(
            self.data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470"),
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_DICTIONARY,
        )

    def test_data_set_admin_can_parse_extract_data_set_generic_base_only_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_GENERIC_BASE_ONLY_SUCCESS_XML
        )
        self.assertEqual(
            self.data_set_admin.extract("ESWIFT.TEST.T1136242.*"),
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_GENERIC_BASE_ONLY_SUCCESS_DICTIONARY,
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_data_set_admin_can_parse_extract_data_set_base_only_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(
            exception.exception.result,
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Data Set
    # ============================================================================
    def test_data_set_admin_can_parse_delete_data_set_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_DELETE_DATA_SET_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.data_set_admin.delete("ESWIFT.TEST.T1136242.P3020470"),
            TestDataSetConstants.TEST_DELETE_DATA_SET_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_data_set_admin_can_parse_delete_data_set_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_DELETE_DATA_SET_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.data_set_admin.delete("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(
            exception.exception.result,
            TestDataSetConstants.TEST_DELETE_DATA_SET_RESULT_ERROR_DICTIONARY,
        )
