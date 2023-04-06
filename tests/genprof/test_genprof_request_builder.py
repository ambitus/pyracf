"""Test general resource profile request builder."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.genprof.test_genprof_constants as TestGenprofConstants
from pyracf.genprof.resource_admin import ResourceAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestGenprofRequestBuilder(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ResourceAdmin:
        irrsmo00_init_mock.return_value = None
        return ResourceAdmin()

    def test_resource_admin_build_add_genprof_request(self, irrsmo00_init_mock: Mock):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        result = resource_admin.add(
            TestGenprofConstants.TEST_ADD_GENPROF_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(result, TestGenprofConstants.TEST_ADD_GENPROF_REQUEST_XML)

    def test_resource_admin_build_alter_genprof_request(self, irrsmo00_init_mock: Mock):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        result = resource_admin.alter(
            TestGenprofConstants.TEST_ALTER_GENPROF_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(result, TestGenprofConstants.TEST_ALTER_GENPROF_REQUEST_XML)

    def test_resource_admin_build_extract_genprof_request_base(
        self, irrsmo00_init_mock: Mock
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        result = resource_admin.extract(
            TestGenprofConstants.TEST_EXTRACT_GENPROF_REQUEST_BASE_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(
            result, TestGenprofConstants.TEST_EXTRACT_GENPROF_REQUEST_BASE_XML
        )

    def test_resource_admin_build_delete_genprof_request(
        self, irrsmo00_init_mock: Mock
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        result = resource_admin.delete(
            "TESTING", "ELIJTEST", generate_request_only=True
        )
        self.assertEqual(result, TestGenprofConstants.TEST_DELETE_GENPROF_REQUEST_XML)
