"""Test access request builder."""

import unittest
from unittest.mock import Mock

import __init__

import tests.access.test_access_constants as TestAccessConstants
from pyracf import AccessAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestAccessRequestBuilder(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    access_admin = AccessAdmin(generate_requests_only=True)

    def test_access_admin_build_alter_access_request(self):
        result = self.access_admin.alter(
            "TESTING", "ELIJTEST", "ESWIFT", traits={"base:access": "NONE"}
        )
        self.assertEqual(result, TestAccessConstants.TEST_ALTER_ACCESS_REQUEST_XML)

    def test_access_admin_build_delete_access_request(self):
        result = self.access_admin.delete("TESTING", "ELIJTEST", "ESWIFT")
        self.assertEqual(result, TestAccessConstants.TEST_DELETE_ACCESS_REQUEST_XML)
