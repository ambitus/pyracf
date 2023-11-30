"""Test setropts result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.setropts.test_setropts_constants as TestSetroptsConstants
from pyracf import SecurityResponseError
from pyracf.common.irrsmo00 import IRRSMO00
from pyracf.setropts.setropts_admin import SetroptsAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestSetroptsResultParser(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    setropts_admin = SetroptsAdmin()

    # ============================================================================
    # Alter Setropts
    # ============================================================================
    def test_setropts_admin_can_parse_alter_setropts_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.setropts_admin.alter(options={"base:raclist": "elijtest"}),
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in misspelled SETROPTS parameter
    def test_setropts_admin_can_parse_add_setropts_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError) as exception:
            self.setropts_admin.alter(options={"base:raclist": "elixtest"})
        self.assertEqual(
            exception.exception.result,
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # List Setropts
    # ============================================================================
    def test_setropts_admin_can_parse_list_setropts_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.setropts_admin.list_racf_options(),
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_DICTIONARY,
        )

    def test_setropts_admin_can_parse_list_setropts_success_2_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_2_XML
        )
        self.assertEqual(
            self.setropts_admin.list_racf_options(),
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_2_DICTIONARY,
        )

    def test_setropts_admin_can_parse_list_setropts_success_3_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_3_XML
        )
        self.assertEqual(
            self.setropts_admin.list_racf_options(),
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_3_DICTIONARY,
        )

    # Error in misspelled SETROPTS parameter
    def test_setropts_admin_can_parse_list_setropts_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError) as exception:
            # Not valid error for this request, but good test
            self.setropts_admin.list_racf_options()
        self.assertEqual(
            exception.exception.result,
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_ERROR_DICTIONARY,
        )
