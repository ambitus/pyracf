"""Test dataset profile request builder."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.dataset.test_dataset_constants as TestDatasetConstants
from pyracf import DatasetAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestDatasetRequestBuilder(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> DatasetAdmin:
        irrsmo00_init_mock.return_value = None
        return DatasetAdmin(generate_requests_only=True)

    def test_dataset_admin_build_add_dataset_request(self, irrsmo00_init_mock: Mock):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        result = dataset_admin.add(
            "ESWIFT.TEST.T1136242.P3020470",
            TestDatasetConstants.TEST_ADD_DATASET_REQUEST_TRAITS,
        )
        self.assertEqual(result, TestDatasetConstants.TEST_ADD_DATASET_REQUEST_XML)

    def test_dataset_admin_build_add_dataset_request_generic(
        self, irrsmo00_init_mock: Mock
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        result = dataset_admin.add(
            "ESWIFT.TEST.**",
            TestDatasetConstants.TEST_ADD_DATASET_REQUEST_TRAITS,
            generic=True,
        )
        self.assertEqual(
            result, TestDatasetConstants.TEST_ADD_DATASET_REQUEST_GENERIC_XML
        )

    def test_dataset_admin_build_alter_dataset_request(self, irrsmo00_init_mock: Mock):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        result = dataset_admin.alter(
            "ESWIFT.TEST.T1136242.P3020470",
            TestDatasetConstants.TEST_ALTER_DATASET_REQUEST_TRAITS,
        )
        self.assertEqual(result, TestDatasetConstants.TEST_ALTER_DATASET_REQUEST_XML)

    def test_dataset_admin_build_extract_dataset_request_base(
        self, irrsmo00_init_mock: Mock
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        result = dataset_admin.extract("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(
            result, TestDatasetConstants.TEST_EXTRACT_DATASET_REQUEST_BASE_XML
        )

    def test_dataset_admin_build_extract_dataset_request_generic_base(
        self, irrsmo00_init_mock: Mock
    ):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        result = dataset_admin.extract("ESWIFT.TEST.T1136242.*")
        self.assertEqual(
            result, TestDatasetConstants.TEST_EXTRACT_DATASET_REQUEST_GENRIC_BASE_XML
        )

    def test_dataset_admin_build_delete_dataset_request(self, irrsmo00_init_mock: Mock):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        result = dataset_admin.delete("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(result, TestDatasetConstants.TEST_DELETE_DATASET_REQUEST_XML)
