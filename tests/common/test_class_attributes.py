import unittest
from unittest.mock import Mock, call, patch

from pyracf import (
    AccessAdmin,
    ConnectionAdmin,
    DataSetAdmin,
    GroupAdmin,
    ResourceAdmin,
    SetroptsAdmin,
    UserAdmin,
)
from pyracf.common.security_admin import SecurityAdmin


class TestClassAttributes(unittest.TestCase):
    maxDiff = None
    admin_types = [
        AccessAdmin,
        ConnectionAdmin,
        DataSetAdmin,
        GroupAdmin,
        ResourceAdmin,
        SetroptsAdmin,
        UserAdmin,
    ]

    def test_all_admin_types_support_irrsmo00_result_buffer_size(self):
        for admin_type in self.admin_types:
            admin_object = admin_type(irrsmo00_result_buffer_size=32768)
            self.assertEqual(
                admin_object.__dict__["_SecurityAdmin__irrsmo00"].__dict__[
                    "_IRRSMO00__result_buffer_size"
                ],
                32768,
            )
            admin_object = admin_type()
            self.assertEqual(
                admin_object.__dict__["_SecurityAdmin__irrsmo00"].__dict__[
                    "_IRRSMO00__result_buffer_size"
                ],
                16384,
            )

    def test_all_admin_types_raise_value_error_when_irrsmo00_result_buffer_size_is_no_good(
        self,
    ):
        for admin_type in self.admin_types:
            with self.assertRaises(ValueError) as exception:
                admin_type(irrsmo00_result_buffer_size=9999)
            self.assertEqual(
                str(exception.exception),
                "IRRSMO00 result buffer size must be an "
                + "integer value greater than or equal to '10000'.",
            )
            with self.assertRaises(ValueError) as exception:
                admin_type(irrsmo00_result_buffer_size="Plankton")
            self.assertEqual(
                str(exception.exception),
                "IRRSMO00 result buffer size must be an "
                + "integer value greater than or equal to '10000'.",
            )

    @patch("pyracf.common.utilities.logger.Logger.log_warning")
    def test_all_admin_type_log_a_warning_when_irrsmo00_result_buffer_size_is_very_large(
        self, log_warning_mock: Mock
    ):
        for admin_type in self.admin_types:
            admin_type(irrsmo00_result_buffer_size=100000001)
        log_warning_mock.assert_has_calls(
            [
                call(
                    "IRRSMO00 result buffer sizes greater than '100000000' may "
                    + "result in a 'SIGKILL' signal to be raised, which is NOT "
                    + "recoverable and will lead to the Python process that "
                    + "pyRACF is running under to be killed."
                )
            ]
            * len(self.admin_types)
        )

    def test_all_admin_types_support_debug(self):
        for admin_type in self.admin_types:
            admin_object = admin_type(debug=True)
            self.assertEqual(admin_object.__dict__["_SecurityAdmin__debug"], True)
            admin_object = admin_type()
            self.assertEqual(admin_object.__dict__["_SecurityAdmin__debug"], False)

    def test_all_admin_types_support_dump_mode(self):
        for admin_type in self.admin_types:
            admin_object = admin_type(dump_mode=True)
            self.assertEqual(admin_object.__dict__["_SecurityAdmin__dump_mode"], True)
            admin_object = admin_type()
            self.assertEqual(admin_object.__dict__["_SecurityAdmin__dump_mode"], False)

    def test_all_admin_types_support_generate_requests_only(self):
        for admin_type in self.admin_types:
            admin_object = admin_type(generate_requests_only=True)
            self.assertEqual(admin_object.__dict__["_generate_requests_only"], True)
            admin_object = admin_type()
            self.assertEqual(admin_object.__dict__["_generate_requests_only"], False)

    @patch.object(SecurityAdmin, "_SecurityAdmin__update_valid_segment_traits")
    def test_all_admin_types_support_update_existing_segment_traits(
        self,
        update_valid_segment_traits_mock: Mock,
    ):
        for admin_type in self.admin_types:
            admin_type(update_existing_segment_traits={"base": {"base:gary": "gary"}})
            admin_type()
        update_valid_segment_traits_mock.assert_has_calls(
            [call({"base": {"base:gary": "gary"}})] * len(self.admin_types)
        )

    @patch.object(SecurityAdmin, "_SecurityAdmin__replace_valid_segment_traits")
    def test_all_admin_types_support_replace_existing_segment_traits(
        self,
        replace_valid_segment_traits_mock: Mock,
    ):
        for admin_type in self.admin_types:
            admin_type(replace_existing_segment_traits={"base": {"base:gary": "gary"}})
            admin_type()
        replace_valid_segment_traits_mock.assert_has_calls(
            [call({"base": {"base:gary": "gary"}})] * len(self.admin_types)
        )

    @patch.object(SecurityAdmin, "_SecurityAdmin__add_additional_secret_traits")
    def test_all_admin_types_support_additional_secret_traits(
        self, add_additional_secret_traits_mock: Mock
    ):
        for admin_type in self.admin_types:
            admin_type(additional_secret_traits=["base:gary"])
            admin_type()
        add_additional_secret_traits_mock.assert_has_calls(
            [call(["base:gary"])] * len(self.admin_types)
        )

    def test_all_admin_types_support_run_as_userid(self):
        for admin_type in self.admin_types:
            admin_object = admin_type(run_as_userid="plankton")
            self.assertEqual(
                admin_object.__dict__["_SecurityAdmin__running_userid"], "PLANKTON"
            )
            admin_object = admin_type()
            self.assertEqual(
                admin_object.__dict__["_SecurityAdmin__running_userid"], None
            )
