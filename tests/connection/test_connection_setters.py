"""Test connection setter functions."""

import unittest
from unittest.mock import Mock

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestConnectionSetters(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    connection_admin = ConnectionAdmin(generate_requests_only=True)

    # ============================================================================
    # Group Special Authority
    # ============================================================================
    def test_connection_admin_build_give_group_special_request(self):
        result = self.connection_admin.give_group_special_authority(
            "ESWIFT", "TESTGRP0"
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_GIVE_GROUP_SPECIAL_AUTHORITY
        )

    def test_connection_admin_build_take_away_group_special_authority_request(self):
        result = self.connection_admin.take_away_group_special_authority(
            "ESWIFT", "TESTGRP0"
        )
        self.assertEqual(
            result,
            TestConnectionConstants.TEST_CONNECTION_TAKE_AWAY_GROUP_SPECIAL_AUTHORITY,
        )

    # ============================================================================
    # Group Auditor Authority
    # ============================================================================
    def test_connection_admin_build_give_group_auditor_authority_request(self):
        result = self.connection_admin.give_group_auditor_authority(
            "ESWIFT", "TESTGRP0"
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_GIVE_GROUP_AUDITOR_AUTHORITY
        )

    def test_connection_admin_build_take_away_group_auditor_authority_request(self):
        result = self.connection_admin.take_away_group_auditor_authority(
            "ESWIFT", "TESTGRP0"
        )
        self.assertEqual(
            result,
            TestConnectionConstants.TEST_CONNECTION_TAKE_AWAY_GROUP_AUDITOR_AUTHORITY,
        )

    # ============================================================================
    # Group Operations Authority
    # ============================================================================
    def test_connection_admin_build_give_group_operations_authority_request(self):
        result = self.connection_admin.give_group_operations_authority(
            "ESWIFT", "TESTGRP0"
        )
        self.assertEqual(
            result,
            TestConnectionConstants.TEST_CONNECTION_GIVE_GROUP_OPERATIONS_AUTHORITY,
        )

    def test_connection_admin_build_take_away_group_operations_authority_request(self):
        result = self.connection_admin.take_away_group_operations_authority(
            "ESWIFT", "TESTGRP0"
        )
        self.assertEqual(
            result,
            TestConnectionConstants.TEST_CONNECTION_TAKE_AWAY_GROUP_OPERATIONS_AUTHORITY,
        )

    # ============================================================================
    # Group Access Attribute
    # ============================================================================
    def test_connection_admin_build_give_group_access_attribute_request(self):
        result = self.connection_admin.give_group_access_attribute("ESWIFT", "TESTGRP0")
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_SET_GROUP_ACCESS_ATTRIBUTE
        )

    def test_connection_admin_build_take_away_group_access_attribute(self):
        result = self.connection_admin.take_away_group_access_attribute(
            "ESWIFT", "TESTGRP0"
        )
        self.assertEqual(
            result,
            TestConnectionConstants.TEST_CONNECTION_REMOVE_GROUP_ACCESS_ATTRIBUTE,
        )
