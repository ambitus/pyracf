"""Test dataset profile result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.dataset.test_dataset_constants as TestDatasetConstants
from pyracf import DatasetAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestDatasetResultParser(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> DatasetAdmin:
        irrsmo00_init_mock.return_value = None
        return DatasetAdmin()

    # ============================================================================
    # Add Dataset
    # ============================================================================
    def test_dataset_admin_can_parse_add_dataset_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_ADD_DATASET_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            dataset_admin.add(
                "ESWIFT.TEST.T1136242.P3020470",
                TestDatasetConstants.TEST_ADD_DATASET_REQUEST_TRAITS,
            ),
            TestDatasetConstants.TEST_ADD_DATASET_RESULT_SUCCESS_DICTIONARY,
        )

    # Error User or Group ESWIFF not defined to RACF
    def test_dataset_admin_can_parse_add_dataset_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_ADD_DATASET_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            dataset_admin.add(
                "ESWIFF.TEST.T1136242.P3020470",
                TestDatasetConstants.TEST_ADD_DATASET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.results,
            TestDatasetConstants.TEST_ADD_DATASET_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter Dataset
    # ============================================================================
    def test_dataset_admin_can_parse_alter_dataset_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_ALTER_DATASET_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            dataset_admin.alter(
                "ESWIFT.TEST.T1136242.P3020470",
                TestDatasetConstants.TEST_ALTER_DATASET_REQUEST_TRAITS,
            ),
            TestDatasetConstants.TEST_ALTER_DATASET_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 dataset does not exist
    def test_dataset_admin_can_parse_alter_dataset_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_ALTER_DATASET_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            dataset_admin.alter(
                "ESWIFT.TEST.T1136242.P3020470",
                TestDatasetConstants.TEST_ALTER_DATASET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.results,
            TestDatasetConstants.TEST_ALTER_DATASET_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Extract Dataset
    # ============================================================================
    def test_dataset_admin_can_parse_extract_dataset_base_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            dataset_admin.extract("ESWIFT.TEST.T1136242.P3020470"),
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_DICTIONARY,
        )

    def test_dataset_admin_can_parse_extract_dataset_generic_base_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_GENERIC_BASE_SUCCESS_XML
        )
        self.assertEqual(
            dataset_admin.extract("ESWIFT.TEST.T1136242.*"),
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_GENERIC_BASE_SUCCESS_DICTIONARY,
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_dataset_admin_can_parse_extract_dataset_base_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            dataset_admin.extract("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(
            exception.exception.results,
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Dataset
    # ============================================================================
    def test_dataset_admin_can_parse_delete_dataset_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_DELETE_DATASET_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            dataset_admin.delete("ESWIFT.TEST.T1136242.P3020470"),
            TestDatasetConstants.TEST_DELETE_DATASET_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_dataset_admin_can_parse_delete_dataset_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_DELETE_DATASET_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            dataset_admin.delete("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(
            exception.exception.results,
            TestDatasetConstants.TEST_DELETE_DATASET_RESULT_ERROR_DICTIONARY,
        )
