"""Test connection setter functions."""

import unittest

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin

# Resolves F401
__init__


class TestConnectionSetters(unittest.TestCase):
    maxDiff = None
    connection_admin = ConnectionAdmin(generate_requests_only=True)

    # ============================================================================
    # Group Special Authority
    # ============================================================================
    def test_connection_admin_build_give_group_special_request(self):
        result = self.connection_admin.give_group_special_authority(
            "ESWIFT", "testgrp0"
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_GIVE_GROUP_SPECIAL_AUTHORITY
        )

    def test_connection_admin_build_take_away_group_special_authority_request(self):
        result = self.connection_admin.take_away_group_special_authority(
            "ESWIFT", "testgrp0"
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
            "ESWIFT", "testgrp0"
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_GIVE_GROUP_AUDITOR_AUTHORITY
        )

    def test_connection_admin_build_take_away_group_auditor_authority_request(self):
        result = self.connection_admin.take_away_group_auditor_authority(
            "ESWIFT", "testgrp0"
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
            "ESWIFT", "testgrp0"
        )
        self.assertEqual(
            result,
            TestConnectionConstants.TEST_CONNECTION_GIVE_GROUP_OPERATIONS_AUTHORITY,
        )

    def test_connection_admin_build_take_away_group_operations_authority_request(self):
        result = self.connection_admin.take_away_group_operations_authority(
            "ESWIFT", "testgrp0"
        )
        self.assertEqual(
            result,
            TestConnectionConstants.TEST_CONNECTION_TAKE_AWAY_GROUP_OPERATIONS_AUTHORITY,
        )

    # ============================================================================
    # Group Access Attribute
    # ============================================================================
    def test_connection_admin_build_give_group_access_attribute_request(self):
        result = self.connection_admin.give_group_access_attribute("ESWIFT", "testgrp0")
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_SET_GROUP_ACCESS_ATTRIBUTE
        )

    def test_connection_admin_build_take_away_group_access_attribute(self):
        result = self.connection_admin.take_away_group_access_attribute(
            "ESWIFT", "testgrp0"
        )
        self.assertEqual(
            result,
            TestConnectionConstants.TEST_CONNECTION_REMOVE_GROUP_ACCESS_ATTRIBUTE,
        )
