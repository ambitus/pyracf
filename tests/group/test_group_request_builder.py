"""Test group request builder."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.group.test_group_constants as TestGroupConstants
from pyracf import GroupAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestGroupRequestBuilder(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> GroupAdmin:
        irrsmo00_init_mock.return_value = None
        return GroupAdmin()

    def test_group_admin_build_add_group_request(self, irrsmo00_init_mock: Mock):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        result = group_admin.add(
            TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS, generate_request_only=True
        )
        self.assertEqual(result, TestGroupConstants.TEST_ADD_GROUP_REQUEST_XML)

    def test_group_admin_build_alter_group_request(self, irrsmo00_init_mock: Mock):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        result = group_admin.alter(
            TestGroupConstants.TEST_ALTER_GROUP_REQUEST_TRAITS, generate_request_only=True
        )
        self.assertEqual(result, TestGroupConstants.TEST_ALTER_GROUP_REQUEST_XML)

    def test_group_admin_build_extract_group_request_base_omvs(
        self, irrsmo00_init_mock: Mock
    ):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        result = group_admin.extract(
            TestGroupConstants.TEST_EXTRACT_GROUP_REQUEST_BASE_OMVS_TRAITS,
            generate_request_only=True,
        )
        self.assertEqual(
            result, TestGroupConstants.TEST_EXTRACT_GROUP_REQUEST_BASE_OMVS_XML
        )

    def test_group_admin_build_delete_group_request(self, irrsmo00_init_mock: Mock):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        result = group_admin.delete("TESTGRP0", generate_request_only=True)
        self.assertEqual(result, TestGroupConstants.TEST_DELETE_GROUP_REQUEST_XML)
