"""Test setropts setter functions."""

import unittest

import __init__

import tests.setropts.test_setropts_constants as TestSetroptsConstants
from pyracf import SetroptsAdmin

# Resolves F401
__init__


class TestSetroptsSetters(unittest.TestCase):
    maxDiff = None
    setropts_admin = SetroptsAdmin(generate_requests_only=True)

    # ============================================================================
    # Class Adders
    # ============================================================================
    def test_setropts_admin_build_add_audit_class_request(self):
        result = self.setropts_admin.add_audit_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_AUDIT_CLASS_XML
        )

    def test_setropts_admin_build_add_active_class_request(self):
        result = self.setropts_admin.add_active_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_ACTIVE_CLASS_XML
        )

    def test_setropts_admin_build_add_statistics_class_request(self):
        result = self.setropts_admin.add_statistics_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_STATISTICS_CLASS_XML
        )

    def test_setropts_admin_build_add_generic_command_processing_class_request(self):
        result = self.setropts_admin.add_generic_command_processing_classes("elijtest")
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_ADD_GENERIC_COMMAND_PROCESSING_CLASS_XML,
        )

    def test_setropts_admin_build_add_generic_profile_checking_class_request(self):
        result = self.setropts_admin.add_generic_profile_checking_classes("elijtest")
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_ADD_GENERIC_PROFILE_CHECKING_CLASS_XML,
        )

    def test_setropts_admin_build_add_generic_profile_sharing_class_request(self):
        result = self.setropts_admin.add_generic_profile_sharing_classes("elijtest")
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_ADD_GENERIC_PROFILE_SHARING_CLASS_XML,
        )

    def test_setropts_admin_build_add_global_access_class_request(self):
        result = self.setropts_admin.add_global_access_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_GLOBAL_ACCESS_CLASS_XML
        )

    def test_setropts_admin_build_add_raclist_class_request(self):
        result = self.setropts_admin.add_raclist_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_RACLIST_CLASS_XML
        )

    def test_setropts_admin_build_add_audit_classes_request_string(self):
        result = self.setropts_admin.add_audit_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_AUDIT_CLASSES_XML
        )

    def test_setropts_admin_build_add_active_classes_request_string(self):
        result = self.setropts_admin.add_active_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_ACTIVE_CLASSES_XML
        )

    def test_setropts_admin_build_add_statistics_classes_request_string(self):
        result = self.setropts_admin.add_statistics_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_STATISTICS_CLASSES_XML
        )

    def test_setropts_admin_build_add_generic_command_processing_classes_request_string(
        self,
    ):
        result = self.setropts_admin.add_generic_command_processing_classes(
            "elijtest xfacilit"
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_ADD_GENERIC_COMMAND_PROCESSING_CLASSES_XML,
        )

    def test_setropts_admin_build_add_generic_profile_checking_classes_request_string(
        self,
    ):
        result = self.setropts_admin.add_generic_profile_checking_classes(
            "elijtest xfacilit"
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_ADD_GENERIC_PROFILE_CHECKING_CLASSES_XML,
        )

    def test_setropts_admin_build_add_generic_profile_sharing_classes_request_string(
        self,
    ):
        result = self.setropts_admin.add_generic_profile_sharing_classes(
            "elijtest xfacilit"
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_ADD_GENERIC_PROFILE_SHARING_CLASSES_XML,
        )

    def test_setropts_admin_build_add_global_access_classes_request_string(self):
        result = self.setropts_admin.add_global_access_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_GLOBAL_ACCESS_CLASSES_XML
        )

    def test_setropts_admin_build_add_raclist_classes_request_string(self):
        result = self.setropts_admin.add_raclist_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_RACLIST_CLASSES_XML
        )

    def test_setropts_admin_build_add_audit_classes_request_list(self):
        result = self.setropts_admin.add_audit_classes(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_AUDIT_CLASSES_XML
        )

    def test_setropts_admin_build_add_active_classes_request_list(self):
        result = self.setropts_admin.add_active_classes(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_ACTIVE_CLASSES_XML
        )

    def test_setropts_admin_build_add_statistics_classes_request_list(self):
        result = self.setropts_admin.add_statistics_classes(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_STATISTICS_CLASSES_XML
        )

    def test_setropts_admin_build_add_generic_command_processing_classes_request_list(
        self,
    ):
        result = self.setropts_admin.add_generic_command_processing_classes(
            ["elijtest", "xfacilit"]
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_ADD_GENERIC_COMMAND_PROCESSING_CLASSES_XML,
        )

    def test_setropts_admin_build_add_generic_profile_checking_classes_request_list(
        self,
    ):
        result = self.setropts_admin.add_generic_profile_checking_classes(
            ["elijtest", "xfacilit"]
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_ADD_GENERIC_PROFILE_CHECKING_CLASSES_XML,
        )

    def test_setropts_admin_build_add_generic_profile_sharing_classes_request_list(
        self,
    ):
        result = self.setropts_admin.add_generic_profile_sharing_classes(
            ["elijtest", "xfacilit"]
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_ADD_GENERIC_PROFILE_SHARING_CLASSES_XML,
        )

    def test_setropts_admin_build_add_global_access_classes_request_list(self):
        result = self.setropts_admin.add_global_access_classes(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_GLOBAL_ACCESS_CLASSES_XML
        )

    def test_setropts_admin_build_add_raclist_classes_request_list(self):
        result = self.setropts_admin.add_raclist_classes(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_ADD_RACLIST_CLASSES_XML
        )

    # ============================================================================
    # Class Removers
    # ============================================================================
    def test_setropts_admin_build_remove_audit_class_request(self):
        result = self.setropts_admin.remove_audit_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_AUDIT_CLASS_XML
        )

    def test_setropts_admin_build_remove_active_class_request(self):
        result = self.setropts_admin.remove_active_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_ACTIVE_CLASS_XML
        )

    def test_setropts_admin_build_remove_statistics_class_request(self):
        result = self.setropts_admin.remove_statistics_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_STATISTICS_CLASS_XML
        )

    def test_setropts_admin_build_remove_generic_command_processing_class_request(self):
        result = self.setropts_admin.remove_generic_command_processing_classes(
            "elijtest"
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_REMOVE_GENERIC_COMMAND_PROCESSING_CLASS_XML,
        )

    def test_setropts_admin_build_remove_generic_profile_checking_class_request(self):
        result = self.setropts_admin.remove_generic_profile_checking_classes("elijtest")
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_REMOVE_GENERIC_PROFILE_CHECKING_CLASS_XML,
        )

    def test_setropts_admin_build_remove_generic_profile_sharing_class_request(self):
        result = self.setropts_admin.remove_generic_profile_sharing_classes("elijtest")
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_REMOVE_GENERIC_PROFILE_SHARING_CLASS_XML,
        )

    def test_setropts_admin_build_remove_global_access_class_request(self):
        result = self.setropts_admin.remove_global_access_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_GLOBAL_ACCESS_CLASS_XML
        )

    def test_setropts_admin_build_remove_raclist_class_request(self):
        result = self.setropts_admin.remove_raclist_classes("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_RACLIST_CLASS_XML
        )

    def test_setropts_admin_build_remove_audit_classes_request_string(self):
        result = self.setropts_admin.remove_audit_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_AUDIT_CLASSES_XML
        )

    def test_setropts_admin_build_remove_active_classes_request_string(self):
        result = self.setropts_admin.remove_active_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_ACTIVE_CLASSES_XML
        )

    def test_setropts_admin_build_remove_statistics_classes_request_string(self):
        result = self.setropts_admin.remove_statistics_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_STATISTICS_CLASSES_XML
        )

    def test_setropts_admin_build_remove_generic_command_processing_classes_request_string(
        self,
    ):
        result = self.setropts_admin.remove_generic_command_processing_classes(
            "elijtest xfacilit"
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_REMOVE_GENERIC_COMMAND_PROCESSING_CLASSES_XML,
        )

    def test_setropts_admin_build_remove_generic_profile_checking_classes_request_string(
        self,
    ):
        result = self.setropts_admin.remove_generic_profile_checking_classes(
            "elijtest xfacilit"
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_REMOVE_GENERIC_PROFILE_CHECKING_CLASSES_XML,
        )

    def test_setropts_admin_build_remove_generic_profile_sharing_classes_request_string(
        self,
    ):
        result = self.setropts_admin.remove_generic_profile_sharing_classes(
            "elijtest xfacilit"
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_REMOVE_GENERIC_PROFILE_SHARING_CLASSES_XML,
        )

    def test_setropts_admin_build_remove_global_access_classes_request_string(self):
        result = self.setropts_admin.remove_global_access_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_GLOBAL_ACCESS_CLASSES_XML
        )

    def test_setropts_admin_build_remove_raclist_classes_request_string(self):
        result = self.setropts_admin.remove_raclist_classes("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_RACLIST_CLASSES_XML
        )

    def test_setropts_admin_build_remove_audit_classes_request_list(self):
        result = self.setropts_admin.remove_audit_classes(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_AUDIT_CLASSES_XML
        )

    def test_setropts_admin_build_remove_active_classes_request_list(self):
        result = self.setropts_admin.remove_active_classes(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_ACTIVE_CLASSES_XML
        )

    def test_setropts_admin_build_remove_statistics_classes_request_list(self):
        result = self.setropts_admin.remove_statistics_classes(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_STATISTICS_CLASSES_XML
        )

    def test_setropts_admin_build_remove_generic_command_processing_classes_request_list(
        self,
    ):
        result = self.setropts_admin.remove_generic_command_processing_classes(
            ["elijtest", "xfacilit"]
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_REMOVE_GENERIC_COMMAND_PROCESSING_CLASSES_XML,
        )

    def test_setropts_admin_build_remove_generic_profile_checking_classes_request_list(
        self,
    ):
        result = self.setropts_admin.remove_generic_profile_checking_classes(
            ["elijtest", "xfacilit"]
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_REMOVE_GENERIC_PROFILE_CHECKING_CLASSES_XML,
        )

    def test_setropts_admin_build_remove_generic_profile_sharing_classes_request_list(
        self,
    ):
        result = self.setropts_admin.remove_generic_profile_sharing_classes(
            ["elijtest", "xfacilit"]
        )
        self.assertEqual(
            result,
            TestSetroptsConstants.TEST_SETROPTS_REMOVE_GENERIC_PROFILE_SHARING_CLASSES_XML,
        )

    def test_setropts_admin_build_remove_global_access_classes_request_list(self):
        result = self.setropts_admin.remove_global_access_classes(
            ["elijtest", "xfacilit"]
        )
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_GLOBAL_ACCESS_CLASSES_XML
        )

    def test_setropts_admin_build_remove_raclist_classes_request_list(self):
        result = self.setropts_admin.remove_raclist_classes(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REMOVE_RACLIST_CLASSES_XML
        )

    # ============================================================================
    # Raclist Refresh
    # ============================================================================
    def test_setropts_admin_build_refresh_raclist_request(self):
        result = self.setropts_admin.refresh_raclist("elijtest")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REFRESH_RACLIST_XML
        )

    def test_setropts_admin_build_refresh_raclist_multiple_request_list(self):
        result = self.setropts_admin.refresh_raclist(["elijtest", "xfacilit"])
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REFRESH_RACLIST_MULTIPLE_XML
        )

    def test_setropts_admin_build_refresh_raclist_multiple_request_string(self):
        result = self.setropts_admin.refresh_raclist("elijtest xfacilit")
        self.assertEqual(
            result, TestSetroptsConstants.TEST_SETROPTS_REFRESH_RACLIST_MULTIPLE_XML
        )
