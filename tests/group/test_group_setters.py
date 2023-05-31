"""Test group setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.group.test_group_constants as TestGroupConstants
from pyracf import GroupAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestGroupSetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> GroupAdmin:
        irrsmo00_init_mock.return_value = None
        return GroupAdmin()

    def test_group_admin_build_set_ovm_gid_request(self, irrsmo00_init_mock: Mock):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        result = group_admin.set_ovm_gid("ESWIFT", "TESTGRP0", generate_request_only=True)
        self.assertEqual(result, TestGroupConstants.TEST_GROUP_SET_OVM_GID_XML)

    def test_group_admin_build_set_omvs_gid_request(self, irrsmo00_init_mock: Mock):
        group_admin = self.boilerplate(irrsmo00_init_mock)
        result = group_admin.set_omvs_gid("ESWIFT", "TESTGRP0", generate_request_only=True)
        self.assertEqual(result, TestGroupConstants.TEST_GROUP_SET_OMVS_GID_XML)