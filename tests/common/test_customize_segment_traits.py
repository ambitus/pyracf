"""Test customizing security admin segment traits."""

import unittest
from unittest.mock import Mock, patch

import __init__

import tests.common.test_common_constants as TestCommonConstants
from pyracf import UserAdmin
from pyracf.common.irrsmo00 import IRRSMO00

# Resolves F401
__init__


class TestCustomizeSegmentTraits(unittest.TestCase):
    maxDiff = None
    IRRSMO00.__init__ = Mock(return_value=None)

    # ============================================================================
    # Customize Segment Traits Request Generation
    # ============================================================================
    def test_user_admin_build_alter_request_replace_existing_segment_traits(self):
        user_admin = UserAdmin(
            generate_requests_only=True,
            replace_existing_segment_traits=TestCommonConstants.TEST_USER_REPLACE_SEGMENT_TRAITS,
        )
        result = user_admin.alter(
            "squidwrd", traits=TestCommonConstants.TEST_ALTER_USER_CSDATA_REQUEST_TRAITS
        )
        self.assertEqual(
            result, TestCommonConstants.TEST_ALTER_USER_REQUEST_REPLACE_SEGMENTS_XML
        )

    def test_user_admin_build_alter_request_update_existing_segment_traits(self):
        user_admin = UserAdmin(
            generate_requests_only=True,
            update_existing_segment_traits=TestCommonConstants.TEST_USER_ADDITIONAL_SEGMENT_TRAITS,
        )
        result = user_admin.alter(
            "squidwrd",
            traits=TestCommonConstants.TEST_ALTER_USER_CSDATA_AND_OMVS_REQUEST_TRAITS,
        )
        self.assertEqual(
            result,
            TestCommonConstants.TEST_ALTER_USER_REQUEST_UPDATE_SEGMENTS_XML,
        )

    # ============================================================================
    # Customize Segment Traits Result Parsing
    # ============================================================================
    @patch("pyracf.common.irrsmo00.IRRSMO00.call_racf")
    def test_user_admin_can_parse_extract_user_base_omvs_csdata_success_xml(
        self,
        call_racf_mock: Mock,
    ):
        user_admin = UserAdmin(
            update_existing_segment_traits=TestCommonConstants.TEST_USER_REPLACE_SEGMENT_TRAITS
        )
        call_racf_mock.return_value = (
            TestCommonConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_CSDATA_SUCCESS_XML
        )
        self.assertEqual(
            user_admin.extract("squidwrd", segments=["omvs", "csdata"]),
            TestCommonConstants.TEST_EXTRACT_USER_RESULT_BASE_OMVS_CSDATA_SUCCESS_DICTIONARY,
        )
