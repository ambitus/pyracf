"""Test access result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.access.test_access_constants as TestAccessConstants
from pyracf import AccessAdmin, SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestAccessResultParser(unittest.TestCase):
    maxDiff = None
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

    def test_access_admin_permit_can_check_for_necessary_refresh_xml(
        self,
        call_racf_mock: Mock,
    ):
        permit_access_xml_with_refresh = (
            TestAccessConstants.TEST_PERMIT_ACCESS_RESULT_SUCCESS_XML
        )
        permit_access_xml_with_refresh = permit_access_xml_with_refresh.replace(
            "</image>",
            "</image>\n<message>ICH06011I RACLISTED PROFILES FOR ELIJTEST "
            + "WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED</message>",
        )
        call_racf_mock.return_value = permit_access_xml_with_refresh
        self.assertEqual(
            self.access_admin.permit(
                "TESTING",
                "ELIJTEST",
                "ESWIFT",
                traits={"base:access": "NONE"},
                check_refresh=True,
            ),
            True,
        )

    def test_access_admin_permit_can_check_for_unnecessary_refresh_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_PERMIT_ACCESS_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.access_admin.permit(
                "TESTING",
                "ELIJTEST",
                "ESWIFT",
                traits={"base:access": "NONE"},
                check_refresh=True,
            ),
            False,
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

    def test_access_admin_delete_can_check_for_necessary_refresh_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestAccessConstants.TEST_DELETE_ACCESS_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.access_admin.delete(
                "TESTING", "ELIJTEST", "ESWIFT", check_refresh=True
            ),
            True,
        )

    def test_access_admin_delete_can_check_for_unnecessary_refresh_xml(
        self,
        call_racf_mock: Mock,
    ):
        delete_access_xml_no_refresh = (
            TestAccessConstants.TEST_DELETE_ACCESS_RESULT_SUCCESS_XML
        )
        delete_access_xml_no_refresh = delete_access_xml_no_refresh.replace(
            "ICH06011I", "NOMSG"
        )
        call_racf_mock.return_value = delete_access_xml_no_refresh
        self.assertEqual(
            self.access_admin.delete(
                "TESTING", "ELIJTEST", "ESWIFT", check_refresh=True
            ),
            False,
        )
