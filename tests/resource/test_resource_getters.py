"""Test general resource profile getter functions."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.resource.test_resource_constants as TestResourceConstants
from pyracf import ResourceAdmin, SecurityResponseError
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


@patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
class TestResourceGetters(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)
    resource_admin = ResourceAdmin()

    # ============================================================================
    # Universal Access
    # ============================================================================
    def test_resource_admin_get_universal_access_returns_valid_when_read(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_universal_access("TESTING", "ELIJTEST"), "read"
        )

    def test_resource_admin_get_universal_access_returns_valid_when_none(
        self,
        call_racf_mock: Mock,
    ):
        resource_extract_no_universal_access = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_no_universal_access = resource_extract_no_universal_access.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          NONE               READ    NO</message>",
        )
        call_racf_mock.return_value = resource_extract_no_universal_access
        self.assertIsNone(
            self.resource_admin.get_universal_access("TESTING", "ELIJTEST")
        )

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_get_universal_access_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.resource_admin.get_universal_access("TESTING", "ELIJTEST")

    def test_resource_admin_get_my_access_returns_valid_when_read(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        self.assertEqual(
            self.resource_admin.get_my_access("TESTING", "ELIJTEST"), "read"
        )

    def test_resource_admin_get_my_access_returns_valid_when_none(
        self,
        call_racf_mock: Mock,
    ):
        resource_extract_no_your_access = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_SUCCESS_XML
        )
        resource_extract_no_your_access = resource_extract_no_your_access.replace(
            "<message> 00    ESWIFT          READ               READ    NO</message>",
            "<message> 00    ESWIFT          READ               NONE    NO</message>",
        )
        call_racf_mock.return_value = resource_extract_no_your_access
        self.assertIsNone(self.resource_admin.get_my_access("TESTING", "ELIJTEST"))

    # Error in environment, TESTING already deleted/not added
    def test_resource_admin_get_my_access_raises_an_exception_when_extract_fails(
        self,
        call_racf_mock: Mock,
    ):
        call_racf_mock.return_value = (
            TestResourceConstants.TEST_EXTRACT_RESOURCE_RESULT_BASE_ERROR_XML
        )
        with self.assertRaises(SecurityResponseError):
            self.resource_admin.get_my_access("TESTING", "ELIJTEST")
