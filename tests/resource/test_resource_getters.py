"""Test general resource profile getter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin
from pyracf.common.security_request_error import SecurityRequestError

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
@patch("pyracf.common.irrsmo00.IRRSMO00.__init__")
class TestResourceGetters(unittest.TestCase):
    maxDiff = None

    def boilerplate(self, irrsmo00_init_mock: Mock) -> ResourceAdmin:
        irrsmo00_init_mock.return_value = None
        return ResourceAdmin()

    # ============================================================================
    # Universal Access
    # ============================================================================
    def test_resource_admin_get_universal_access_returns_valid_when_read(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertTrue(
            resource_admin.get_universal_access("TESTING", "ELIJTEST").title() == "Read"
        )

    def test_resource_admin_get_universal_access_returns_valid_when_none(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        resource_extract_no_universal_access = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_no_universal_access = resource_extract_no_universal_access.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          NONE               READ    NO</message>",
        )
        call_racf_mock.return_value = resource_extract_no_universal_access
        self.assertTrue(
            resource_admin.get_universal_access("TESTING", "ELIJTEST") is None
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_get_universal_access_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            resource_admin.get_universal_access("TESTING", "ELIJTEST")

    def test_resource_admin_get_my_access_returns_valid_when_read(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertTrue(
            resource_admin.get_my_access("TESTING", "ELIJTEST").title() == "Read"
        )

    def test_resource_admin_get_my_access_returns_valid_when_none(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        resource_extract_no_your_access = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_no_your_access = resource_extract_no_your_access.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          READ               NONE    NO</message>",
        )
        call_racf_mock.return_value = resource_extract_no_your_access
        self.assertTrue(resource_admin.get_my_access("TESTING", "ELIJTEST") is None)

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_get_my_access_raises_an_exception_when_extract_fails(
        self,
        irrsmo00_init_mock: Mock,
        call_racf_mock: Mock,
    ):
        resource_admin = self.boilerplate(irrsmo00_init_mock)
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityRequestError):
            resource_admin.get_my_access("TESTING", "ELIJTEST")
