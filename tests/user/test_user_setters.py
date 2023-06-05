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

    def test_user_admin_build_set_special_request(self, irrsmo00_init_mock: Mock):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.set_special(
            "squidwrd",
        )
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_SPECIAL_XML)

    def test_user_admin_build_delete_special_request(self, irrsom00_init_mock: Mock):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.delete_special("squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_USER_DELELETE_SPECIAL_XML)

    def test_user_admin_build_set_auditor_request(self, irrsmo00_init_mock: Mock):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.set_auditor("squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_AUDITOR_XML)

    def test_user_admin_build_delete_auditor_request(self, irrsom00_init_mock: Mock):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.delete_auditor("squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_USER_DELETE_AUDITOR_XML)

    def test_user_admin_build_set_operations_request(self, irrsmo00_init_mock: Mock):
        user_admin = self.boilerplate(irrsmo00_init_mock)
        result = user_admin.set_operations("squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OPERATOR_XML)

    def test_user_admin_build_delete_operations_request(self, irrsom00_init_mock: Mock):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.delete_operations("squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_USER_DELETE_OPERATOR_XML)

    def test_user_admin_build_set_omvs_uid_request(self, init_mock_init_mock: Mock):
        user_admin = self.boilerplate(init_mock_init_mock)
        result = user_admin.set_omvs_uid("squidwrd", 40)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_UID_XML)
