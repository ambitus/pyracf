"""Test setropts getter functions."""

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
class TestSetroptsGetters(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    setropts_admin = SetroptsAdmin()

    # ============================================================================
    # Password Rules
    # ============================================================================
    def test_setropts_admin_get_password_rules(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.setropts_admin.get_password_rules(),
            TestSetroptsConstants.TEST_SETROPTS_PASSWORD_RULES,
        )

    # Error in misspelled SETROPTS parameter
    def test_setropts_admin_get_password_rules_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.setropts_admin.get_password_rules()

    # ============================================================================
    # Get attributes
    # ============================================================================
    def test_setropts_admin_get_class_attributes(
        self,
        call_racf_mock: Mock,
    ):
        setropts_extract_auditor = (
            TestSetroptsConstants.TEST_LIST_SETROPTS_RESULT_SUCCESS_XML
        )
        call_racf_mock.return_value = setropts_extract_auditor
        self.assertEqual(
            self.setropts_admin.get_class_attributes("FACILITY"),
            TestSetroptsConstants.TEST_SETROPTS_CLASS_ATTRIBUTES,
        )

    # Error in misspelled SETROPTS parameter
    def test_setropts_admin_get_class_attributes_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestSetroptsConstants.TEST_ALTER_SETROPTS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.setropts_admin.get_class_attributes("FACILITY")
