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
    # DatasetAdmin.get_uacc(class_name)
    # ============================================================================
    def test_dataset_admin_get_uacc_returns_valid_when_read(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        self.assertTrue(
            dataset_admin.get_uacc("ESWIFT.TEST.T1136242.P3020470").title() == "Read"
        )

    def test_dataset_admin_get_uacc_returns_valid_when_none(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        dataset_extract_no_uacc = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        dataset_extract_no_uacc = dataset_extract_no_uacc.replace(
            "<message> 00    ESWIFT          READ          NO      NO</message>",
            "<message> 00    ESWIFT          NONE          NO      NO</message>",
        )
        call_racf_mock.return_value = dataset_extract_no_uacc
        self.assertTrue(dataset_admin.get_uacc("ESWIFT.TEST.T1136242.P3020470") is None)

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_dataset_admin_get_uacc_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            dataset_admin.get_uacc("ESWIFT.TEST.T1136242.P3020470")

    # ============================================================================
    # DatasetAdmin.get_your_acc(class_name)
    # ============================================================================
    def test_dataset_admin_get_your_acc_returns_valid_when_alter(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        self.assertTrue(
            dataset_admin.get_your_acc("ESWIFT.TEST.T1136242.P3020470").title()
            == "Alter"
        )

    def test_dataset_admin_get_your_acc_returns_valid_when_none(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        dataset_extract_no_your_acc = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_SUCCESS_XML
        )
        dataset_extract_no_your_acc = dataset_extract_no_your_acc.replace(
            "<message> ALTER        SYS1           NON-VSAM</message>",
            "<message> NONE         SYS1           NON-VSAM</message>",
        )
        call_racf_mock.return_value = dataset_extract_no_your_acc
        self.assertTrue(
            dataset_admin.get_your_acc("ESWIFT.TEST.T1136242.P3020470") is None
        )

    # Error in environment, ESWIFT.TEST.T1136242.P3020470 already deleted/not added
    def test_dataset_admin_get_your_acc_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestDatasetConstants.TEST_EXTRACT_DATASET_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            dataset_admin.get_your_acc("ESWIFT.TEST.T1136242.P3020470")
