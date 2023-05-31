"""Test connection request builder."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestConnectionRequestBuilder(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ConnectionAdmin:
        irrsmo00_init_mock.return_value = None
        return ConnectionAdmin()

    def test_connection_admin_build_add_connection_request(self, irrsmo00_init_mock: Mock):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.add(
            TestConnectionConstants.TEST_ADD_CONNECTION_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(result, TestConnectionConstants.TEST_ADD_CONNECTION_REQUEST_XML)

    def test_connection_admin_build_alter_connection_request(self, irrsmo00_init_mock: Mock):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.alter(
            TestConnectionConstants.TEST_ALTER_CONNECTION_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(result, TestConnectionConstants.TEST_ALTER_CONNECTION_REQUEST_XML)

    def test_connection_admin_build_delete_connection_request(self, irrsmo00_init_mock: Mock):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.delete(
            TestConnectionConstants.TEST_DELETE_CONNECTION_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(result, TestConnectionConstants.TEST_DELETE_CONNECTION_REQUEST_XML)
