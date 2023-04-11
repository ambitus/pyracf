"""Test setropts getter functions."""

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
class TestSetroptsGetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(
        self, irrsmo00_init_mock: Mock, dump_request_xml_mock: Mock
    ) -> SetroptsAdmin:
        irrsmo00_init_mock.return_value = None
        dump_request_xml_mock.return_value = b""
        return SetroptsAdmin()

    # ============================================================================
    # SetroptsAdmin.get_password_rules()
    # ============================================================================
    def test_setropts_admin_get_password_rules(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_XML
        )
        self.assertTrue(
            setropts_admin.get_password_rules()
            == TestSetroptsConstants.TEST_SETROPTS_PASSWORD_RULES
        )

    # Error in misspelled SETROPTS parameter
    def test_setropts_admin_get_password_rules_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            setropts_admin.get_password_rules()

    # ============================================================================
    # SetroptsAdmin.get_class_types(class_name)
    # ============================================================================
    def test_setropts_admin_get_class_types(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        setropts_extract_auditor = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_XML
        )
        call_racf_mock.return_value = setropts_extract_auditor
        self.assertTrue(
            setropts_admin.get_class_types("FACILITY")
            == TestSetroptsConstants.TEST_SETROPTS_CLASS_ATTRIBUTES
        )

    # Error in misspelled SETROPTS parameter
    def test_setropts_admin_get_class_types_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        setropts_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_COMMAND_SETROPTS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            setropts_admin.get_class_types("FACILITY")
