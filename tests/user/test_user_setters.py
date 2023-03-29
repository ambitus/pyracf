"""Test user setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf.user.user_admin import UserAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestUserSetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> UserAdmin:
        irrsmo00_init_mock.return_value = None
        return UserAdmin()

    def test_user_admin_build_set_special_request(self, irrsmo00_init_mock: Mock):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.set_special("squidwrd", generate_request_only=True)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_SPECIAL_XML)

    def test_user_admin_build_del_special_request(self, irrsom00_init_mock: Mock):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.del_special("squidwrd", generate_request_only=True)
        self.assertEqual(result, TestUserConstants.TEST_USER_DEL_SPECIAL_XML)

    def test_user_admin_build_set_uid_request(self, init_mock_init_mock: Mock):
        user_admin = self.boilerplate(init_mock_init_mock)
        result = user_admin.set_uid("squidwrd", 40, generate_request_only=True)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_UID_XML)
