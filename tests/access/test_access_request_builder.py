"""Test access request builder."""

import unittest

import __init__

import tests.access.test_access_constants as TestAccessConstants
from pyracf import AccessAdmin

# Resolves F401
__init__


class TestAccessRequestBuilder(unittest.TestCase):
    maxDiff = None
    access_admin = AccessAdmin(generate_requests_only=True)

    def test_access_admin_build_permit_access_request(self):
        result = self.access_admin.permit(
            "TESTING", "ELIJTEST", "ESWIFT", traits={"base:access": "NONE"}
        )
        self.assertEqual(result, TestAccessConstants.TEST_PERMIT_ACCESS_REQUEST_XML)

    def test_access_admin_build_delete_access_request(self):
        result = self.access_admin.delete("TESTING", "ELIJTEST", "ESWIFT")
        self.assertEqual(result, TestAccessConstants.TEST_DELETE_ACCESS_REQUEST_XML)
