"""Test customizing security admin segment traits."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.common.test_common_constants as TestCommonConstants
import tests.data_set.test_data_set_constants as TestDataSetConstants
import tests.group.test_group_constants as TestGroupConstants
import tests.resource.test_resource_constants as TestResourceConstants
import tests.user.test_user_constants as TestUserConstants
from pyracf import (
    DataSetAdmin,
    GroupAdmin,
    ResourceAdmin,
    SecurityRequestError,
    UserAdmin,
)

# Resolves F401
__init__


class TestAdditionalSecretsRedaction(unittest.TestCase):
    maxDiff = None

    # ============================================================================
    # User Administration
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_user_admin_custom_secret_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(additional_secret_traits=["omvs:uid"])
        call_racf_mock.side_effect = [
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestUserConstants.TEST_ALTER_USER_RESULT_EXTENDED_SUCCESS_XML,
        ]
        result = user_admin.alter(
            "squidwrd",
            traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED,
        )
        self.assertEqual(
            result,
            TestCommonConstants.TEST_ALTER_USER_RESULT_SUCCESS_UID_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED["omvs:uid"],
            result,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_user_admin_custom_secret_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(additional_secret_traits=["omvs:uid"])
        call_racf_mock.side_effect = [
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestUserConstants.TEST_ALTER_USER_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            user_admin.alter(
                "squidwrd",
                traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_UID_ERROR,
            )
        self.assertEqual(
            exception.exception.result,
            TestCommonConstants.TEST_ALTER_USER_RESULT_ERROR_UID_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_UID_ERROR["omvs:uid"],
            exception.exception.result,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_user_admin_custom_secret_redacted_when_complex_characters(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(additional_secret_traits=["base:installation_data"])
        call_racf_mock.side_effect = [
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML,
            TestCommonConstants.TEST_ALTER_USER_RESULT_INST_DATA_SUCCESS_XML,
        ]
        result = user_admin.alter(
            "squidwrd",
            traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_INST_DATA,
        )
        self.assertEqual(
            result,
            TestCommonConstants.TEST_ALTER_USER_RESULT_SUCCESS_INST_DATA_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_INST_DATA[
                "base:installation_data"
            ],
            result,
        )

    def test_user_admin_custom_secret_redacted_request(self):
        user_admin = UserAdmin(
            additional_secret_traits=["omvs:uid"], generate_requests_only=True
        )
        result = user_admin.alter(
            "squidwrd",
            traits=TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED,
        )
        self.assertNotIn(
            bytes(
                TestUserConstants.TEST_ALTER_USER_REQUEST_TRAITS_EXTENDED["omvs:uid"],
                "utf-8",
            ),
            result,
        )

    # ============================================================================
    # Group Administration
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_group_admin_custom_secret_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        group_admin = GroupAdmin(additional_secret_traits=["omvs:gid"])
        call_racf_mock.side_effect = [
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML,
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_SUCCESS_XML,
        ]
        result = group_admin.alter(
            "testgrp0",
            traits=TestGroupConstants.TEST_ALTER_GROUP_REQUEST_TRAITS,
        )
        self.assertEqual(
            result,
            TestCommonConstants.TEST_ALTER_GROUP_RESULT_SUCCESS_GID_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            TestGroupConstants.TEST_ALTER_GROUP_REQUEST_TRAITS["omvs:gid"],
            result,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_group_admin_custom_secret_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        group_admin = GroupAdmin(additional_secret_traits=["omvs:gid"])
        call_racf_mock.side_effect = [
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML,
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            group_admin.alter(
                "testgrp0",
                traits=TestGroupConstants.TEST_ALTER_GROUP_REQUEST_ERROR_TRAITS,
            )
        self.assertEqual(
            exception.exception.result,
            TestCommonConstants.TEST_ALTER_GROUP_RESULT_ERROR_GID_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            TestGroupConstants.TEST_ALTER_GROUP_REQUEST_ERROR_TRAITS["omvs:gid"],
            exception.exception.result,
        )

    def test_group_admin_custom_secret_redacted_request(self):
        group_admin = GroupAdmin(
            additional_secret_traits=["omvs:gid"], generate_requests_only=True
        )
        result = group_admin.alter(
            "squidwrd",
            traits=TestGroupConstants.TEST_ALTER_GROUP_REQUEST_TRAITS,
        )
        self.assertNotIn(
            bytes(
                TestGroupConstants.TEST_ALTER_GROUP_REQUEST_TRAITS["omvs:gid"], "utf-8"
            ),
            result,
        )

    # ============================================================================
    # General Resource Profile Administration
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_custom_secret_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        resource_admin = ResourceAdmin(additional_secret_traits=["base:owner"])
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_SUCCESS_XML,
        ]
        result = resource_admin.alter(
            "TESTING",
            "ELIJTEST",
            traits=TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_TRAITS,
        )
        self.assertEqual(
            result,
            TestCommonConstants.TEST_ALTER_RESOURCE_RESULT_SUCCESS_OWNER_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_TRAITS["base:owner"],
            result,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_custom_mapped_secret_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        resource_admin = ResourceAdmin(additional_secret_traits=["base:audit_update"])
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestCommonConstants.TEST_ALTER_RESOURCE_OVERWRITE_AUDIT_RESULT_SUCCESS_XML,
        ]
        result = resource_admin.overwrite_audit_rules_by_access_level(
            "TESTING",
            "ELIJTEST",
            update="ALL",
        )
        self.assertEqual(
            result,
            TestCommonConstants.TEST_ALTER_RESOURCE_RESULT_SUCCESS_AUDIT_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            "ALL",
            result,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_resource_admin_custom_secret_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        secret_trait = "base:universal_access"
        resource_admin = ResourceAdmin(additional_secret_traits=[secret_trait])
        call_racf_mock.side_effect = [
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML,
            TestResourceConstants.TEST_ALTER_RESOURCE_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            resource_admin.alter(
                "TESTING",
                "ELIJTEST",
                traits=TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_ERROR_TRAITS,
            )
        self.assertEqual(
            exception.exception.result,
            TestCommonConstants.TEST_ALTER_RESOURCE_RESULT_ERROR_UACC_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_ERROR_TRAITS[
                f"{secret_trait}"
            ],
            exception.exception.result,
        )

    def test_resource_admin_custom_secret_redacted_request(self):
        resource_admin = ResourceAdmin(
            additional_secret_traits=["base:owner"], generate_requests_only=True
        )
        result = resource_admin.alter(
            "TESTING",
            "ELIJTEST",
            traits=TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_TRAITS,
        )
        self.assertNotIn(
            bytes(
                TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_TRAITS["base:owner"],
                "utf-8",
            ),
            result,
        )

    # ============================================================================
    # Data Set Profile Administration
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_custom_secret_redacted_on_success(
        self,
        call_racf_mock: Mock,
    ):
        data_set_admin = DataSetAdmin(additional_secret_traits=["base:owner"])
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_SUCCESS_XML,
        ]
        result = data_set_admin.alter(
            "ESWIFT.TEST.T1136242.P3020470",
            traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
        )
        self.assertEqual(
            result,
            TestCommonConstants.TEST_ALTER_DATA_SET_RESULT_SUCCESS_OWNER_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS["base:owner"],
            result,
        )

    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_data_set_admin_custom_secret_redacted_on_error(
        self,
        call_racf_mock: Mock,
    ):
        secret_trait = "base:universal_access"
        data_set_admin = DataSetAdmin(additional_secret_traits=[secret_trait])
        call_racf_mock.side_effect = [
            TestDataSetConstants.TEST_EXTRACT_DATA_SET_RESULT_BASE_ONLY_SUCCESS_XML,
            TestDataSetConstants.TEST_ALTER_DATA_SET_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            data_set_admin.alter(
                "ESWIFT.TEST.T1136242.P3020470",
                traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
            )
        self.assertEqual(
            exception.exception.result,
            TestCommonConstants.TEST_ALTER_DATA_SET_RESULT_ERROR_UACC_SECRET_DICTIONARY,
        )
        self.assertNotIn(
            TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS[f"{secret_trait}"],
            exception.exception.result,
        )

    def test_data_set_admin_custom_secret_redacted_request(self):
        data_set_admin = DataSetAdmin(
            additional_secret_traits=["base:owner"], generate_requests_only=True
        )
        result = data_set_admin.alter(
            "ESWIFT.TEST.T1136242.P3020470",
            traits=TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS,
        )
        self.assertNotIn(
            bytes(
                TestDataSetConstants.TEST_ALTER_DATA_SET_REQUEST_TRAITS["base:owner"],
                "utf-8",
            ),
            result,
        )
