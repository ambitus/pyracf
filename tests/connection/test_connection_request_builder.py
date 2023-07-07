"""Test connection request builder."""

import unittest
from unittest.mock import Mock

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestConnectionRequestBuilder(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    connection_admin = ConnectionAdmin(generate_requests_only=True)

    def test_connection_admin_build_add_connection_request(self):
        result = self.connection_admin.add("ESWIFT", "TESTGRP0")
        print(result)
        print(TestConnectionConstants.TEST_ADD_CONNECTION_REQUEST_XML)
        self.assertEqual(
            result, TestConnectionConstants.TEST_ADD_CONNECTION_REQUEST_XML
        )

    def test_connection_admin_build_alter_connection_request(self):
        result = self.connection_admin.alter(
            "ESWIFT",
            "TESTGRP0",
            traits=TestConnectionConstants.TEST_ALTER_CONNECTION_REQUEST_TRAITS,
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_ALTER_CONNECTION_REQUEST_XML
        )

    def test_connection_admin_build_delete_connection_request(self):
        result = self.connection_admin.delete("ESWIFT", "TESTGRP0")
        self.assertEqual(
            result, TestConnectionConstants.TEST_DELETE_CONNECTION_REQUEST_XML
        )
