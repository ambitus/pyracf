"""Test user getter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import UserAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestUserGetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> UserAdmin:
        irrsmo00_init_mock.return_value = None
        return UserAdmin()

    # ============================================================================
    # UserAdmin.is_special()
    # ============================================================================
    def test_user_admin_is_special_returns_true_when_special(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertTrue(user_admin.is_special("squidwrd"))

    def test_user_admin_is_special_returns_false_when_not_special(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        user_extract_no_special = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        user_extract_no_special = user_extract_no_special.replace(
            "<message> ATTRIBUTES=SPECIAL</message>",
            "<message> ATTRIBUTES=NONE</message>",
        )
        call_racf_mock.return_value = user_extract_no_special
        self.assertFalse(user_admin.is_special("squidwrd"))

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_is_special_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.is_special("squidwrd")

    # ============================================================================
    # UserAdmin.is_auditor()
    # ============================================================================
    def test_user_admin_is_auditor_returns_true_when_auditor(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        user_extract_auditor = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        user_extract_auditor = user_extract_auditor.replace(
            "<message> ATTRIBUTES=SPECIAL</message>",
            "<message> ATTRIBUTES=AUDITOR</message>",
        )
        call_racf_mock.return_value = user_extract_auditor
        self.assertTrue(user_admin.is_auditor("squidwrd"))

    def test_user_admin_is_auditor_returns_false_when_not_auditor(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        user_extract_no_auditor = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        call_racf_mock.return_value = user_extract_no_auditor
        self.assertFalse(user_admin.is_auditor("squidwrd"))

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_is_auditor_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.is_auditor("squidwrd")

    # ============================================================================
    # UserAdmin.is_operations()
    # ============================================================================
    def test_user_admin_is_operations_returns_true_when_operations(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        user_extract_operations = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        user_extract_operations = user_extract_operations.replace(
            "<message> ATTRIBUTES=SPECIAL</message>",
            "<message> ATTRIBUTES=OPERATIONS</message>",
        )
        call_racf_mock.return_value = user_extract_operations
        self.assertTrue(user_admin.is_operations("squidwrd"))

    def test_user_admin_is_operations_returns_false_when_not_operations(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertFalse(user_admin.is_operations("squidwrd"))

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_is_operations_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.is_operations("squidwrd")

    # ============================================================================
    # UserAdmin.get_uid()
    # ============================================================================
    def test_user_admin_get_uid_works(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(user_admin.get_uid("squidwrd"), 2424)

    def test_user_admin_get_uid_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.get_uid("squidwrd"), 2424

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_get_uid_returns_none_when_no_omvs_segment_exists(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertIsNone(user_admin.get_uid("squidwrd"))