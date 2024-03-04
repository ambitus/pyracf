"""Test group getter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.group.test_group_constants as TestGroupConstants
from pyracf import GroupAdmin, SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestGroupGetters(unittest.TestCase):
    maxDiff = None
    group_admin = GroupAdmin()

    # ============================================================================
    # Group Special Authority
    # ============================================================================
    def test_group_admin_has_group_special_authority_returns_true_when_group_special(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertTrue(
            self.group_admin.has_group_special_authority("testgrp0", "ESWIFT")
        )

    def test_group_admin_has_group_special_authority_returns_false_when_not_group_special(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertFalse(
            self.group_admin.has_group_special_authority("testgrp0", "ESWIFT")
        )

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_has_group_special_authority_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.group_admin.has_group_special_authority("testgrp0", "ESWIFT")

    # ============================================================================
    # Group Operations Authority
    # ============================================================================
    def test_group_admin_has_group_operations_authority_returns_true_when_group_operations(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertTrue(
            self.group_admin.has_group_operations_authority("testgrp0", "LEONARD")
        )

    def test_group_admin_has_group_operations_authority_returns_false_when_not_group_operations(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertFalse(
            self.group_admin.has_group_operations_authority("testgrp0", "LEONARD")
        )

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_has_group_operations_authority_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.group_admin.has_group_operations_authority("testgrp0", "LEONARD")

    # ============================================================================
    # Group Auditor Authority
    # ============================================================================
    def test_group_admin_has_group_auditor_authority_returns_true_when_group_auditor(
        self,
        call_racf_mock: Mock,
    ):
        group_extract_auditor = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML
        )
        group_extract_auditor = group_extract_auditor.replace(
            "<message>         CONNECT ATTRIBUTES=SPECIAL</message>",
            "<message>         CONNECT ATTRIBUTES=AUDITOR</message>",
        )
        call_racf_mock.return_value = group_extract_auditor
        self.assertTrue(
            self.group_admin.has_group_auditor_authority("testgrp0", "ESWIFT")
        )

    def test_group_admin_has_group_auditor_authority_returns_false_when_not_group_auditor(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertFalse(
            self.group_admin.has_group_auditor_authority("testgrp0", "ESWIFT")
        )

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_has_group_auditor_authority_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.group_admin.has_group_auditor_authority("testgrp0", "ESWIFT")

    # ============================================================================
    # Group Access Attribute
    # ============================================================================
    def test_group_admin_has_group_access_attribute_returns_true_when_grpacc(
        self,
        call_racf_mock: Mock,
    ):
        group_extract_grpacc = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML
        )
        group_extract_grpacc = group_extract_grpacc.replace(
            "<message>         CONNECT ATTRIBUTES=OPERATIONS</message>",
            "<message>         CONNECT ATTRIBUTES=GRPACC</message>",
        )
        call_racf_mock.return_value = group_extract_grpacc
        self.assertTrue(
            self.group_admin.has_group_access_attribute("testgrp0", "LEONARD")
        )

    def test_group_admin_has_group_access_attribute_returns_false_when_not_grpacc(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertFalse(
            self.group_admin.has_group_access_attribute("testgrp0", "LEONARD")
        )

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_has_group_access_attribute_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.group_admin.has_group_access_attribute("testgrp0", "LEONARD")

    # ============================================================================
    # OMVS GID
    # ============================================================================
    def test_group_admin_get_omvs_gid_works(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(self.group_admin.get_omvs_gid("testgrp0"), 1234567)

    # Error in environment, SQUIDWRD already deleted/not added
    def test_group_admin_get_omvs_gid_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.group_admin.get_omvs_gid("testgrp0"), 1234567

    def test_group_admin_get_omvs_gid_returns_none_when_no_omvs_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.group_admin.get_omvs_gid("testgrp0"))

    # ============================================================================
    # OVM GID
    # ============================================================================
    def test_group_admin_get_ovm_gid_works(
        self,
        call_racf_mock: Mock,
    ):
        group_extract_ovm_gid = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        group_extract_ovm_gid = group_extract_ovm_gid.replace(
            "<message>OMVS INFORMATION</message>", "<message>OVM INFORMATION</message>"
        )
        call_racf_mock.return_value = group_extract_ovm_gid
        self.assertEqual(self.group_admin.get_ovm_gid("testgrp0"), 1234567)

    # Error in environment, SQUIDWRD already deleted/not added
    def test_group_admin_get_ovm_gid_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            self.group_admin.get_ovm_gid("testgrp0"), 1234567

    def test_group_admin_get_ovm_gid_returns_none_when_no_ovm_segment_exists(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertIsNone(self.group_admin.get_ovm_gid("testgrp0"))
