"""Test user request builder."""

import unittest
from unittest.mock import Mock

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import UserAdmin
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
            traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSWORD,
        )
        self.assertEqual(result, TestUserConstants.TEST_ADD_USER_REQUEST_PASSWORD_XML)
        self.assertNotIn(self.test_password, result.decode("utf-8"))

    def test_user_admin_build_add_user_request_passphrase_redacted(
        self,
    ):
        result = self.user_admin.add(
            "squidwrd",
            traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSPHRASE,
        )
        self.assertEqual(result, TestUserConstants.TEST_ADD_USER_REQUEST_PASSPHRASE_XML)
        self.assertNotIn(self.test_password, result.decode("utf-8"))

    def test_user_admin_build_add_user_request_passphrase_and_password_redacted(
        self,
    ):
        result = self.user_admin.add(
            "squidwrd",
            traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS_PASSPHRASE_AND_PASSWORD,
        )
        self.assertEqual(
            result, TestUserConstants.TEST_ADD_USER_REQUEST_PASSPHRASE_AND_PASSWORD_XML
        )
        self.assertNotIn(self.test_password, result.decode("utf-8"))

    # ============================================================================
    # Custom Field Data
    # ============================================================================
    def test_user_admin_build_alter_request_alternate_segments(self):
        user_admin = UserAdmin(
            generate_requests_only=True,
            overwrite_field_data=TestUserConstants.TEST_USER_ALTERNATE_SEGMENTS,
        )
        result = user_admin.alter(
            "squidwrd", traits=TestUserConstants.TEST_ALTER_USER_CSDATA_REQUEST_TRAITS
        )
        self.assertEqual(
            result, TestUserConstants.TEST_ALTER_USER_REQUEST_ALTERNATIVE_SEGMENTS_XML
        )

    def test_user_admin_build_alter_request_overwrite_segments(self):
        user_admin = UserAdmin(
            generate_requests_only=True,
            overwrite_field_data=TestUserConstants.TEST_USER_OVERWRITE_SEGMENTS,
        )
        result = user_admin.alter(
            "squidwrd", traits=TestUserConstants.TEST_ALTER_USER_CSDATA_REQUEST_TRAITS
        )
        self.assertEqual(
            result, TestUserConstants.TEST_ALTER_USER_REQUEST_OVERWRITE_SEGMENTS_XML
        )

    def test_user_admin_build_alter_request_update_segments(self):
        user_admin = UserAdmin(
            generate_requests_only=True,
            add_field_data=TestUserConstants.TEST_USER_UPDATE_SEGMENTS,
        )
        result = user_admin.alter(
            "squidwrd", traits=TestUserConstants.TEST_ALTER_USER_CSDATA_REQUEST_TRAITS
        )
        self.assertEqual(
            result, TestUserConstants.TEST_ALTER_USER_REQUEST_UPDATE_SEGMENTS_XML
        )
