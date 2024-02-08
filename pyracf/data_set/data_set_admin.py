"""RACF Data Set Profile Administration."""

from typing import List, Union

from pyracf.common.exceptions.add_operation_error import AddOperationError
from pyracf.common.exceptions.alter_operation_error import AlterOperationError
from pyracf.common.exceptions.security_request_error import SecurityRequestError
from pyracf.common.security_admin import SecurityAdmin

from .data_set_request import DataSetRequest


class DataSetAdmin(SecurityAdmin):
    """RACF Data Set Profile Administration."""

    def __init__(
        self,
        irrsmo00_result_buffer_size: Union[int, None] = None,
        debug: bool = False,
        dump_mode: bool = False,
        generate_requests_only: bool = False,
        update_existing_segment_traits: Union[dict, None] = None,
        replace_existing_segment_traits: Union[dict, None] = None,
        additional_secret_traits: Union[List[str], None] = None,
        run_as_userid: Union[str, None] = None,
    ) -> None:
        self._valid_segment_traits = {
            "base": {
                "base:alter_volume": "racf:altvol",
                "base:audit_alter": "racf:audaltr",
                "base:audit_control": "racf:audcntl",
                "base:audit_none": "racf:audnone",
                "base:audit_read": "racf:audread",
                "base:audit_update": "racf:audupdt",
                "base:security_categories": "racf:category",
                "base:installation_data": "racf:data",
                "base:erase_data_sets_on_delete": "racf:erase",
                "base:model_profile_class": "racf:fclass",
                "base:model_profile_generic": "racf:fgeneric",
                "base:tape_data_set_file_sequence_number": "racf:fileseq",
                "base:model_profile": "racf:from",
                "base:model_profile_volume": "racf:fvolume",
                "base:global_audit_alter": "racf:gaudaltr",
                "base:global_audit_control": "racf:gaudcntl",
                "base:global_audit_none": "racf:gaudnone",
                "base:global_audit_read": "racf:gaudread",
                "base:global_audit_update": "racf:gaudupdt",
                "base:level": "racf:level",
                "base:data_set_model_profile": "racf:model",
                "base:notify_userid": "racf:notify",
                "base:owner": "racf:owner",
                "base:tape_data_set_security_retention_period": "racf:retpd",
                "base:security_label": "racf:seclabel",
                "base:security_level": "racf:seclevel",
                "base:generic_not_allowed": "racf:set",
                "base:generic_allowed": "racf:setonly",
                "base:use_tape_data_set_profile": "racf:tape",
                "base:universal_access": "racf:uacc",
                "base:data_set_allocation_unit": "racf:unit",
                "base:volumes": "racf:volume",
                "base:warn_on_insufficient_access": "racf:warning",
            },
            "dfp": {"dfp:owner": "racf:resowner", "dfp:ckds_data_key": "racf:datakey"},
            "tme": {"tme:roles": "racf:roles"},
        }
        self._valid_segment_traits["base"].update(
            self._common_base_traits_data_set_generic
        )
        del self._valid_segment_traits["base"]["base:generic"]
        super().__init__(
            "dataSet",
            irrsmo00_result_buffer_size=irrsmo00_result_buffer_size,
            debug=debug,
            dump_mode=dump_mode,
            generate_requests_only=generate_requests_only,
            update_existing_segment_traits=update_existing_segment_traits,
            replace_existing_segment_traits=replace_existing_segment_traits,
            additional_secret_traits=additional_secret_traits,
            run_as_userid=run_as_userid,
        )

    # ============================================================================
    # Access
    # ============================================================================
    def get_universal_access(self, data_set: str) -> Union[str, bytes, None]:
        """Get universal access for data set profile."""
        profile = self.extract(data_set, profile_only=True)
        return self._get_field(profile, "base", "universalAccess")

    def set_universal_access(
        self, data_set: str, universal_acccess: str
    ) -> Union[dict, bytes]:
        """Set the universal access for a data set profile."""
        result = self.alter(data_set, {"base:universal_access": universal_acccess})
        return self._to_steps(result)

    def get_my_access(self, data_set: str) -> Union[str, bytes, None]:
        """Get the access associated with your own data set profile."""
        profile = self.extract(data_set, profile_only=True)
        return self._get_field(profile, "base", "yourAccess")

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(
        self,
        data_set: str,
        traits: dict = {},
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> Union[dict, bytes]:
        """Create a new data set profile."""
        if self._generate_requests_only:
            self._build_segment_trait_dictionary(traits)
            data_set_request = DataSetRequest(data_set, "set", volume, generic)
            self._build_xml_segments(data_set_request)
            return self._make_request(data_set_request)
        try:
            profile = self.extract(
                data_set, volume=volume, generic=generic, profile_only=True
            )
            if self._get_field(profile, "base", "name") == data_set.lower():
                raise AddOperationError(data_set, self._profile_type)
        except SecurityRequestError as exception:
            if not exception.contains_error_message(self._profile_type, "ICH35003I"):
                raise exception
        self._build_segment_trait_dictionary(traits)
        data_set_request = DataSetRequest(data_set, "set", volume, generic)
        self._build_xml_segments(data_set_request)
        return self._make_request(data_set_request)

    def alter(
        self,
        data_set: str,
        traits: dict,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> Union[dict, bytes]:
        """Alter an existing data set profile."""
        if self._generate_requests_only:
            self._build_segment_trait_dictionary(traits)
            data_set_request = DataSetRequest(data_set, "set", volume, generic)
            self._build_xml_segments(data_set_request, alter=True)
            return self._make_request(data_set_request, irrsmo00_precheck=True)
        try:
            profile = self.extract(
                data_set, volume=volume, generic=generic, profile_only=True
            )
        except SecurityRequestError as exception:
            raise AlterOperationError(data_set, self._profile_type) from exception
        if not self._get_field(profile, "base", "name") == data_set.lower():
            raise AlterOperationError(data_set, self._profile_type)
        self._build_segment_trait_dictionary(traits)
        data_set_request = DataSetRequest(data_set, "set", volume, generic)
        self._build_xml_segments(data_set_request, alter=True)
        return self._make_request(data_set_request, irrsmo00_precheck=True)

    def extract(
        self,
        data_set: str,
        segments: List[str] = [],
        volume: Union[str, None] = None,
        generic: bool = False,
        profile_only: bool = False,
    ) -> Union[dict, bytes]:
        """Extract a data set profile."""
        self._build_segment_dictionary(segments)
        data_set_request = DataSetRequest(data_set, "listdata", volume, generic)
        self._build_xml_segments(data_set_request, extract=True)
        result = self._extract_and_check_result(data_set_request)
        if profile_only:
            return self._get_profile(result)
        return result

    def delete(
        self,
        data_set: str,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> Union[dict, bytes]:
        """Delete a data set profile."""
        data_set_request = DataSetRequest(data_set, "del", volume, generic)
        return self._make_request(data_set_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityResult"]["dataSet"]["commands"][0]["messages"]
        indexes = [
            i
            for i in range(len(messages) - 1)
            if messages[i] and "INFORMATION FOR DATASET " in messages[i]
        ]
        indexes.append(len(messages))
        profiles = []
        for i in range(len(indexes) - 1):
            profile = self._format_profile_generic(
                messages[indexes[i] : indexes[i + 1]]
            )
            # Post processing
            if "(g)" in profile["base"].get("name"):
                profile["base"]["generic"] = True
                profile["base"]["name"] = self._cast_from_str(
                    profile["base"].get("name").split(" ")[0]
                )
            else:
                profile["base"]["generic"] = False

            if profile["base"].get("installationData"):
                profile["base"]["installationData"] = " ".join(
                    profile["base"]["installationData"]
                )
            if profile["base"].get("notify") == [None, "user", "to", "be", "notified"]:
                profile["base"]["notify"] = None
            profiles.append(profile)

        del result["securityResult"]["dataSet"]["commands"][0]["messages"]
        result["securityResult"]["dataSet"]["commands"][0]["profiles"] = profiles
