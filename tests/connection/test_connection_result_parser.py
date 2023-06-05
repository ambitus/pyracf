"""Test connection result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestConnectionResultParser(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ConnectionAdmin:
        irrsmo00_init_mock.return_value = None
        return ConnectionAdmin()

    # ============================================================================
    # Add Connection
    # ============================================================================
    def test_connection_admin_can_parse_add_connection_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_ADD_CONNECTION_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            connection_admin.add(
                TestConnectionConstants.TEST_ADD_CONNECTION_REQUEST_TRAITS
            ),
            TestConnectionConstants.TEST_ADD_CONNECTION_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTGRP0 group already deleted/not added
    def test_connection_admin_can_parse_add_connection_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_ADD_CONNECTION_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            connection_admin.add(
                TestConnectionConstants.TEST_ADD_CONNECTION_REQUEST_TRAITS
            )
        self.assertEqual(
            exception.exception.results,
            TestConnectionConstants.TEST_ADD_CONNECTION_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter Connection
    # ============================================================================
    def test_connection_admin_can_parse_alter_connection_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_ALTER_CONNECTION_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            connection_admin.alter(
                TestConnectionConstants.TEST_ALTER_CONNECTION_REQUEST_TRAITS
            ),
            TestConnectionConstants.TEST_ALTER_CONNECTION_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTGRP0 group already deleted/not added
    def test_connection_admin_can_parse_alter_connection_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_ALTER_CONNECTION_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            connection_admin.alter(
                TestConnectionConstants.TEST_ALTER_CONNECTION_REQUEST_TRAITS
            )
        self.assertEqual(
            exception.exception.results,
            TestConnectionConstants.TEST_ALTER_CONNECTION_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Connection
    # ============================================================================
    def test_connection_admin_can_parse_delete_connection_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_DELETE_CONNECTION_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            connection_admin.delete(
                TestConnectionConstants.TEST_DELETE_CONNECTION_REQUEST_TRAITS
            ),
            TestConnectionConstants.TEST_DELETE_CONNECTION_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTGRP0 group already deleted/not added
    def test_connection_admin_can_parse_delete_connection_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestConnectionConstants.TEST_DELETE_CONNECTION_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            connection_admin.delete(
                TestConnectionConstants.TEST_DELETE_CONNECTION_REQUEST_TRAITS
            )
        self.assertEqual(
            exception.exception.results,
            TestConnectionConstants.TEST_DELETE_CONNECTION_RESULT_ERROR_DICTIONARY,
        )
