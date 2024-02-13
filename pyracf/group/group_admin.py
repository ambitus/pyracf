"""Group Administration."""

from typing import List, Union

from pyracf.common.exceptions.add_operation_error import AddOperationError
from pyracf.common.exceptions.alter_operation_error import AlterOperationError
from pyracf.common.exceptions.security_request_error import SecurityRequestError
from pyracf.common.security_admin import SecurityAdmin

from .group_request import GroupRequest


class GroupAdmin(SecurityAdmin):
    """Group Administration."""

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
                "base:installation_data": "racf:data",
                "base:data_set_model": "racf:model",
                "base:owner": "racf:owner",
                "base:superior_group": "racf:supgroup",
                "base:terminal_universal_access": "racf:termuacc",
                "base:universal": "racf:universl",
            },
            "dfp": {
                "dfp:data_application": "dataappl",
                "dfp:data_class": "dataclas",
                "dfp:management_class": "mgmtclas",
                "dfp:storage_class": "storclas",
            },
            "omvs": {
                "omvs:auto_gid": "racf:autogid",
                "omvs:gid": "gid",
                "omvs:shared": "racf:shared",
            },
            "ovm": {"ovm:gid": "racf:gid"},
            "tme": {"tme:roles": "racf:roles"},
        }
        super().__init__(
            "group",
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
    # Group Special
    # ============================================================================
    def has_group_special_authority(
        self, group: str, userid: str
    ) -> Union[bool, bytes]:
        """Check if a user is connected to a group with group special authority."""
        profile = self.extract(group, profile_only=True)
        return self.__has_connect_attribute(userid, profile, "special")

    # ============================================================================
    # Group Operations
    # ============================================================================
    def has_group_operations_authority(
        self, group: str, userid: str
    ) -> Union[bool, bytes]:
        """Check if a user is connected to a group with group operations authority."""
        profile = self.extract(group, profile_only=True)
        return self.__has_connect_attribute(userid, profile, "operations")

    # ============================================================================
    # Group Auditor
    # ============================================================================
    def has_group_auditor_authority(
        self, group: str, userid: str
    ) -> Union[bool, bytes]:
        """Check if a user is connected to a group with group auditor authority."""
        profile = self.extract(group, profile_only=True)
        return self.__has_connect_attribute(userid, profile, "auditor")

    # ============================================================================
    # Group Access
    # ============================================================================
    def has_group_access_attribute(self, group: str, userid: str) -> Union[bool, bytes]:
        """Check if a user is connected to a group with the group access attribute."""
        profile = self.extract(group, profile_only=True)
        return self.__has_connect_attribute(userid, profile, "grpacc")

    # ============================================================================
    # OMVS GID
    # ============================================================================
    def get_omvs_gid(self, group: str) -> Union[int, bytes]:
        """Get a group's OMVS GID."""
        profile = self.extract(group, segments=["omvs"], profile_only=True)
        return self._get_field(profile, "omvs", "gid")

    def set_omvs_gid(self, group: str, gid: int) -> Union[dict, bytes]:
        """Set a group's OMVS GID."""
        result = self.alter(group, traits={"omvs:gid": gid})
        return self._to_steps(result)

    # ============================================================================
    # OVM GID
    # ============================================================================
    def get_ovm_gid(self, group: str) -> Union[int, bytes]:
        """Get a group's OVM GID."""
        profile = self.extract(group, segments=["ovm"], profile_only=True)
        return self._get_field(profile, "ovm", "gid")

    def set_ovm_gid(self, group: str, gid: int) -> Union[dict, bytes]:
        """Set a group's OVM GID."""
        result = self.alter(group, traits={"ovm:gid": gid})
        return self._to_steps(result)

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(self, group: str, traits: dict = {}) -> Union[dict, bytes]:
        """Create a new group."""
        if self._generate_requests_only:
            self._build_segment_trait_dictionary(traits)
            group_request = GroupRequest(group, "set")
            self._build_xml_segments(group_request)
            return self._make_request(group_request)
        try:
            self.extract(group)
        except SecurityRequestError as exception:
            if not exception.contains_error_message(self._profile_type, "ICH51003I"):
                raise exception
            self._build_segment_trait_dictionary(traits)
            group_request = GroupRequest(group, "set")
            self._build_xml_segments(group_request)
            return self._make_request(group_request)
        raise AddOperationError(group, self._profile_type)

    def alter(self, group: str, traits: dict) -> Union[dict, bytes]:
        """Alter an existing group."""
        if self._generate_requests_only:
            self._build_segment_trait_dictionary(traits)
            group_request = GroupRequest(group, "set")
            self._build_xml_segments(group_request, alter=True)
            return self._make_request(group_request, irrsmo00_precheck=True)
        try:
            self.extract(group)
        except SecurityRequestError as exception:
            raise AlterOperationError(group, self._profile_type) from exception
        self._build_segment_trait_dictionary(traits)
        group_request = GroupRequest(group, "set")
        self._build_xml_segments(group_request, alter=True)
        return self._make_request(group_request, irrsmo00_precheck=True)

    def extract(
        self, group: str, segments: List[str] = [], profile_only: bool = False
    ) -> Union[dict, bytes]:
        """Extract a group's profile."""
        self._build_segment_dictionary(segments)
        group_request = GroupRequest(group, "listdata")
        self._build_xml_segments(group_request, extract=True)
        result = self._extract_and_check_result(group_request)
        if profile_only:
            return self._get_profile(result)
        return result

    def delete(self, group: str) -> Union[dict, bytes]:
        """Delete a group."""
        group_request = GroupRequest(group, "del")
        return self._make_request(group_request)

    # ============================================================================
    # Private/Protected Utility Functions
    # ============================================================================
    def _format_profile(self, result: dict) -> None:
        """Format profile extract data into a dictionary."""
        messages = result["securityResult"]["group"]["commands"][0]["messages"]
        indexes = [
            i
            for i in range(len(messages) - 1)
            if messages[i] and "INFORMATION FOR GROUP " in messages[i]
        ]
        indexes.append(len(messages))
        profiles = []
        for i in range(len(indexes) - 1):
            profile = self._format_profile_generic(
                messages[indexes[i] : indexes[i + 1]]
            )
            if "subgroup(s)" in profile.keys():
                profile["subgroup(s)"] = profile["subgroups"]
            profiles.append(profile)

        # Post processing
        del result["securityResult"]["group"]["commands"][0]["messages"]
        result["securityResult"]["group"]["commands"][0]["profiles"] = profiles

    def __has_connect_attribute(
        self, userid: str, profile: dict, attribute: str
    ) -> bool:
        """check if a user has a connect attribute in a group profile."""
        if profile["base"]["users"] is None:
            return False
        connect_profile = [
            user
            for user in profile["base"]["users"]
            if user["userid"].lower() == userid.lower()
        ]
        if connect_profile:
            if attribute in connect_profile[0]["connectAttributes"]:
                return True
        return False
