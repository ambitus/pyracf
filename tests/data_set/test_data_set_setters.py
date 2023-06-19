"""Test data set setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.data_set.test_data_set_constants as TestDataSetConstants
from pyracf import DataSetAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestDataSetSetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> DataSetAdmin:
        irrsmo00_init_mock.return_value = None
        return DataSetAdmin(generate_requests_only=True)

    def test_data_set_admin_build_set_uacc_request(self, irrsmo00_init_mock: Mock):
        data_set_admin = self.boilerplate(irrsmo00_init_mock)
        result = data_set_admin.set_universal_access(
            "ESWIFT.TEST.T1136242.P3020470", "ALTER"
        )
        self.assertEqual(
            result, TestDataSetConstants.TEST_DATA_SET_SET_UNIVERSAL_ACCESS_XML
        )
