"""Test user getter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import SecurityRequestError, UserAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestUserGetters(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    user_admin = UserAdmin()

    # ============================================================================
    # Special Authority
    # ============================================================================
    def test_user_admin_has_special_authority_returns_true_when_attribute_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertTrue(self.user_admin.has_special_authority("squidwrd"))

    def test_user_admin_has_special_authority_returns_false_when_attribute_does_not_exist(
        self,
        call_racf_mock: Mock,
    ):
        user_extract_no_special = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        user_extract_no_special = user_extract_no_special.replace(
            "<message> ATTRIBUTES=SPECIAL</message>",
            "<message> ATTRIBUTES=NONE</message>",
        )
        call_racf_mock.return_value = user_extract_no_special
        self.assertFalse(self.user_admin.has_special_authority("squidwrd"))

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_has_special_authority_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.has_special_authority("squidwrd")

    # ============================================================================
    # Auditor Authority
    # ============================================================================
    def test_user_admin_has_auditor_authority_returns_true_when_attribute_exists(
        self,
        call_racf_mock: Mock,
    ):
        user_extract_auditor = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        user_extract_auditor = user_extract_auditor.replace(
            "<message> ATTRIBUTES=SPECIAL</message>",
            "<message> ATTRIBUTES=AUDITOR</message>",
        )
        call_racf_mock.return_value = user_extract_auditor
        self.assertTrue(self.user_admin.has_auditor_authority("squidwrd"))

    def test_user_admin_has_auditor_authority_returns_false_when_attribute_does_not_exist(
        self,
        call_racf_mock: Mock,
    ):
        user_extract_no_auditor = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        call_racf_mock.return_value = user_extract_no_auditor
        self.assertFalse(self.user_admin.has_auditor_authority("squidwrd"))

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_has_auditory_authority_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.has_auditor_authority("squidwrd")

    # ============================================================================
    # Operations Authority
    # ============================================================================
    def test_user_admin_has_operations_authority_returns_true_when_attribute_exists(
        self,
        call_racf_mock: Mock,
    ):
        user_extract_operations = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        user_extract_operations = user_extract_operations.replace(
            "<message> ATTRIBUTES=SPECIAL</message>",
            "<message> ATTRIBUTES=OPERATIONS</message>",
        )
        call_racf_mock.return_value = user_extract_operations
        self.assertTrue(self.user_admin.has_operations_authority("squidwrd"))

    def test_user_admin_has_operations_authority_returns_false_when_attribute_does_not_exist(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertFalse(self.user_admin.has_operations_authority("squidwrd"))

    # Error in environment, SQUIDWRD already deleted/not added
    def test_user_admin_has_operations_authority_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.has_operations_authority("squidwrd")

    # ============================================================================
    # Class Authorizations
    # ============================================================================
    def test_user_admin_get_class_authorizations_returns_the_class_authorizations_list(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_WITH_CLASS_AUTHORIZATIONS
        )
        self.assertEqual(
            self.user_admin.get_class_authorizations("squidwrd"),
            ["facility", "terminal", "xfacilit"],
        )

    def test_user_admin_get_class_authorizations_returns_empty_list_when_no_class_authorizations(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertEqual(self.user_admin.get_class_authorizations("squidwrd"), [])

    def test_user_admin_get_class_authorizations_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_class_authorizations("squidwrd")

    # ============================================================================
    # Revoke Date
    # ============================================================================
    def test_user_admin_get_revoke_date_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_revoke_date("squidwrd"), "10/22/2023")

    def test_user_admin_get_revoke_date_returns_none_when_there_is_no_revoke_date(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(self.user_admin.get_revoke_date("squidwrd"), None)

    # ============================================================================
    # Resume Date
    # ============================================================================
    def test_user_admin_get_resume_date_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_resume_date("squidwrd"), "11/2/2023")

    def test_user_admin_get_resume_date_returns_none_when_there_is_no_resume_date(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(self.user_admin.get_resume_date("squidwrd"), None)

    # ============================================================================
    # Owner
    # ============================================================================
    def test_user_admin_get_owner_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_owner("squidwrd"), "leonard")

    def test_user_admin_get_owner_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        ).replace("OWNER=LEONARD", "OWNER=12345678")
        self.assertEqual(self.user_admin.get_owner("squidwrd"), "12345678")

    # ============================================================================
    # Name
    # ============================================================================
    def test_user_admin_get_name_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_name("squidwrd"), "squidward")

    def test_user_admin_get_name_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        ).replace("NAME=SQUIDWARD", "NAME=12345678")
        self.assertEqual(self.user_admin.get_name("squidwrd"), "12345678")

    # ============================================================================
    # OMVS UID
    # ============================================================================
    def test_user_admin_get_omvs_uid_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(self.user_admin.get_omvs_uid("squidwrd"), 2424)

    def test_user_admin_get_omvs_uid_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_uid("squidwrd")

    def test_user_admin_get_omvs_uid_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_uid("squidwrd"))

    # ============================================================================
    # OMVS Max Address Space Size
    # ============================================================================
    def test_user_admin_get_omvs_max_address_space_size_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(
            self.user_admin.get_omvs_max_address_space_size("squidwrd"), 10485760
        )

    def test_user_admin_get_omvs_max_address_space_size_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_max_address_space_size("squidwrd")

    def test_user_admin_get_omvs_max_address_space_size_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_address_space_size("squidwrd"))

    # ============================================================================
    # OMVS Max CPU Time
    # ============================================================================
    def test_user_admin_get_omvs_max_cpu_time_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_omvs_max_cpu_time("squidwrd"), 1500)

    def test_user_admin_get_omvs_max_cpu_time_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_max_cpu_time("squidwrd")

    def test_user_admin_get_omvs_max_cpu_time_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_cpu_time("squidwrd"))

    # ============================================================================
    # OMVS Max CPU Time
    # ============================================================================
    def test_user_admin_get_omvs_max_files_per_process_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_omvs_max_files_per_process("squidwrd"), 50)

    def test_user_admin_get_omvs_max_files_per_process_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_max_files_per_process("squidwrd")

    def test_user_admin_get_omvs_max_files_per_process_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_files_per_process("squidwrd"))

    # ============================================================================
    # OMVS Max Non-Shared Memory
    # ============================================================================
    def test_user_admin_get_omvs_max_non_shared_memory_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(
            self.user_admin.get_omvs_max_non_shared_memory("squidwrd"), "4g"
        )

    def test_user_admin_get_omvs_max_non_shared_memory_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_max_non_shared_memory("squidwrd")

    def test_user_admin_get_omvs_max_non_shared_memory_returns_none_when_field_is_unset(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_non_shared_memory("squidwrd"))

    def test_user_admin_get_omvs_max_non_shared_memory_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_non_shared_memory("squidwrd"))

    # ============================================================================
    # OMVS Max File Mapping Pages
    # ============================================================================
    def test_user_admin_get_omvs_max_file_mapping_pages_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(
            self.user_admin.get_omvs_max_file_mapping_pages("squidwrd"), 350
        )

    def test_user_admin_get_omvs_max_file_mapping_pages_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_max_file_mapping_pages("squidwrd")

    def test_user_admin_get_omvs_max_file_mapping_pages_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_file_mapping_pages("squidwrd"))

    # ============================================================================
    # OMVS Max Processes
    # ============================================================================
    def test_user_admin_get_omvs_max_processes_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_omvs_max_processes("squidwrd"), 128)

    def test_user_admin_get_omvs_max_processes_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_max_processes("squidwrd")

    def test_user_admin_get_omvs_max_processes_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_processes("squidwrd"))

    # ============================================================================
    # OMVS Max Shared Memory
    # ============================================================================
    def test_user_admin_get_omvs_max_shared_memory_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_omvs_max_shared_memory("squidwrd"), "2g")

    def test_user_admin_get_omvs_max_shared_memory_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_max_shared_memory("squidwrd")

    def test_user_admin_get_omvs_max_shared_memory_returns_none_when_field_is_unset(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_shared_memory("squidwrd"))

    def test_user_admin_get_omvs_max_shared_memory_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_shared_memory("squidwrd"))

    # ============================================================================
    # OMVS Max Threads
    # ============================================================================
    def test_user_admin_get_omvs_max_threads_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_omvs_max_threads("squidwrd"), 48)

    def test_user_admin_get_omvs_max_threads_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_max_threads("squidwrd")

    def test_user_admin_get_omvs_max_threads_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_max_threads("squidwrd"))

    # ============================================================================
    # OMVS Home Directory
    # ============================================================================
    def test_user_admin_get_omvs_home_directory_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(
            self.user_admin.get_omvs_home_directory("squidwrd"), "/u/squidwrd"
        )

    def test_user_admin_get_omvs_home_directory_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_home_directory("squidwrd")

    def test_user_admin_get_omvs_home_directory_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_home_directory("squidwrd"))

    def test_user_admin_get_omvs_home_directory_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        ).replace("HOME= /u/squidwrd", "HOME= 12345678")
        self.assertEqual(
            self.user_admin.get_omvs_home_directory("squidwrd"), "12345678"
        )

    def test_user_admin_get_omvs_home_directory_handles_case_sensitivity_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        ).replace("HOME= /u/squidwrd", "HOME= /u/SQUIDWRD")
        self.assertEqual(
            self.user_admin.get_omvs_home_directory("squidwrd"), "/u/SQUIDWRD"
        )

    # ============================================================================
    # OMVS Program
    # ============================================================================
    def test_user_admin_get_omvs_default_shell_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(self.user_admin.get_omvs_default_shell("squidwrd"), "/bin/sh")

    def test_user_admin_get_omvs_default_shell_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_omvs_default_shell("squidwrd")

    def test_user_admin_get_omvs_default_shell_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_omvs_default_shell("squidwrd"))

    def test_user_admin_get_omvs_default_shell_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        ).replace("PROGRAM= /bin/sh", "PROGRAM= 12345678")
        self.assertEqual(self.user_admin.get_omvs_default_shell("squidwrd"), "12345678")

    def test_user_admin_get_omvs_default_shell_handles_case_sensitivity_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_SUCCESS_XML
        ).replace("PROGRAM= /bin/sh", "PROGRAM= /BIN/sh")
        self.assertEqual(self.user_admin.get_omvs_default_shell("squidwrd"), "/BIN/sh")

    # ============================================================================
    # TSO Account Number
    # ============================================================================
    def test_user_admin_get_tso_account_number_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_tso_account_number("squidwrd"), "sb29")

    def test_user_admin_get_tso_account_number_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_account_number("squidwrd")

    def test_user_admin_get_tso_account_number_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_account_number("squidwrd"))

    def test_user_admin_get_tso_account_number_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        ).replace("ACCTNUM= SB29", "ACCTNUM= 1234")
        self.assertEqual(self.user_admin.get_tso_account_number("squidwrd"), "1234")

    # ============================================================================
    # TSO Logon Command
    # ============================================================================
    def test_user_admin_get_tso_logon_command_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_tso_logon_command("squidwrd"), "ispf")

    def test_user_admin_get_tso_logon_command_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_logon_command("squidwrd")

    def test_user_admin_get_tso_logon_command_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_logon_command("squidwrd"))

    def test_user_admin_get_tso_logon_command_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        ).replace("COMMAND= ISPF", "COMMAND= 1234")
        self.assertEqual(self.user_admin.get_tso_logon_command("squidwrd"), "1234")

    # ============================================================================
    # TSO Hold Class
    # ============================================================================
    def test_user_admin_get_tso_hold_class_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_tso_hold_class("squidwrd"), "a")

    def test_user_admin_get_tso_hold_class_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_hold_class("squidwrd")

    def test_user_admin_get_tso_hold_class_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_hold_class("squidwrd"))

    def test_user_admin_get_tso_hold_class_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        ).replace("HOLDCLASS= A", "HOLDCLASS= 1")
        self.assertEqual(self.user_admin.get_tso_hold_class("squidwrd"), "1")

    # ============================================================================
    # TSO Max Region size
    # ============================================================================
    def test_user_admin_get_tso_max_region_size_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_tso_max_region_size("squidwrd"), 2048)

    def test_user_admin_get_tso_max_region_size_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_max_region_size("squidwrd")

    def test_user_admin_get_tso_max_region_size_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_max_region_size("squidwrd"))

    # ============================================================================
    # TSO Message Class
    # ============================================================================
    def test_user_admin_get_tso_message_class_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_tso_message_class("squidwrd"), "b")

    def test_user_admin_get_tso_message_class_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_message_class("squidwrd")

    def test_user_admin_get_tso_message_class_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_message_class("squidwrd"))

    def test_user_admin_get_tso_message_class_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        ).replace("MSGCLASS= B", "MSGCLASS= 1")
        self.assertEqual(self.user_admin.get_tso_message_class("squidwrd"), "1")

    # ============================================================================
    # TSO Logon Procedure
    # ============================================================================
    def test_user_admin_get_tso_logon_procedure_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_tso_logon_procedure("squidwrd"), "proc")

    def test_user_admin_get_tso_logon_procedure_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_logon_procedure("squidwrd")

    def test_user_admin_get_tso_logon_procedure_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_logon_procedure("squidwrd"))

    def test_user_admin_get_tso_logon_procedure_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        ).replace("PROC= PROC", "PROC= 1234")
        self.assertEqual(self.user_admin.get_tso_logon_procedure("squidwrd"), "1234")

    # ============================================================================
    # TSO Default Region size
    # ============================================================================
    def test_user_admin_get_tso_region_size_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_tso_default_region_size("squidwrd"), 1024)

    def test_user_admin_get_tso_default_region_size_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_default_region_size("squidwrd")

    def test_user_admin_get_default_tso_region_size_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_default_region_size("squidwrd"))

    # ============================================================================
    # TSO Sysout Class
    # ============================================================================
    def test_user_admin_get_tso_sysout_class_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_tso_sysout_class("squidwrd"), "o")

    def test_user_admin_get_tso_sysout_class_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_sysout_class("squidwrd")

    def test_user_admin_get_tso_sysout_class_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_sysout_class("squidwrd"))

    def test_user_admin_get_tso_sysout_class_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        ).replace("SYSOUTCLASS= O", "SYSOUTCLASS= 1")
        self.assertEqual(self.user_admin.get_tso_sysout_class("squidwrd"), "1")

    # ============================================================================
    # TSO User Data
    # ============================================================================
    def test_user_admin_get_tso_user_data_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(self.user_admin.get_tso_user_data("squidwrd"), "abcd")

    def test_user_admin_get_tso_user_data_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_user_data("squidwrd")

    def test_user_admin_get_tso_user_data_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_user_data("squidwrd"))

    def test_user_admin_get_tso_user_data_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        ).replace("USERDATA= ABCD", "USERDATA= 1234")
        self.assertEqual(self.user_admin.get_tso_user_data("squidwrd"), "1234")

    # ============================================================================
    # TSO User Data
    # ============================================================================
    def test_user_admin_get_tso_data_set_allocation_unit_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        )
        self.assertEqual(
            self.user_admin.get_tso_data_set_allocation_unit("squidwrd"), "sysda"
        )

    def test_user_admin_get_tso_data_set_allocation_unit_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.user_admin.get_tso_data_set_allocation_unit("squidwrd")

    def test_user_admin_get_tso_data_set_allocation_unit_returns_none_when_no_tso_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.user_admin.get_tso_data_set_allocation_unit("squidwrd"))

    def test_user_admin_get_tso_data_set_allocation_unit_handles_non_string_value_properly(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestUserConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_TSO_REVOKE_RESUME_XML
        ).replace("UNIT= SYSDA", "UNIT= 1234")
        self.assertEqual(
            self.user_admin.get_tso_data_set_allocation_unit("squidwrd"), "1234"
        )
