"""Test data set profile result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.data_set.test_data_set_constants as TestDataSetConstants
from pyracf import DataSetAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestDataSetResultParser(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> DataSetAdmin:
        irrsmo00_init_mock.return_value = None
        return DataSetAdmin()

    # ============================================================================
    # Add Data Set
    # ============================================================================
    def test_data_set_admin_can_parse_add_data_set_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            data_set_admin.add(
                "ESWIFT.TEST.T1136242.P3020470",
                TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
            ),
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_SUCCESS_DICTIONARY,
        )

    # Error User or Group ESWIFF not defined to RACF
    def test_data_set_admin_can_parse_add_data_set_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            data_set_admin.add(
                "ESWIFF.TEST.T1136242.P3020470",
                TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.results,
            TestDataSetConstants.TEST_ADD_DATA_SET_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter Data Set
    # ============================================================================
    def test_data_set_admin_can_parse_alter_data_set_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            data_set_admin.alter(
                "ESWIFT.TEST.T1136242.P3020470",
                TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
            ),
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 data set does not exist
    def test_data_set_admin_can_parse_alter_data_set_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            data_set_admin.alter(
                "ESWIFT.TEST.T1136242.P3020470",
                TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.results,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Extract Data Set
    # ============================================================================
    def test_data_set_admin_can_parse_extract_data_set_base_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470"),
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_SUCCESS_DICTIONARY,
        )

    def test_data_set_admin_can_parse_extract_data_set_generic_base_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_GENERIC_BASE_SUCCESS_XML
        )
        self.assertEqual(
            data_set_admin.extract("ESWIFT.TEST.T1136242.*"),
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_GENERIC_BASE_SUCCESS_DICTIONARY,
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_data_set_admin_can_parse_extract_data_set_base_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(
            exception.exception.results,
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Data Set
    # ============================================================================
    def test_data_set_admin_can_parse_delete_data_set_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_DELETE_DATA_SET_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            data_set_admin.delete("ESWIFT.TEST.T1136242.P3020470"),
            TestDataSetConstants.TEST_DELETE_DATA_SET_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_data_set_admin_can_parse_delete_data_set_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDataSetConstants.TEST_DELETE_DATA_SET_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            data_set_admin.delete("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(
            exception.exception.results,
            TestDataSetConstants.TEST_DELETE_DATA_SET_RESULT_ERROR_DICTIONARY,
        )
