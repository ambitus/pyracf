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

    # ============================================================================
    # Class Authorizations
    # ============================================================================
    def test_user_admin_build_add_class_authorizations_single_class_request(
        self, irrsom00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.add_class_authorizations("squidwrd", "facility")
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_ADD_CLASS_AUTHORIZATIONS_SINGLE_CLASS_XML,
        )

    def test_user_admin_build_add_class_authorizations_multiple_classes_request(
        self, irrsom00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.add_class_authorizations(
            "squidwrd", ["facility", "terminal"]
        )
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_ADD_CLASS_AUTHORIZATIONS_MULTIPLE_CLASSES_XML,
        )

    def test_user_admin_build_remove_class_authorizations_single_class_request(
        self, irrsom00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.remove_class_authorizations("squidwrd", "facility")
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_REMOVE_CLASS_AUTHORIZATIONS_SINGLE_CLASS_XML,
        )

    def test_user_admin_build_remove_class_authorizations_multiple_classes_request(
        self, irrsom00_init_mock: Mock
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        result = user_admin.remove_class_authorizations(
            "squidwrd", ["facility", "terminal"]
        )
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_REMOVE_CLASS_AUTHORIZATIONS_MULTIPLE_CLASSES_XML,
        )

    @patch("pyracf.user.user_admin.UserAdmin.get_class_authorizations")
    def test_user_admin_build_delete_all_class_authorizations_request(
        self,
        get_class_authorizations_mock: Mock,
        irrsom00_init_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        get_class_authorizations_mock.return_value = [
            "facility",
            "terminal",
            "xfacilit",
        ]
        result = user_admin.delete_all_class_authorizations("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_DELETE_ALL_CLASS_AUTHORIZATIONS_XML
        )

    @patch("pyracf.user.user_admin.UserAdmin.get_class_authorizations")
    def test_user_admin_build_delete_all_class_authorizations_request_returns_false_if_none(
        self,
        get_class_authorizations_mock: Mock,
        irrsom00_init_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        get_class_authorizations_mock.return_value = []
        result = user_admin.delete_all_class_authorizations("squidwrd")
        self.assertFalse(result)

    @patch("pyracf.user.user_admin.UserAdmin.get_class_authorizations")
    def test_user_admin_build_set_class_authorizations_request(
        self,
        get_class_authorizations_mock: Mock,
        irrsom00_init_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        get_class_authorizations_mock.return_value = [
            "facility",
            "terminal",
            "xfacilit",
        ]
        result = user_admin.set_class_authorizations(
            "squidwrd", ["terminal", "xfacilit"]
        )
        self.assertEqual(
            result,
            (
                TestUserConstants.TEST_USER_DELETE_ALL_CLASS_AUTHORIZATIONS_XML
                + TestUserConstants.TEST_USER_SET_CLASS_AUTHORIZATIONS_XML
            ),
        )

    @patch("pyracf.user.user_admin.UserAdmin.get_class_authorizations")
    def test_user_admin_build_set_class_authorizations_no_existinsg_class_authorizations_request(
        self,
        get_class_authorizations_mock: Mock,
        irrsom00_init_mock: Mock,
    ):
        user_admin = self.boilerplate(irrsom00_init_mock)
        get_class_authorizations_mock.return_value = []
        result = user_admin.set_class_authorizations(
            "squidwrd", ["terminal", "xfacilit"]
        )
        print(result)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_CLASS_AUTHORIZATIONS_XML
        )

    # ============================================================================
    # OMVS UID
    # ============================================================================
    def test_user_admin_build_set_omvs_uid_request(self, init_mock_init_mock: Mock):
        user_admin = self.boilerplate(init_mock_init_mock)
        result = user_admin.set_omvs_uid("squidwrd", 40)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_UID_XML)

    # ============================================================================
    # OMVS Home
    # ============================================================================
    def test_user_admin_build_set_omvs_home_request(self, init_mock_init_mock: Mock):
        user_admin = self.boilerplate(init_mock_init_mock)
        result = user_admin.set_omvs_home("squidwrd", "/u/squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_HOME_XML)
