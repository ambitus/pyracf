"""Test user setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import UserAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestUserCSdata(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> UserAdmin:
        irrsmo00_init_mock.return_value = None
        return UserAdmin()

    def test_user_admin_build_alter_request_alternate_segments(
        self, irrsmo00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        user_admin.overwrite_field_data(TestUserConstants.TEST_USER_ALTERNATE_SEGMENTS)
        result = user_admin.alter(
            TestUserConstants.TEST_ALTER_USER_CSDATA_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(
            result, TestUserConstants.TEST_ALTER_USER_ALTERNATE_SEGMENTS_REQUEST_XML
        )

    def test_user_admin_build_alter_request_overwrite_segments(
        self, irrsmo00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        user_admin.overwrite_field_data(TestUserConstants.TEST_USER_OVERWRITE_SEGMENTS)
        result = user_admin.alter(
            TestUserConstants.TEST_ALTER_USER_CSDATA_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(
            result, TestUserConstants.TEST_ALTER_USER_OVERWRITE_SEGMENTS_REQUEST_XML
        )

    def test_user_admin_build_alter_request_update_segments(
        self, irrsmo00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        user_admin.add_field_data(TestUserConstants.TEST_USER_UPDATE_SEGMENTS)
        result = user_admin.alter(
            TestUserConstants.TEST_ALTER_USER_CSDATA_REQUEST_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(
            result, TestUserConstants.TEST_ALTER_USER_UPDATE_SEGMENTS_REQUEST_XML
        )
