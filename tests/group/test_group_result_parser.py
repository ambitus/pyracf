"""Test group result parser."""

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
class TestGroupResultParser(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> GroupAdmin:
        irrsmo00_init_mock.return_value = None
        return GroupAdmin()

    # ============================================================================
    # Add Group
    # ============================================================================
    def test_group_admin_can_parse_add_group_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_ADD_GROUP_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            group_admin.add(
                "TESTGRP0", traits=TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS
            ),
            TestGroupConstants.TEST_ADD_GROUP_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTGRP0 already added/exists
    def test_group_admin_can_parse_add_group_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = TestGroupConstants.TEST_ADD_GROUP_RESULT_ERROR_XML
        with self.assertRaises(SecurityRequestError) as exception:
            group_admin.add(
                "TESTGRP0", traits=TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS
            )
        self.assertEqual(
            exception.exception.results,
            TestGroupConstants.TEST_ADD_GROUP_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter Group
    # ============================================================================
    def test_group_admin_can_parse_alter_group_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            group_admin.alter(
                "TESTGRP0", traits=TestGroupConstants.TEST_ALTER_GROUP_REQUEST_TRAITS
            ),
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_SUCCESS_DICTIONARY,
        )

    # Error: invalid gid "3000000000"
    def test_group_admin_can_parse_alter_group_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            group_admin.alter(
                group_admin.alter(
                    "TESTGRP0",
                    traits=TestGroupConstants.TEST_ALTER_GROUP_REQUEST_ERROR_TRAITS,
                )
            )
        self.assertEqual(
            exception.exception.results,
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Extract Group
    # ============================================================================
    def test_group_admin_can_parse_extract_group_base_omvs_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(
            group_admin.extract(
                "TESTGRP0",
                segments=TestGroupConstants.TEST_EXTRACT_GROUP_REQUEST_BASE_OMVS_TRAITS,
            ),
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_can_parse_extract_group_base_omvs_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            group_admin.extract(
                "TESTGRP0",
                segments=TestGroupConstants.TEST_EXTRACT_GROUP_REQUEST_BASE_OMVS_TRAITS,
            )
        self.assertEqual(
            exception.exception.results,
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Group
    # ============================================================================
    def test_group_admin_can_parse_delete_group_success_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_DELETE_GROUP_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            group_admin.delete("TESTGRP0"),
            TestGroupConstants.TEST_DELETE_GROUP_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_can_parse_delete_group_error_xml(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_DELETE_GROUP_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            group_admin.delete("TESTGRP0")
        self.assertEqual(
            exception.exception.results,
            TestGroupConstants.TEST_DELETE_GROUP_RESULT_ERROR_DICTIONARY,
        )
