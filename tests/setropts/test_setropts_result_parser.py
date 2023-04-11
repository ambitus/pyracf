"""Test setropts result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.setropts.test_setropts_constants as TestSetroptsConstants
from pyracf.common.security_request_error import SecurityRequestError
from pyracf.setropts.setropts_admin import SetroptsAdmin

# Resolves F401
__init__


@patch("pyracf.common.security_request.SecurityRequest.dump_request_xml")
@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestSetroptsResultParser(unittest.TestCase):
    maxDiff = None

    def boilerplate(
        self, irrsmo00_init_mock: Mock, dump_request_xml_mock: Mock
    ) -> SetroptsAdmin:
        irrsmo00_init_mock.return_value = None
        dump_request_xml_mock.return_value = b""
        return SetroptsAdmin()

    # ============================================================================
    # Command Setropts
    # ============================================================================
    def test_setropts_admin_can_parse_command_setropts_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            setropts_admin.command(
                TestSetroptsConstants.TEST_COMMAND_SETROPTS_REQUEST_TRAITS
            ),
            TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in misspelled SETROPTS parameter
    def test_setropts_admin_can_parse_add_setropts_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            setropts_admin.command(
                {"raclist":"elixtest"}
            )
        self.assertEqual(
            exception.exception.results,
            TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # List Setropts
    # ============================================================================
    def test_setropts_admin_can_parse_list_setropts_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_XML
        )
        print(setropts_admin.list_ropts())
        self.assertEqual(
            setropts_admin.list_ropts(),
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in misspelled SETROPTS parameter
    def test_setropts_admin_can_parse_list_setropts_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            setropts_admin.list_ropts() # Not possible to misspell in this function, but it is the easiest error to test
        self.assertEqual(
            exception.exception.results,
            TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_ERROR_DICTIONARY,
        )
