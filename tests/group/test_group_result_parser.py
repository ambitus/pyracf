"""Test group result parser."""

import copy
import unittest
from unittest.mock import Mock, patch

import __init__

import tests.group.test_group_constants as TestGroupConstants
from pyracf import (
    AddOperationError,
    AlterOperationError,
    DownstreamFatalError,
    GroupAdmin,
    SecurityRequestError,
)

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestGroupResultParser(unittest.TestCase):
    maxDiff = None
    group_admin = GroupAdmin()

    # ============================================================================
    # Add Group
    # ============================================================================
    def test_group_admin_can_parse_add_group_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_ERROR_XML,
            TestGroupConstants.TEST_ADD_GROUP_RESULT_SUCCESS_XML,
        ]
        self.assertEqual(
            self.group_admin.add(
                "TESTGRP0", traits=TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS
            ),
            TestGroupConstants.TEST_ADD_GROUP_RESULT_SUCCESS_DICTIONARY,
        )

    def test_group_admin_throws_error_on_add_existing_group(
        self,
        call_racf_mock: Mock,
    ):
        group_name = "TESTGRP0"
        call_racf_mock.side_effect = [
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML,
            TestGroupConstants.TEST_ADD_GROUP_RESULT_SUCCESS_XML,
        ]
        with self.assertRaises(AddOperationError) as exception:
            self.group_admin.add(
                group_name, traits=TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS
            )
        self.assertEqual(
            exception.exception.message,
            "Refusing to make security request to IRRSMO00."
            + "\n\nTarget profile "
            + f"'{group_name}' already exists as a '{self.group_admin._profile_type}' profile.",
        )

    def test_group_admin_add_surfaces_error_from_preliminary_extract(
        self,
        call_racf_mock: Mock,
    ):
        group_name = "TESTGRP0"
        extract_group_error_xml = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_ERROR_XML
        )
        extract_group_error_xml = extract_group_error_xml.replace(
            "<message>ICH51003I NAME NOT FOUND IN RACF DATA SET</message>",
            "<message>ICH32004I NOT AUTHORIZED TO ISSUE LISTGRP</message>",
        )
        call_racf_mock.side_effect = [
            extract_group_error_xml,
            TestGroupConstants.TEST_ADD_GROUP_RESULT_SUCCESS_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            self.group_admin.add(
                group_name, traits=TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS
            )
        extract_group_error_json = copy.deepcopy(
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_ERROR_DICTIONARY
        )
        extract_group_error_json["securityResult"]["group"]["commands"][0][
            "messages"
        ] = ["ICH32004I NOT AUTHORIZED TO ISSUE LISTGRP"]
        self.assertEqual(
            exception.exception.result,
            extract_group_error_json,
        )

    # Error in command, TESTGRPP0 is bad GROUP
    def test_group_admin_can_parse_add_group_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BAD_ATTRIBUTE_ERROR_XML,
            TestGroupConstants.TEST_ADD_GROUP_RESULT_ERROR_XML,
        ]
        with self.assertRaises(DownstreamFatalError) as exception:
            self.group_admin.add(
                "TESTGRPP0", traits=TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS
            )
        self.assertEqual(
            exception.exception.result,
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BAD_ATTRIBUTE_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Alter Group
    # ============================================================================
    def test_group_admin_can_parse_alter_group_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML,
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_SUCCESS_XML,
        ]
        self.assertEqual(
            self.group_admin.alter(
                "TESTGRP0", traits=TestGroupConstants.TEST_ALTER_GROUP_REQUEST_TRAITS
            ),
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_SUCCESS_DICTIONARY,
        )

    def test_group_admin_throws_error_on_alter_new_group(
        self,
        call_racf_mock: Mock,
    ):
        group_name = "TESTGRP0"
        call_racf_mock.side_effect = [
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML,
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_SUCCESS_XML,
        ]
        with self.assertRaises(AlterOperationError) as exception:
            self.group_admin.alter(
                group_name, traits=TestGroupConstants.TEST_ALTER_GROUP_REQUEST_TRAITS
            )
        self.assertEqual(
            exception.exception.message,
            "Refusing to make security request to IRRSMO00."
            + "\n\nTarget profile "
            + f"'{group_name}' does not exist as a '{self.group_admin._profile_type}' profile.",
        )

    # Error: bad gid "3000000000"
    def test_group_admin_can_parse_alter_group_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.side_effect = [
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML,
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_ERROR_XML,
        ]
        with self.assertRaises(SecurityRequestError) as exception:
            self.group_admin.alter(
                "TESTGRP0",
                traits=TestGroupConstants.TEST_ALTER_GROUP_REQUEST_ERROR_TRAITS,
            )
        self.assertEqual(
            exception.exception.result,
            TestGroupConstants.TEST_ALTER_GROUP_RESULT_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Extract Group
    # ============================================================================
    def test_group_admin_can_parse_extract_group_base_omvs_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_XML
        )
        self.assertEqual(
            self.group_admin.extract("TESTGRP0", segments=["omvs"]),
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_SUCCESS_DICTIONARY,
        )

    def test_group_admin_can_parse_extract_group_base_only_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_XML
        )
        self.assertEqual(
            self.group_admin.extract("TESTGRP0"),
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_ONLY_SUCCESS_JSON,
        )

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_can_parse_extract_group_base_omvs_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.group_admin.extract("TESTGRP0", segments=["omvs"])
        self.assertEqual(
            exception.exception.result,
            TestGroupConstants.TEST_EXTRACT_GROUP_RESULT_BASE_OMVS_ERROR_DICTIONARY,
        )

    # ============================================================================
    # Delete Group
    # ============================================================================
    def test_group_admin_can_parse_delete_group_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_DELETE_GROUP_RESULT_SUCCESS_XML
        )
        self.assertEqual(
            self.group_admin.delete("TESTGRP0"),
            TestGroupConstants.TEST_DELETE_GROUP_RESULT_SUCCESS_DICTIONARY,
        )

    # Error in environment, TESTGRP0 already deleted/not added
    def test_group_admin_can_parse_delete_group_error_xml(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestGroupConstants.TEST_DELETE_GROUP_RESULT_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError) as exception:
            self.group_admin.delete("TESTGRP0")
        self.assertEqual(
            exception.exception.result,
            TestGroupConstants.TEST_DELETE_GROUP_RESULT_ERROR_DICTIONARY,
        )
