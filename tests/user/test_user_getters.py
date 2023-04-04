"""Test user getter functions."""

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
class TestUserGetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(
        self, irrsmo00_init_mock: Mock, dump_request_xml_mock: Mock
    ) -> UserAdmin:
        irrsmo00_init_mock.return_value = None
        dump_request_xml_mock.return_value = b""
        return UserAdmin()

    # ============================================================================
    # UserAdmin.is_special()
    # ============================================================================
    def test_user_admin_is_special_returns_true_when_special(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertTrue(user_admin.is_special("squidwrd"))

    def test_user_admin_is_special_returns_false_when_not_special(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        user_extract_no_special = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        user_extract_no_special = user_extract_no_special.replace(
            "<message> ATTRIBUTES=SPECIAL</message>",
            "<message> ATTRIBUTES=NONE</message>",
        )
        call_racf_mock.return_value = user_extract_no_special
        self.assertFalse(user_admin.is_special("squidwrd"))

    def test_user_admin_is_special_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.is_special("squidwrd")

    # ============================================================================
    # UserAdmin.get_uid()
    # ============================================================================
    def test_user_admin_get_uid_works(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(user_admin.get_uid("squidwrd"), 2424)

    def test_user_admin_get_uid_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.get_uid("squidwrd"), 2424

    def test_user_admin_get_uid_returns_none_when_no_omvs_segment_exists(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
        dump_request_xml_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock, dump_request_xml_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertEqual(user_admin.get_uid("squidwrd"), None)
