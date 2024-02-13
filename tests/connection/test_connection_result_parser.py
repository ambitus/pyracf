"""Test connection result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin, SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestConnectionResultParser(unittest.TestCase):
    maxDiff = None
    connection_admin = ConnectionAdmin()

    # ============================================================================
    # Connect Connection
    # ============================================================================
    def test_connection_admin_can_parse_connect_connection_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_CONNECT_CONNECTION_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.connection_admin.connect(
                "ESWIFT",
                "TESTGRP0",
                traits=TestConnectionConstants.TEST_CONNECT_CONNECTION_REQUEST_TRAITS,
            ),
            TestConnectionConstants.TEST_CONNECT_CONNECTION_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTGRP0 group already deleted/not added
    def test_connection_admin_can_parse_connect_connection_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_CONNECT_CONNECTION_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.connection_admin.connect(
                "ESWIFT",
                "TESTGRP0",
                traits=TestConnectionConstants.TEST_CONNECT_CONNECTION_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.result,
            TestConnectionConstants.TEST_CONNECT_CONNECTION_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Connection
    # ============================================================================
    def test_connection_admin_can_parse_delete_connection_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_DELETE_CONNECTION_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.connection_admin.delete("ESWIFT", "TESTGRP0"),
            TestConnectionConstants.TEST_DELETE_CONNECTION_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTGRP0 group already deleted/not added
    def test_connection_admin_can_parse_delete_connection_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_DELETE_CONNECTION_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.connection_admin.delete("ESWIFT", "TESTGRP0")
        self.assertEqual(
            exception.exception.result,
            TestConnectionConstants.TEST_DELETE_CONNECTION_RESULT_ERROR_DICTIONARY,
        )
