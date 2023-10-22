"""Test user setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.user.test_user_constants as TestUserConstants
from pyracf import UserAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestUserSetters(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    user_admin = UserAdmin(generate_requests_only=True)

    # ============================================================================
    # Special Authority
    # ============================================================================
    def test_user_admin_build_give_special_authority_request(self):
        result = self.user_admin.give_special_authority(
            "squidwrd",
        )
        self.assertEqual(result, TestUserConstants.TEST_USER_GIVE_SPECIAL_AUTHORITY_XML)

    def test_user_admin_build_remove_special_authority_request(self):
        result = self.user_admin.take_away_special_authority("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_REMOVE_SPECIAL_AUTHORITY_XML
        )

    # ============================================================================
    # Auditor Authority
    # ============================================================================
    def test_user_admin_build_give_auditor_authority_request(self):
        result = self.user_admin.give_auditor_authority("squidwrd")
        self.assertEqual(result, TestUserConstants.TEST_USER_GIVE_AUDITOR_AUTHORITY_XML)

    def test_user_admin_build_remove_auditor_authority_request(self):
        result = self.user_admin.take_away_auditor_authority("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_REMOVE_AUDITOR_AUTHORITY_XML
        )

    # ============================================================================
    # Operations Authority
    # ============================================================================
    def test_user_admin_build_give_operations_authority_request(self):
        result = self.user_admin.give_operations_authority("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_GIVE_OPERATIONS_AUTHORITY_XML
        )

    def test_user_admin_build_remove_operations_authority_request(self):
        result = self.user_admin.take_away_operations_authority("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_REMOVE_OPERATIONS_AUTHORITY_XML
        )

    # ============================================================================
    # Password
    # ============================================================================
    def test_user_admin_build_set_password_request(self):
        result = self.user_admin.set_password("squidwrd", "GIyTTqdF")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_PASSWORD_XML)

    def test_user_admin_build_set_password_delete_request(self):
        result = self.user_admin.set_password("squidwrd", False)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_PASSWORD_DELETE_XML)

    # ============================================================================
    # Passphrase
    # ============================================================================
    def test_user_admin_build_set_passphrase_request(self):
        result = self.user_admin.set_passphrase("squidwrd", "PassPhrasesAreCool!")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_PASSPHRASE_XML)

    def test_user_admin_build_set_passphrase_delete_request(self):
        result = self.user_admin.set_passphrase("squidwrd", False)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_PASSPHRASE_DELETE_XML)

    # ============================================================================
    # Class Authorizations
    # ============================================================================
    def test_user_admin_build_add_class_authorizations_single_class_request(self):
        result = self.user_admin.add_class_authorizations("squidwrd", "facility")
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_ADD_CLASS_AUTHORIZATIONS_SINGLE_CLASS_XML,
        )

    def test_user_admin_build_add_class_authorizations_multiple_classes_request(self):
        result = self.user_admin.add_class_authorizations(
            "squidwrd", ["facility", "terminal"]
        )
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_ADD_CLASS_AUTHORIZATIONS_MULTIPLE_CLASSES_XML,
        )

    def test_user_admin_build_remove_class_authorizations_single_class_request(self):
        result = self.user_admin.remove_class_authorizations("squidwrd", "facility")
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_REMOVE_CLASS_AUTHORIZATIONS_SINGLE_CLASS_XML,
        )

    def test_user_admin_build_remove_class_authorizations_multiple_classes_request(
        self,
    ):
        result = self.user_admin.remove_class_authorizations(
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
    ):
        get_class_authorizations_mock.return_value = [
            "facility",
            "terminal",
            "xfacilit",
        ]
        result = self.user_admin.delete_all_class_authorizations("squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_DELETE_ALL_CLASS_AUTHORIZATIONS_XML
        )

    @patch("pyracf.user.user_admin.UserAdmin.get_class_authorizations")
    def test_user_admin_build_delete_all_class_authorizations_request_returns_false_if_none(
        self,
        get_class_authorizations_mock: Mock,
    ):
        get_class_authorizations_mock.return_value = []
        result = self.user_admin.delete_all_class_authorizations("squidwrd")
        self.assertFalse(result)

    @patch("pyracf.user.user_admin.UserAdmin.get_class_authorizations")
    def test_user_admin_build_set_class_authorizations_request(
        self,
        get_class_authorizations_mock: Mock,
    ):
        get_class_authorizations_mock.return_value = [
            "facility",
            "terminal",
            "xfacilit",
        ]
        result = self.user_admin.set_class_authorizations(
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
    ):
        get_class_authorizations_mock.return_value = []
        result = self.user_admin.set_class_authorizations(
            "squidwrd", ["terminal", "xfacilit"]
        )
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_CLASS_AUTHORIZATIONS_XML
        )

    # ============================================================================
    # Revoke Date
    # ============================================================================
    def test_user_admin_build_set_revoke_date_request(self):
        result = self.user_admin.set_revoke_date("squidwrd", "10/22/23")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_REVOKE_DATE_XML)

    def test_user_admin_build_set_revoke_date_delete_request(self):
        result = self.user_admin.set_revoke_date("squidwrd", False)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_REVOKE_DATE_DELETE_XML)

    # ============================================================================
    # Resume Date
    # ============================================================================
    def test_user_admin_build_set_resume_date_request(self):
        result = self.user_admin.set_resume_date("squidwrd", "11/2/23")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_RESUME_DATE_XML)

    def test_user_admin_build_set_resume_date_delete_request(self):
        result = self.user_admin.set_resume_date("squidwrd", False)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_RESUME_DATE_DELETE_XML)

    # ============================================================================
    # Owner
    # ============================================================================
    def test_user_admin_build_set_owner_request(self):
        result = self.user_admin.set_owner("squidwrd", "leonard")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OWNER_XML)

    # ============================================================================
    # Name
    # ============================================================================
    def test_user_admin_build_set_name_request(self):
        result = self.user_admin.set_name("squidwrd", "Squidward")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_NAME_XML)

    def test_user_admin_build_set_name_delete_request(self):
        result = self.user_admin.set_name("squidwrd", False)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_NAME_DELETE_XML)

    # ============================================================================
    # OMVS UID
    # ============================================================================
    def test_user_admin_build_set_omvs_uid_request(self):
        result = self.user_admin.set_omvs_uid("squidwrd", 40)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_UID_XML)

    def test_user_admin_build_set_omvs_uid_delete_request(self):
        result = self.user_admin.set_omvs_uid("squidwrd", False)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_UID_DELETE_XML)

    # ============================================================================
    # OMVS Max Address Space Size
    # ============================================================================
    def test_user_admin_build_set_omvs_max_address_space_size_request(self):
        result = self.user_admin.set_omvs_max_address_space_size("squidwrd", 10485760)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_MAX_ADDRESS_SPACE_SIZE_XML
        )

    def test_user_admin_build_set_max_address_space_size_delete_request(self):
        result = self.user_admin.set_omvs_max_address_space_size("squidwrd", False)
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_SET_OMVS_MAX_ADDRESS_SPACE_SIZE_DELETE_XML,
        )

    # ============================================================================
    # OMVS Max CPU Time
    # ============================================================================
    def test_user_admin_build_set_omvs_max_cpu_time_request(self):
        result = self.user_admin.set_omvs_max_cpu_time("squidwrd", 1500)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_MAX_CPU_TIME_XML)

    def test_user_admin_build_set_max_cpu_time_delete_request(self):
        result = self.user_admin.set_omvs_max_cpu_time("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_MAX_CPU_TIME_DELETE_XML
        )

    # ============================================================================
    # OMVS Max Files Per Process
    # ============================================================================
    def test_user_admin_build_set_omvs_max_files_per_process_request(self):
        result = self.user_admin.set_omvs_max_files_per_process("squidwrd", 50)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_MAX_FILES_PER_PROCESS_XML
        )

    def test_user_admin_build_set_max_files_per_process_delete_request(self):
        result = self.user_admin.set_omvs_max_files_per_process("squidwrd", False)
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_SET_OMVS_MAX_FILES_PER_PROCESS_DELETE_XML,
        )

    # ============================================================================
    # OMVS Max Non-Shared Memory
    # ============================================================================
    def test_user_admin_build_set_omvs_max_non_shared_memory_request(self):
        result = self.user_admin.set_omvs_max_non_shared_memory("squidwrd", "4g")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_MAX_NON_SHARED_MEMORY_XML
        )

    def test_user_admin_build_set_max_non_shared_memory_delete_request(self):
        result = self.user_admin.set_omvs_max_non_shared_memory("squidwrd", False)
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_SET_OMVS_MAX_NON_SHARED_MEMORY_DELETE_XML,
        )

    # ============================================================================
    # OMVS Max File Mapping Pages
    # ============================================================================
    def test_user_admin_build_set_omvs_max_file_mapping_pages_request(self):
        result = self.user_admin.set_omvs_max_file_mapping_pages("squidwrd", 350)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_MAX_FILE_MAPPING_PAGES_XML
        )

    def test_user_admin_build_set_max_file_mapping_pages_delete_request(self):
        result = self.user_admin.set_omvs_max_file_mapping_pages("squidwrd", False)
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_SET_OMVS_MAX_FILE_MAPPING_PAGES_DELETE_XML,
        )

    # ============================================================================
    # OMVS Max Processes
    # ============================================================================
    def test_user_admin_build_set_omvs_max_processes_request(self):
        result = self.user_admin.set_omvs_max_processes("squidwrd", 128)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_MAX_PROCESSES_XML)

    def test_user_admin_build_set_omvs_max_processes_delete_request(self):
        result = self.user_admin.set_omvs_max_processes("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_MAX_PROCESSES_DELETE_XML
        )

    # ============================================================================
    # OMVS Max Shared Memory
    # ============================================================================
    def test_user_admin_build_set_omvs_max_shared_memory_request(self):
        result = self.user_admin.set_omvs_max_shared_memory("squidwrd", "2g")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_MAX_SHARED_MEMORY_XML
        )

    def test_user_admin_build_set_omvs_max_shared_memory_delete_request(self):
        result = self.user_admin.set_omvs_max_shared_memory("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_MAX_SHARED_MEMORY_DELETE_XML
        )

    # ============================================================================
    # OMVS Max Threads
    # ============================================================================
    def test_user_admin_build_set_omvs_max_threads_request(self):
        result = self.user_admin.set_omvs_max_threads("squidwrd", 48)
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_MAX_THREADS_XML)

    def test_user_admin_build_set_omvs_max_threads_delete_request(self):
        result = self.user_admin.set_omvs_max_threads("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_MAX_THREADS_DELETE_XML
        )

    # ============================================================================
    # OMVS Home Directory
    # ============================================================================
    def test_user_admin_build_set_omvs_home_directory_request(self):
        result = self.user_admin.set_omvs_home_directory("squidwrd", "/u/squidwrd")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_HOME_DIRECTORY_XML
        )

    def test_user_admin_build_set_omvs_home_directory_delete_request(self):
        result = self.user_admin.set_omvs_home_directory("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_HOME_DIRECTORY_DELETE_XML
        )

    # ============================================================================
    # OMVS Default Shell
    # ============================================================================
    def test_user_admin_build_set_omvs_default_shell_request(self):
        result = self.user_admin.set_omvs_default_shell("squidwrd", "/bin/sh")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_OMVS_DEFAULT_SHELL_XML)

    def test_user_admin_build_set_omvs_default_shell_delete_request(self):
        result = self.user_admin.set_omvs_default_shell("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_OMVS_DEFAULT_SHELL_DELETE_XML
        )

    # ============================================================================
    # TSO Account Number
    # ============================================================================
    def test_user_admin_build_set_tso_account_number_request(self):
        result = self.user_admin.set_tso_account_number("squidwrd", "SB29")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_TSO_ACCOUNT_NUMBER_XML)

    def test_user_admin_build_set_tso_account_number_delete_request(self):
        result = self.user_admin.set_tso_account_number("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_ACCOUNT_NUMBER_DELETE_XML
        )

    # ============================================================================
    # TSO Logon Command
    # ============================================================================
    def test_user_admin_build_set_tso_logon_command_request(self):
        result = self.user_admin.set_tso_logon_command("squidwrd", "ISPF")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_TSO_LOGON_COMMAND_XML)

    def test_user_admin_build_set_tso_logon_command_delete_request(self):
        result = self.user_admin.set_tso_logon_command("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_LOGON_COMMAND_DELETE_XML
        )

    # ============================================================================
    # TSO Hold Class
    # ============================================================================
    def test_user_admin_build_set_tso_hold_class_request(self):
        result = self.user_admin.set_tso_hold_class("squidwrd", "A")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_TSO_HOLD_CLASS_XML)

    def test_user_admin_build_set_tso_hold_class_delete_request(self):
        result = self.user_admin.set_tso_hold_class("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_HOLD_CLASS_DELETE_XML
        )

    # ============================================================================
    # TSO Max Region Size
    # ============================================================================
    def test_user_admin_build_set_tso_max_region_size_request(self):
        result = self.user_admin.set_tso_max_region_size("squidwrd", 2048)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_MAX_REGION_SIZE_XML
        )

    def test_user_admin_build_set_tso_max_region_size_delete_request(self):
        result = self.user_admin.set_tso_max_region_size("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_MAX_REGION_SIZE_DELETE_XML
        )

    # ============================================================================
    # TSO Message Class
    # ============================================================================
    def test_user_admin_build_set_tso_message_class_request(self):
        result = self.user_admin.set_tso_message_class("squidwrd", "B")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_TSO_MESSAGE_CLASS_XML)

    def test_user_admin_build_set_tso_message_class_delete_request(self):
        result = self.user_admin.set_tso_message_class("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_MESSAGE_CLASS_DELETE_XML
        )

    # ============================================================================
    # TSO Logon Procedure
    # ============================================================================
    def test_user_admin_build_set_tso_logon_procedure_request(self):
        result = self.user_admin.set_tso_logon_procedure("squidwrd", "PROC")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_LOGON_PROCEDURE_XML
        )

    def test_user_admin_build_set_tso_logon_procedure_delete_request(self):
        result = self.user_admin.set_tso_logon_procedure("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_LOGON_PROCEDURE_DELETE_XML
        )

    # ============================================================================
    # TSO Region Size
    # ============================================================================
    def test_user_admin_build_set_tso_default_region_size_request(self):
        result = self.user_admin.set_tso_default_region_size("squidwrd", 2048)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_DEFAULT_REGION_SIZE_XML
        )

    def test_user_admin_build_set_tso_default_region_size_delete_request(self):
        result = self.user_admin.set_tso_default_region_size("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_DEFAULT_REGION_SIZE_DELETE_XML
        )

    # ============================================================================
    # TSO Sysout Class
    # ============================================================================
    def test_user_admin_build_set_tso_sysout_class_request(self):
        result = self.user_admin.set_tso_sysout_class("squidwrd", "O")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_TSO_SYSOUT_CLASS_XML)

    def test_user_admin_build_set_tso_sysout_class_delete_request(self):
        result = self.user_admin.set_tso_sysout_class("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_SYSOUT_CLASS_DELETE_XML
        )

    # ============================================================================
    # TSO User Data
    # ============================================================================
    def test_user_admin_build_set_tso_user_data_request(self):
        result = self.user_admin.set_tso_user_data("squidwrd", "ABCD")
        self.assertEqual(result, TestUserConstants.TEST_USER_SET_TSO_USER_DATA_XML)

    def test_user_admin_build_set_tso_user_data_delete_request(self):
        result = self.user_admin.set_tso_user_data("squidwrd", False)
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_USER_DATA_DELETE_XML
        )

    # ============================================================================
    # TSO Data Set Allocation Unit
    # ============================================================================
    def test_user_admin_build_set_tso_data_set_allocation_unit_request(self):
        result = self.user_admin.set_tso_data_set_allocation_unit("squidwrd", "SYSDA")
        self.assertEqual(
            result, TestUserConstants.TEST_USER_SET_TSO_DATA_SET_ALLOCATION_UNIT_XML
        )

    def test_user_admin_build_set_tso_data_set_allocation_unit_delete_request(self):
        result = self.user_admin.set_tso_data_set_allocation_unit("squidwrd", False)
        self.assertEqual(
            result,
            TestUserConstants.TEST_USER_SET_TSO_DATA_SET_ALLOCATION_UNIT_DELETE_XML,
        )
