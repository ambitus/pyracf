"""Test group request builder."""

import unittest

import __init__

import tests.group.test_group_constants as TestGroupConstants
from pyracf import GroupAdmin

# Resolves F401
__init__


class TestGroupRequestBuilder(unittest.TestCase):
    maxDiff = None
    group_admin = GroupAdmin(generate_requests_only=True)

    def test_group_admin_build_add_group_request(self):
        result = self.group_admin.add(
            "TESTGRP0", traits=TestGroupConstants.TEST_ADD_GROUP_REQUEST_TRAITS
        )
        self.assertEqual(result, TestGroupConstants.TEST_ADD_GROUP_REQUEST_XML)

    def test_group_admin_build_alter_group_request(self):
        result = self.group_admin.alter(
            "TESTGRP0", traits=TestGroupConstants.TEST_ALTER_GROUP_REQUEST_TRAITS
        )
        self.assertEqual(result, TestGroupConstants.TEST_ALTER_GROUP_REQUEST_XML)

    def test_group_admin_build_extract_group_request_base_omvs(self):
        result = self.group_admin.extract("TESTGRP0", segments=["omvs"])
        self.assertEqual(
            result, TestGroupConstants.TEST_EXTRACT_GROUP_REQUEST_BASE_OMVS_XML
        )

    def test_group_admin_build_delete_group_request(self):
        result = self.group_admin.delete("TESTGRP0")
        self.assertEqual(result, TestGroupConstants.TEST_DELETE_GROUP_REQUEST_XML)
