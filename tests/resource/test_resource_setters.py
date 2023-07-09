"""Test general resource profile setter functions."""

import unittest
from unittest.mock import Mock

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestResourceSetters(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    resource_admin = ResourceAdmin(generate_requests_only=True)

    def test_resource_admin_build_set_universal_access_request(self):
        result = self.resource_admin.set_universal_access(
            "TESTING", "ELIJTEST", "ALTER"
        )
        self.assertEqual(
            result, TestResourceConstants.TEST_RESOURCE_SET_UNIVERSAL_ACCESS_XML
        )
