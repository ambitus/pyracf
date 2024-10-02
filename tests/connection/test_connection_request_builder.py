"""Test connection request builder."""

import unittest

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin

# Resolves F401
__init__


class TestConnectionRequestBuilder(unittest.TestCase):
    maxDiff = None
    connection_admin = ConnectionAdmin(generate_requests_only=True)

    def test_connection_admin_build_connect_connection_request(self):
        result = self.connection_admin.connect(
            "ESWIFT",
            "testgrp0",
            traits=TestConnectionConstants.TEST_CONNECT_CONNECTION_REQUEST_TRAITS,
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECT_CONNECTION_REQUEST_XML
        )

    def test_connection_admin_build_delete_connection_request(self):
        result = self.connection_admin.delete("ESWIFT", "testgrp0")
        self.assertEqual(
            result, TestConnectionConstants.TEST_DELETE_CONNECTION_REQUEST_XML
        )
