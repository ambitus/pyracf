"""Test access request builder."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.access.test_access_constants as TestAccessConstants
from pyracf.access.access_admin import AccessAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestAccessRequestBuilder(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> AccessAdmin:
        irrsmo00_init_mock.return_value = None
        return AccessAdmin()

    def test_access_admin_build_add_access_request(self, irrsmo00_init_mock: Mock):
        access_admin = self.boilerplate(irrsmo00_init_mock)
        result = access_admin.add(
            TestAccessConstants.TEST_ADD_ACCESS_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(result, TestAccessConstants.TEST_ADD_ACCESS_REQUEST_XML)

    def test_access_admin_build_alter_access_request(self, irrsmo00_init_mock: Mock):
        access_admin = self.boilerplate(irrsmo00_init_mock)
        result = access_admin.alter(
            TestAccessConstants.TEST_ALTER_ACCESS_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(result, TestAccessConstants.TEST_ALTER_ACCESS_REQUEST_XML)

    def test_access_admin_build_delete_access_request(self, irrsmo00_init_mock: Mock):
        access_admin = self.boilerplate(irrsmo00_init_mock)
        result = access_admin.delete(
            {"resourcename": "TESTING", "classname": "ELIJTEST", "id": "ESWIFT"},
            generate_request_only=True,
        )
        self.assertEqual(result, TestAccessConstants.TEST_DELETE_ACCESS_REQUEST_XML)
