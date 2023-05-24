"""Test genprof setter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.genprof.test_genprof_constants as TestGenprofConstants
from pyracf import ResourceAdmin

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestGenprofSetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ResourceAdmin:
        irrsmo00_init_mock.return_value = None
        return ResourceAdmin(generate_requests_only=True)

    def test_resource_admin_build_set_uacc_request(self, irrsmo00_init_mock: Mock):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        result = resource_admin.set_uacc("TESTING", "ELIJTEST", "ALTER")
        self.assertEqual(result, TestGenprofConstants.TEST_GENPROF_SET_UACC_XML)
