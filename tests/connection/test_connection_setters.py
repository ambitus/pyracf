"""Test connection setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.connection.test_connection_constants as TestConnectionConstants
from pyracf import ConnectionAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestConnectionSetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ConnectionAdmin:
        irrsmo00_init_mock.return_value = None
        return ConnectionAdmin()

    def test_connection_admin_build_set_group_special(self, irrsmo00_init_mock: Mock):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.set_group_special(
            "ESWIFT", "TESTGRP0", generate_request_only=True
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_SET_GROUP_SPECIAL
        )

    def test_connection_admin_build_del_group_special(self, irrsmo00_init_mock: Mock):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.del_group_special(
            "ESWIFT", "TESTGRP0", generate_request_only=True
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_DEL_GROUP_SPECIAL
        )

    def test_connection_admin_build_set_group_auditor(self, irrsmo00_init_mock: Mock):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.set_group_auditor(
            "ESWIFT", "TESTGRP0", generate_request_only=True
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_SET_GROUP_AUDITOR
        )

    def test_connection_admin_build_del_group_auditor(self, irrsmo00_init_mock: Mock):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.del_group_auditor(
            "ESWIFT", "TESTGRP0", generate_request_only=True
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_DEL_GROUP_AUDITOR
        )

    def test_connection_admin_build_set_group_operations(
        self, irrsmo00_init_mock: Mock
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.set_group_operations(
            "ESWIFT", "TESTGRP0", generate_request_only=True
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_SET_GROUP_OPERATIONS
        )

    def test_connection_admin_build_del_group_operations(
        self, irrsmo00_init_mock: Mock
    ):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.del_group_operations(
            "ESWIFT", "TESTGRP0", generate_request_only=True
        )
        self.assertEqual(
            result, TestConnectionConstants.TEST_CONNECTION_DEL_GROUP_OPERATIONS
        )

    def test_connection_admin_build_set_grpacc(self, irrsmo00_init_mock: Mock):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.set_grpacc(
            "ESWIFT", "TESTGRP0", generate_request_only=True
        )
        self.assertEqual(result, TestConnectionConstants.TEST_CONNECTION_SET_GRPACC)

    def test_connection_admin_build_del_grpacc(self, irrsmo00_init_mock: Mock):
        connection_admin = self.boilerplate(irrsmo00_init_mock)
        result = connection_admin.del_grpacc(
            "ESWIFT", "TESTGRP0", generate_request_only=True
        )
        self.assertEqual(result, TestConnectionConstants.TEST_CONNECTION_DEL_GRPACC)
