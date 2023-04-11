"""Test general resource profile result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.genprof.test_genprof_constants as TestGenprofConstants
from pyracf.common.security_request_error import SecurityRequestError
from pyracf.genprof.resource_admin import ResourceAdmin

# Resolves F401
__init__


@patch("pyracf.common.security_request.SecurityRequest.dump_request_xml")
@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestGenprofResultParser(unittest.TestCase):
    maxDiff = None

    def boilerplate(
        self, irrsmo00_init_mock: Mock, dump_request_xml_mock: Mock
    ) -> ResourceAdmin:
        irrsmo00_init_mock.return_value = None
        dump_request_xml_mock.return_value = b""
        return ResourceAdmin()

    # ============================================================================
    # Add Genprof
    # ============================================================================
    def test_resource_admin_can_parse_add_genprof_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_ADD_GENPROF_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            resource_admin.add({"resourcename": "TESTING", "classname": "ELIJTEST"}),
            TestGenprofConstants.TEST_ADD_GENPROF_RESULT_SUCCESS_DICTIONARY,
        )

    # Error: Invalid Entity Name ELIXTEST
    def test_resource_admin_can_parse_add_genprof_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_ADD_GENPROF_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            resource_admin.add({"resourcename": "TESTING", "classname": "ELIXTEST"})
        self.assertEqual(
            exception.exception.results,
            TestGenprofConstants.TEST_ADD_GENPROF_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter Genprof
    # ============================================================================
    def test_resource_admin_can_parse_alter_genprof_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_ALTER_GENPROF_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            resource_admin.alter(
                TestGenprofConstants.TEST_ALTER_GENPROF_REQUEST_TRAITS
            ),
            TestGenprofConstants.TEST_ALTER_GENPROF_RESULT_SUCCESS_DICTIONARY,
        )

    # Error: Invalid Universal Access ALL
    def test_resource_admin_can_parse_alter_genprof_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_ALTER_GENPROF_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            resource_admin.alter(
                TestGenprofConstants.TEST_ALTER_GENPROF_REQUEST_ERROR_TRAITS
            )
        self.assertEqual(
            exception.exception.results,
            TestGenprofConstants.TEST_ALTER_GENPROF_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Extract Genprof
    # ============================================================================
    def test_resource_admin_can_parse_extract_genprof_base_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            resource_admin.extract(
                TestGenprofConstants.TEST_EXTRACT_GENPROF_REQUEST_BASE_TRAITS
            ),
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_can_parse_extract_genprof_base_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            resource_admin.extract(
                TestGenprofConstants.TEST_EXTRACT_GENPROF_REQUEST_BASE_TRAITS
            )
        self.assertEqual(
            exception.exception.results,
            TestGenprofConstants.TEST_EXTRACT_GENPROF_RESULT_BASE_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Genprof
    # ============================================================================
    def test_resource_admin_can_parse_delete_genprof_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_DELETE_GENPROF_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            resource_admin.delete("TESTING", "ELIJTEST"),
            TestGenprofConstants.TEST_DELETE_GENPROF_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_can_parse_delete_genprof_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestGenprofConstants.TEST_DELETE_GENPROF_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            resource_admin.delete("TESTING", "ELIJTEST")
        self.assertEqual(
            exception.exception.results,
            TestGenprofConstants.TEST_DELETE_GENPROF_RESULT_ERROR_DICTIONARY,
        )
