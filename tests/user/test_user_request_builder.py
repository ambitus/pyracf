"""Test user request builder."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import UserAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestUserRequestBuilder(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> UserAdmin:
        irrsmo00_init_mock.return_value = None
        return UserAdmin(generate_requests_only=True)

    def test_user_admin_build_add_user_request(self, irrsmo00_init_mock: Mock):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.add(
            "squidwrd", traits=TestUserConstants.TEST_ADD_USER_REQUEST_TRAITS
        )
        print(result)
        print(TestUserConstants.TEST_ADD_USER_REQUEST_XML)
        self.assertEqual(result, TestUserConstants.TEST_ADD_USER_REQUEST_XML)

    def test_user_admin_build_alter_user_request(self, irrsmo00_init_mock: Mock):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.alter(
            "squidwrd", traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS
        )
        self.assertEqual(result, TestUserConstants.TEST_ALTER_USER_REQUEST_XML)

    def test_user_admin_build_extract_user_request_base_omvs(
        self, irrsmo00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.extract(
            "squidwrd", TestUserConstants.TEST_EXTRACT_USER_REQUEST_BASE_OMVS_TRAITS
        )
        self.assertEqual(
            result, TestUserConstants.TEST_EXTRACT_USER_REQUEST_BASE_OMVS_XML
        )

    def test_user_admin_build_delete_user_request(self, irrsmo00_init_mock: Mock):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.delete("squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_DELETE_USER_REQUEST_XML)
