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
    # Special Authority
    # ============================================================================
    def test_user_admin_has_special_authority_returns_true_when_attribute_exists(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertTrue(user_admin.has_special_authority("squidwrd"))

    def test_user_admin_has_special_authority_returns_false_when_attribute_does_not_exist(
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
        self.assertFalse(user_admin.has_special_authority("squidwrd"))

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_has_special_authority_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.has_special_authority("squidwrd")

    # ============================================================================
    # Auditor Authority
    # ============================================================================
    def test_user_admin_has_auditor_authority_returns_true_when_attribute_exists(
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
        self.assertTrue(user_admin.has_auditor_authority("squidwrd"))

    def test_user_admin_has_auditor_authority_returns_false_when_attribute_does_not_exist(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        user_extract_no_auditor = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        call_racf_mock.return_value = user_extract_no_auditor
        self.assertFalse(user_admin.has_auditor_authority("squidwrd"))

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_has_auditory_authority_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.has_auditor_authority("squidwrd")

    # ============================================================================
    # Operations Authority
    # ============================================================================
    def test_user_admin_has_operations_authority_returns_true_when_attribute_exists(
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
        self.assertTrue(user_admin.has_operations_authority("squidwrd"))

    def test_user_admin_has_operations_authority_returns_false_when_attribute_does_not_exist(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertFalse(user_admin.has_operations_authority("squidwrd"))

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_has_operations_authority_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.has_operations_authority("squidwrd")

    # ============================================================================
    # Class Authorizations
    # ============================================================================
    def test_user_admin_get_class_authorizations_returns_the_class_authorizations_list(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_WITH_CLASS_AUTHORIZATIONS
        )
        self.assertEqual(
            user_admin.get_class_authorizations("squidwrd"),
            ["facility", "terminal", "xfacilit"],
        )

    def test_user_admin_get_class_authorizations_returns_empty_list_when_no_class_authorizations(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertEqual(user_admin.get_class_authorizations("squidwrd"), [])

    def test_user_admin_get_class_authorizations_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.get_class_authorizations("squidwrd")

    # ============================================================================
    # OMVS UID
    # ============================================================================
    def test_user_admin_get_omvs_uid_works(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(user_admin.get_omvs_uid("squidwrd"), 2424)

    def test_user_admin_get_omvs_uid_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.get_omvs_uid("squidwrd")

    def test_user_admin_get_omvs_uid_returns_none_when_no_omvs_segment_exists(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertIsNone(user_admin.get_omvs_uid("squidwrd"))

    # ============================================================================
    # OMVS Home
    # ============================================================================
    def test_user_admin_get_omvs_home_works(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(user_admin.get_omvs_home("squidwrd"), "/u/squidwrd")

    def test_user_admin_get_omvs_home_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.get_omvs_home("squidwrd")

    def test_user_admin_get_omvs_home_returns_none_when_no_omvs_segment_exists(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertIsNone(user_admin.get_omvs_home("squidwrd"))

    # ============================================================================
    # OMVS Program
    # ============================================================================
    def test_user_admin_get_omvs_program_works(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(user_admin.get_omvs_program("squidwrd"), "/bin/sh")

    def test_user_admin_get_omvs_program_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            user_admin.get_omvs_program("squidwrd")

    def test_user_admin_get_omvs_program_returns_none_when_no_omvs_segment_exists(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertIsNone(user_admin.get_omvs_program("squidwrd"))
