"""Test data set profile request builder."""

import unittest
from unittest.mock import Mock

import __init__

import tests.data_set.test_data_set_constants as TestDataSetConstants
from pyracf import DataSetAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestDataSetRequestBuilder(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    data_set_admin = DataSetAdmin(generate_requests_only=True)

    def test_data_set_admin_build_add_data_set_request(self):
        result = self.data_set_admin.add(
            "ESWIFT.TEST.T1136242.P3020470",
            traits=TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
        )
        self.assertEqual(result, TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_XML)

    def test_data_set_admin_build_add_data_set_request_generic(self):
        result = self.data_set_admin.add(
            "ESWIFT.TEST.**",
            traits=TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_TRAITS,
            generic=True,
        )
        self.assertEqual(
            result, TestDataSetConstants.TEST_ADD_DATA_SET_REQUEST_GENERIC_XML
        )

    def test_data_set_admin_build_alter_data_set_request(self):
        result = self.data_set_admin.alter(
            "ESWIFT.TEST.T1136242.P3020470",
            traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
        )
        self.assertEqual(result, TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_XML)

    def test_data_set_admin_build_extract_data_set_request_base(self):
        result = self.data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(
            result, TestDataSetConstants.TEST_EXTRACT_DATA_SET_REQUEST_BASE_XML
        )

    def test_data_set_admin_build_extract_data_set_request_generic_base(self):
        result = self.data_set_admin.extract("ESWIFT.TEST.T1136242.*")
        self.assertEqual(
            result, TestDataSetConstants.TEST_EXTRACT_DATA_SET_REQUEST_GENRIC_BASE_XML
        )

    def test_data_set_admin_build_delete_dataset_request(self):
        result = self.data_set_admin.delete("ESWIFT.TEST.T1136242.P3020470")
        self.assertEqual(result, TestDataSetConstants.TEST_DELETE_DATA_SET_REQUEST_XML)
