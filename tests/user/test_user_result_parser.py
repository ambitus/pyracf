"""Test user result parser."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf.common.security_request_error import SecurityRequestError
from pyracf.user.user_admin import UserAdmin

# Resolves F401
__init__


@patch("pyracf.common.security_request.SecurityRequest.dump_request_xml")
@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestUserResultParser(unittest.TestCase):
    maxDiff = None

    def boilerplate(
        self, irrsmo00_init_mock: Mock, dump_request_xml_mock: Mock
    ) -> UserAdmin:
        irrsmo00_init_mock.return_value = None
        dump_request_xml_mock.return_value = b""
        return UserAdmin()

    # ============================================================================
    # Add User
    # ============================================================================
    def test_user_admin_can_parse_add_user_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_SUCCESS_XML
        self.assertEqual(
            user_admin.add(TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS),
            TestUserConstants.TEST_ADD_USER_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, SQUIDWRD already added/exists
    def test_user_admin_can_parse_add_user_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = TestUserConstants.TEST_ADD_USER_RESULT_ERROR_XML
        with self.assertRaises(SecurityRequestError) as exception:
            user_admin.add(TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS)
        self.assertEqual(
            exception.exception.results,
            TestUserConstants.TEST_ADD_USER_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter User
    # ============================================================================
    def test_user_admin_can_parse_alter_user_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_ALTER_USER_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            user_admin.alter(TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS),
            TestUserConstants.TEST_ALTER_USER_RESULT_SUCCESS_DICTIONARY,
        )

    # Error: invalid parameter "name"
    def test_user_admin_can_parse_alter_user_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = TestUserConstants.TEST_ALTER_USER_RESULT_ERROR_XML
        with self.assertRaises(SecurityRequestError) as exception:
            user_admin.alter(
                user_admin.alter(TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS)
            )
        self.assertEqual(
            exception.exception.results,
            TestUserConstants.TEST_ALTER_USER_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Extract User
    # ============================================================================
    def test_user_admin_can_parse_extract_user_base_omvs_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(
            user_admin.extract({"userid": "squidward"}),
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_DICTIONARY,
        )

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_can_parse_extract_user_base_omvs_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            user_admin.extract({"userid": "squidward"})
        self.assertEqual(
            exception.exception.results,
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete User
    # ============================================================================
    def test_user_admin_can_parse_delete_user_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_DELETE_USER_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            user_admin.delete("squidwrd"),
            TestUserConstants.TEST_DELETE_USER_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_can_parse_delete_user_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_DELETE_USER_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            user_admin.delete("squidwrd")
        self.assertEqual(
            exception.exception.results,
            TestUserConstants.TEST_DELETE_USER_RESULT_ERROR_DICTIONARY,
        )
