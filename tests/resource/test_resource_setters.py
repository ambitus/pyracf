"""Test general resource profile setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestResourceSetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ResourceAdmin:
        irrsmo00_init_mock.return_value = None
        return ResourceAdmin(generate_requests_only=True)

    def test_resource_admin_build_set_universal_access_request(
        self, irrsmo00_init_mock: Mock
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        result = resource_admin.set_universal_access("TESTING", "ELIJTEST", "ALTER")
        self.assertEqual(
            result, TestResourceConstants.TEST_RESOURCE_SET_UNIVERSAL_ACCESS_XML
        )
