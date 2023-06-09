"""Test dataset profile getter functions."""

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
class TestDatasetGetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> DatasetAdmin:
        irrsmo00_init_mock.return_value = None
        return DatasetAdmin()

    # ============================================================================
    # Access
    # ============================================================================
    def test_dataset_admin_get_universal_access_returns_valid_when_read(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        self.assertTrue(
            dataset_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470").title()
            == "Read"
        )

    def test_dataset_admin_get_universal_access_returns_valid_when_none(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        dataset_extract_no_universal_access = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        dataset_extract_no_universal_access = (
            dataset_extract_no_universal_access.replace(
                "<message> 00    ESWIFT          READ          NO      NO</message>",
                "<message> 00    ESWIFT          NONE          NO      NO</message>",
            )
        )
        call_racf_mock.return_value = dataset_extract_no_universal_access
        self.assertTrue(
            dataset_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470") is None
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_dataset_admin_get_universal_access_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            dataset_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470")

    def test_dataset_admin_get_my_access_returns_valid_when_alter(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        self.assertTrue(
            dataset_admin.get_my_access("ESWIFT.TEST.T1136242.P3020470").title()
            == "Alter"
        )

    def test_dataset_admin_get_my_access_returns_valid_when_none(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        dataset_extract_no_my_access = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        dataset_extract_no_my_access = dataset_extract_no_my_access.replace(
            "<message> ALTER        SYS1           NON-VSAM</message>",
            "<message> NONE         SYS1           NON-VSAM</message>",
        )
        call_racf_mock.return_value = dataset_extract_no_my_access
        self.assertTrue(
            dataset_admin.get_my_access("ESWIFT.TEST.T1136242.P3020470") is None
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_dataset_admin_get_my_access_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            dataset_admin.get_my_access("ESWIFT.TEST.T1136242.P3020470")
