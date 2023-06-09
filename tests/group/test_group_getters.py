"""Test group getter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.group.test_group_constants as TestGroupConstants
from pyracf import GroupAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestGroupGetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> GroupAdmin:
        irrsmo00_init_mock.return_value = None
        return GroupAdmin()

    # ============================================================================
    # Group Special Authority
    # ============================================================================
    def test_group_admin_has_group_special_authority_returns_true_when_group_special(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertTrue(group_admin.has_group_special_authority("TESTGRP0", "ESWIFT"))

    def test_group_admin_has_group_special_authority_returns_false_when_not_group_special(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertFalse(group_admin.has_group_special_authority("TESTGRP0", "ESWIFT"))

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_has_group_special_authority_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            group_admin.has_group_special_authority("TESTGRP0", "ESWIFT")

    # ============================================================================
    # Group Operations Authority
    # ============================================================================
    def test_group_admin_has_group_operations_authority_returns_true_when_group_operations(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertTrue(
            group_admin.has_group_operations_authority("TESTGRP0", "LEONARD")
        )

    def test_group_admin_has_group_operations_authority_returns_false_when_not_group_operations(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertFalse(
            group_admin.has_group_operations_authority("TESTGRP0", "LEONARD")
        )

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_has_group_operations_authority_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            group_admin.has_group_operations_authority("TESTGRP0", "LEONARD")

    # ============================================================================
    # Group Auditor Authority
    # ============================================================================
    def test_group_admin_has_group_auditor_authority_returns_true_when_group_auditor(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        group_extract_auditor = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        group_extract_auditor = group_extract_auditor.replace(
            "<message>         CONNECT ATTRIBUTES=SPECIAL</message>",
            "<message>         CONNECT ATTRIBUTES=AUDITOR</message>",
        )
        call_racf_mock.return_value = group_extract_auditor
        self.assertTrue(group_admin.has_group_auditor_authority("TESTGRP0", "ESWIFT"))

    def test_group_admin_has_group_auditor_authority_returns_false_when_not_group_auditor(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertFalse(group_admin.has_group_auditor_authority("TESTGRP0", "ESWIFT"))

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_has_group_auditor_authority_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            group_admin.has_group_auditor_authority("TESTGRP0", "ESWIFT")

    # ============================================================================
    # Group Access Attribute
    # ============================================================================
    def test_group_admin_has_group_access_attribute_returns_true_when_grpacc(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        group_extract_grpacc = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        group_extract_grpacc = group_extract_grpacc.replace(
            "<message>         CONNECT ATTRIBUTES=OPERATIONS</message>",
            "<message>         CONNECT ATTRIBUTES=GRPACC</message>",
        )
        call_racf_mock.return_value = group_extract_grpacc
        self.assertTrue(group_admin.has_group_access_attribute("TESTGRP0", "LEONARD"))

    def test_group_admin_has_group_access_attribute_returns_false_when_not_grpacc(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertFalse(group_admin.has_group_access_attribute("TESTGRP0", "LEONARD"))

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_has_group_access_attribute_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            group_admin.has_group_access_attribute("TESTGRP0", "LEONARD")

    # ============================================================================
    # OMVS GID
    # ============================================================================
    def test_group_admin_get_omvs_gid_works(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(group_admin.get_omvs_gid("TESTGRP0"), 1234567)

    # Error in environment, SQUIDWRD already deleted/not added
    def test_group_admin_get_omvs_gid_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            group_admin.get_omvs_gid("TESTGRP0"), 1234567

    def test_group_admin_get_omvs_gid_returns_none_when_no_omvs_segment_exists(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertIsNone(group_admin.get_omvs_gid("TESTGRP0"))

    # ============================================================================
    # OVM GID
    # ============================================================================
    def test_group_admin_get_ovm_gid_works(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        group_extract_ovm_gid = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        group_extract_ovm_gid = group_extract_ovm_gid.replace(
            "<message>OMVS INFORMATION</message>", "<message>OVM INFORMATION</message>"
        )
        call_racf_mock.return_value = group_extract_ovm_gid
        self.assertEqual(group_admin.get_ovm_gid("TESTGRP0"), 1234567)

    # Error in environment, SQUIDWRD already deleted/not added
    def test_group_admin_get_ovm_gid_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            group_admin.get_ovm_gid("TESTGRP0"), 1234567

    def test_group_admin_get_ovm_gid_returns_none_when_no_ovm_segment_exists(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_NO_OMVS_SUCCESS_XML
        )
        self.assertIsNone(group_admin.get_ovm_gid("TESTGRP0"))
