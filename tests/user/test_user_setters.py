"""Test user setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import UserAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestUserSetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> UserAdmin:
        irrsmo00_init_mock.return_value = None
        return UserAdmin(generate_requests_only=True)

    # ============================================================================
    # Special Authority
    # ============================================================================
    def test_user_admin_build_give_special_authority_request(
        self, irrsmo00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.give_special_authority(
            "squidwrd",
        )
        self.assertEqual(result, TestUserConstants.TEST_USER_GIVE_SPECIAL_AUTHORITY_XML)

    def test_user_admin_build_remove_special_authority_request(
        self, irrsom00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.take_away_special_authority("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_REMOVE_SPECIAL_AUTHORITY_XML
        )

    # ============================================================================
    # Auditor Authority
    # ============================================================================
    def test_user_admin_build_give_auditor_authority_request(
        self, irrsmo00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.give_auditor_authority("squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_USER_GIVE_AUDITOR_AUTHORITY_XML)

    def test_user_admin_build_remove_auditor_authority_request(
        self, irrsom00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.remove_auditor_authority("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_REMOVE_AUDITOR_AUTHORITY_XML
        )

    # ============================================================================
    # Operations Authority
    # ============================================================================
    def test_user_admin_build_give_operations_authority_request(
        self, irrsmo00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.give_operations_authority("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_GIVE_OPERATIONS_AUTHORITY_XML
        )

    def test_user_admin_build_remove_operations_authority_request(
        self, irrsom00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.remove_operations_authority("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_REMOVE_OPERATIONS_AUTHORITY_XML
        )

    # ============================================================================
    # Password
    # ============================================================================
    def test_user_admin_build_set_password_request(self, irrsom00_init_mock: Mock):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.set_password("squidwrd", "GIyTTqdF")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_PASSWORD_XML)

    def test_user_admin_build_set_omvs_uid_request(self, init_mock_init_mock: Mock):
        user_admin = self.boilerplate(init_mock_init_mock)
        result = user_admin.set_omvs_uid("squidwrd", 40)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_UID_XML)
