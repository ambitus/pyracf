"""Test group setter functions."""

import unittest

import __init__

import tests.group.test_group_constants as TestGroupConstants
from pyracf import GroupAdmin

# Resolves F401
__init__


class TestGroupSetters(unittest.TestCase):
    maxDiff = None
    group_admin = GroupAdmin(generate_requests_only=True)

    def test_group_admin_build_set_ovm_gid_request(self):
        result = self.group_admin.set_ovm_gid("TESTGRP0", "1234567")
        self.assertEqual(result, TestGroupConstants.TEST_GROUP_SET_OVM_GID_XML)

    def test_group_admin_build_set_omvs_gid_request(self):
        result = self.group_admin.set_omvs_gid("TESTGRP0", "1234567")
        self.assertEqual(result, TestGroupConstants.TEST_GROUP_SET_OMVS_GID_XML)
