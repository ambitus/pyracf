"""Test data set setter functions."""

import unittest

import __init__

import tests.data_set.test_data_set_constants as TestDataSetConstants
from pyracf import DataSetAdmin

# Resolves F401
__init__


class TestDataSetSetters(unittest.TestCase):
    maxDiff = None
    data_set_admin = DataSetAdmin(generate_requests_only=True)

    def test_data_set_admin_build_set_uacc_request(self):
        result = self.data_set_admin.set_universal_access(
            "ESWIFT.TEST.T1136242.P3020470", "ALTER"
        )
        self.assertEqual(
            result, TestDataSetConstants.TEST_DATA_SET_SET_UNIVERSAL_ACCESS_XML
        )
