"""Test access result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.access.test_access_constants as TestAccessConstants
from pyracf import AccessAdmin, SecurityRequestError
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestAccessResultParser(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    access_admin = AccessAdmin()

    # ============================================================================
    # Permit Access
    # ============================================================================
    def test_access_admin_can_parse_permit_access_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_PERMIT_ACCESS_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.access_admin.permit(
                "TESTING", "ELIJTEST", "ESWIFT", traits={"base:access": "NONE"}
            ),
            TestAccessConstants.TEST_PERMIT_ACCESS_RESULT_SUCCESS_DICTIONARY,
        )

    # Error, UserId MCGINLEY not defined to RACF
    def test_access_admin_can_parse_permit_access_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_PERMIT_ACCESS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.access_admin.permit(
                "TESTING", "ELIJTEST", "MCGINLEY", traits={"base:access": "ALTER"}
            )
        self.assertEqual(
            exception.exception.result,
            TestAccessConstants.TEST_PERMIT_ACCESS_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Access
    # ============================================================================
    def test_access_admin_can_parse_delete_access_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_DELETE_ACCESS_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.access_admin.delete("TESTING", "ELIJTEST", "ESWIFT"),
            TestAccessConstants.TEST_DELETE_ACCESS_RESULT_SUCCESS_DICTIONARY,
        )

    # Error User not authorized, delete ignored
    def test_access_admin_can_parse_delete_access_error_xml(self, call_racf_mock: Mock):
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_DELETE_ACCESS_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.access_admin.delete("TESTING", "ELIJTEST", "ESWIFT")
        self.assertEqual(
            exception.exception.result,
            TestAccessConstants.TEST_DELETE_ACCESS_RESULT_ERROR_DICTIONARY,
        )
