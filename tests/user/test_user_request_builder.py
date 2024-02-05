"""Test user request builder."""

import unittest

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import SegmentError, SegmentTraitError, UserAdmin

# Resolves F401
__init__


class TestUserRequestBuilder(unittest.TestCase):
    maxDiff = None
    user_admin = UserAdmin(generate_requests_only=True)
    test_password = "GIyTTqdF"
    test_passphrase = "PassPhrasesAreCool!"

    # ============================================================================
    # Default Fields
    # ============================================================================
    def test_user_admin_build_add_user_request(self):
        result = self.user_admin.add(
            "squidwrd", traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS
        )
        self.assertEqual(result, TestUserConstants.TEST_ADD_USER_REQUEST_XML)

    def test_user_admin_build_add_user_base_omvs_tso_revoke_resume_request(self):
        result = self.user_admin.add(
            "squidwrd",
            traits=TestUserConstants.TEST_ADD_USER_BASE_OMVS_TSO_REVOKE_RESUME_REQUEST_TRAITS,
        )
        self.assertEqual(
            result,
            TestUserConstants.TEST_ADD_USER_BASE_OMVS_TSO_REVOKE_RESUME_REQUEST_XML,
        )

    def test_user_admin_build_alter_user_request(self):
        result = self.user_admin.alter(
            "squidwrd", traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS
        )
        self.assertEqual(result, TestUserConstants.TEST_ALTER_USER_REQUEST_XML)

    def test_user_admin_build_extract_user_request_base_omvs(self):
        result = self.user_admin.extract("squidwrd", segments=["omvs"])
        self.assertEqual(
            result, TestUserConstants.TEST_EXTRACT_USER_REQUEST_BASE_OMVS_XML
        )

    def test_user_admin_build_delete_user_request(self):
        result = self.user_admin.delete("squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_DELETE_USER_REQUEST_XML)

    # ============================================================================
    # Password and Password Phrase Redaction
    # ============================================================================
    def test_user_admin_build_add_user_request_password_redacted(
        self,
    ):
        result = self.user_admin.add(
            "squidwrd",
            traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_PASSWORD,
        )
        self.assertEqual(result, TestUserConstants.TEST_ADD_USER_REQUEST_PASSWORD_XML)
        self.assertNotIn(self.test_password, result.decode("utf-8"))

    def test_user_admin_build_add_user_request_passphrase_redacted(
        self,
    ):
        result = self.user_admin.add(
            "squidwrd",
            traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_PASSPHRASE,
        )
        self.assertEqual(result, TestUserConstants.TEST_ADD_USER_REQUEST_PASSPHRASE_XML)
        self.assertNotIn(self.test_passphrase, result.decode("utf-8"))

    def test_user_admin_build_add_user_request_passphrase_and_password_redacted(
        self,
    ):
        result = self.user_admin.add(
            "squidwrd",
            traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_PASSPHRASE_AND_PASSWORD,
        )
        self.assertEqual(
            result, TestUserConstants.TEST_ADD_USER_REQUEST_PASSPHRASE_AND_PASSWORD_XML
        )
        self.assertNotIn(self.test_password, result.decode("utf-8"))
        self.assertNotIn(self.test_passphrase, result.decode("utf-8"))

    # ============================================================================
    # Request Builder Errors
    # ============================================================================
    def test_user_admin_build_add_request_with_bad_segment_traits(self):
        bad_trait = "omvs:bad_trait"
        user_admin = UserAdmin(
            generate_requests_only=True,
        )
        with self.assertRaises(SegmentTraitError) as exception:
            user_admin.add(
                "squidwrd", TestUserConstants.TEST_ADD_USER_REQUEST_BAD_TRAITS
            )
        self.assertEqual(
            exception.exception.message,
            "Unable to build Security Request.\n\n"
            + f"'{bad_trait}' is not a known segment-trait "
            + f"combination for '{self.user_admin._profile_type}'.\n",
        )

    # Since this test uses generate_requests_only, the "Add" after the AddOperationError is
    # returned does not begin with an "Extract" call. This is necessary to recreate the error,
    # so an extra extract call was added to simulate this behavior.
    def test_user_admin_cleans_up_after_build_add_request_with_bad_segment_traits(self):
        bad_trait = "omvs:bad_trait"
        user_admin = UserAdmin(
            generate_requests_only=True,
        )
        with self.assertRaises(SegmentTraitError) as exception:
            user_admin.add(
                "squidwrd", TestUserConstants.TEST_ADD_USER_REQUEST_BAD_TRAITS
            )
        self.assertEqual(
            exception.exception.message,
            "Unable to build Security Request.\n\n"
            + f"'{bad_trait}' is not a known segment-trait "
            + f"combination for '{self.user_admin._profile_type}'.\n",
        )
        result = user_admin.extract("squidwrd", segments=["omvs"])
        self.assertEqual(
            result, TestUserConstants.TEST_EXTRACT_USER_REQUEST_BASE_OMVS_XML
        )
        result = self.user_admin.add(
            "squidwrd", traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS
        )
        self.assertEqual(result, TestUserConstants.TEST_ADD_USER_REQUEST_XML)

    def test_user_admin_build_extract_request_with_bad_segment_name(self):
        bad_segment = "bad_segment"
        user_admin = UserAdmin(
            generate_requests_only=True,
        )
        with self.assertRaises(SegmentError) as exception:
            user_admin.extract("squidwrd", segments=[bad_segment])
        self.assertEqual(
            exception.exception.message,
            "Unable to build Security Request.\n\n"
            + f"'{bad_segment}' is not a known segment for '{self.user_admin._profile_type}'.\n",
        )

    def test_user_admin_cleans_up_after_build_extract_request_with_bad_segment_name(
        self,
    ):
        bad_segment = "bad_segment"
        user_admin = UserAdmin(
            generate_requests_only=True,
        )
        with self.assertRaises(SegmentError) as exception:
            user_admin.extract("squidwrd", segments=["tso", bad_segment])
        self.assertEqual(
            exception.exception.message,
            "Unable to build Security Request.\n\n"
            + f"'{bad_segment}' is not a known segment for '{self.user_admin._profile_type}'.\n",
        )
        result = user_admin.extract("squidwrd", segments=["omvs"])
        self.assertEqual(
            result, TestUserConstants.TEST_EXTRACT_USER_REQUEST_BASE_OMVS_XML
        )
