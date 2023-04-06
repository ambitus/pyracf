"""Test dataset setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.dataset.test_dataset_constants as TestDatasetConstants
from pyracf.dataset.dataset_admin import DatasetAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestDatasetSetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> DatasetAdmin:
        irrsmo00_init_mock.return_value = None
        return DatasetAdmin()

    def test_dataset_admin_build_set_uacc_request(self, irrsmo00_init_mock: Mock):
        dataset_admin = self.boilerplate(irrsmo00_init_mock)
        result = dataset_admin.set_uacc(
            "ESWIFT.TEST.T1136242.P3020470", "ALTER", generate_request_only=True
        )
        self.assertEqual(result, TestDatasetConstants.TEST_DATASET_SET_UACC_XML)
