"""Test user request builder."""

import unittest
from unittest.mock import Mock

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import InvalidSegmentNameError, InvalidSegmentTraitError, UserAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestUserRequestBuilder(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
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

    def test_user_admin_build_alter_user_request(self):
        result = self.user_admin.alter(
            "squidwrd", traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS
        )
        self.assertEqual(result, TestUserConstants.TEST_ALTER_USER_REQUEST_XML)

    def test_user_admin_build_extract_user_request_base_omvs(self):
        result = self.user_admin.extract(
            "squidwrd", segments={"omvs": True, "mfa": False}
        )
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
    # Customize Segment Traits
    # ============================================================================
    def test_user_admin_build_alter_request_replace_existing_segment_traits(self):
        user_admin = UserAdmin(
            generate_requests_only=True,
            replace_existing_segment_traits=TestUserConstants.TEST_USER_REPLACE_SEGMENT_TRAITS,
        )
        result = user_admin.alter(
            "squidwrd", traits=TestUserConstants.TEST_ALTER_USER_CSDATA_REQUEST_TRAITS
        )
        self.assertEqual(
            result, TestUserConstants.TEST_ALTER_USER_REQUEST_REPLACE_SEGMENTS_XML
        )

    def test_user_admin_build_alter_request_update_existing_segment_traits(self):
        user_admin = UserAdmin(
            generate_requests_only=True,
            update_existing_segment_traits=TestUserConstants.TEST_USER_ADDITIONAL_SEGMENT_TRAITS,
        )
        result = user_admin.alter(
            "squidwrd",
            traits=TestUserConstants.TEST_ALTER_USER_CSDATA_AND_OMVS_REQUEST_TRAITS,
        )
        self.assertEqual(
            result,
            TestUserConstants.TEST_ALTER_USER_REQUEST_UPDATE_SEGMENTS_XML,
        )

    # ============================================================================
    # Request Builder Errors
    # ============================================================================
    def test_user_admin_build_add_request_with_invalid_segment_traits(self):
        invalid_trait = "omvs:invalid_trait"
        user_admin = UserAdmin(
            generate_requests_only=True,
        )
        with self.assertRaises(InvalidSegmentTraitError) as exception:
            user_admin.add(
                "squidwrd", TestUserConstants.TEST_ADD_USER_REQUEST_INVALID_TRAITS
            )
        self.assertEqual(
            exception.exception.message,
            "Building of Security Request failed.\n\n"
            + "Could not find "
            + f"'{invalid_trait}' in valid segment traits for the requested operation.\n",
        )

    def test_user_admin_build_extract_request_with_invalid_segment_name(self):
        invalid_segment = "test_segment"
        user_admin = UserAdmin(
            generate_requests_only=True,
        )
        with self.assertRaises(InvalidSegmentNameError) as exception:
            user_admin.extract("squidwrd", {invalid_segment: True})
        self.assertEqual(
            exception.exception.message,
            "Building of Security Request failed.\n\n"
            + "Could not find "
            + f"'{invalid_segment}' in valid segments for the requested operation.\n",
        )
