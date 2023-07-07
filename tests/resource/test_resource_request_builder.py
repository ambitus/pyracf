"""Test general resource profile request builder."""

import unittest
from unittest.mock import Mock

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestResourceRequestBuilder(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    resource_admin = ResourceAdmin(generate_requests_only=True)

    def test_resource_admin_build_add_resource_request(self):
        result = self.resource_admin.add(
            "TESTING",
            "ELIJTEST",
            traits=TestResourceConstants.TEST_ADD_RESOURCE_REQUEST_TRAITS,
        )
        self.assertEqual(result, TestResourceConstants.TEST_ADD_RESOURCE_REQUEST_XML)

    def test_resource_admin_build_alter_resource_request(self):
        result = self.resource_admin.alter(
            "TESTING",
            "ELIJTEST",
            traits=TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_TRAITS,
        )
        self.assertEqual(result, TestResourceConstants.TEST_ALTER_RESOURCE_REQUEST_XML)

    def test_resource_admin_build_extract_resource_request_base(self):
        result = self.resource_admin.extract("TESTING", "ELIJTEST")
        self.assertEqual(
            result, TestResourceConstants.TEST_EXTRACT_RESOURCE_REQUEST_BASE_XML
        )

    def test_resource_admin_build_delete_resource_request(self):
        result = self.resource_admin.delete("TESTING", "ELIJTEST")
        self.assertEqual(result, TestResourceConstants.TEST_DELETE_RESOURCE_REQUEST_XML)
