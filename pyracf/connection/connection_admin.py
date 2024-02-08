"""RACF Connection Administration."""

from typing import List, Union

from pyracf.common.security_admin import SecurityAdmin

from .connection_request import ConnectionRequest


class ConnectionAdmin(SecurityAdmin):
    """RACF Connection Administration."""

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
                "base:automatic_data_set_protection": "racf:adsp",
                "base:auditor": "racf:auditor",
                "base:group_authority": "racf:auth",
                "base:group": "racf:group",
                "base:group_access": "racf:grpacc",
                "base:operations": "racf:oper",
                "base:owner": "racf:owner",
                "base:resume": "racf:resume",
                "base:revoke": "racf:revoke",
                "base:special": "racf:special",
                "base:universal_access": "racf:uacc",
            }
        }
        super().__init__(
            "groupConnection",
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
    def give_group_special_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Give a user RACF special authority within a group."""
        result = self.connect(userid, group, {"base:special": True})
        return self._to_steps(result)

    def take_away_group_special_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Remove a user's RACF special authoritiy within a group."""
        result = self.connect(userid, group, {"base:special": False})
        return self._to_steps(result)

    # ============================================================================
    # Group Operations
    # ============================================================================
    def give_group_operations_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Give a user operations authority within a group."""
        result = self.connect(userid, group, {"base:operations": True})
        return self._to_steps(result)

    def take_away_group_operations_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Remove a user's operations authority within a group."""
        result = self.connect(userid, group, {"base:operations": False})
        return self._to_steps(result)

    # ============================================================================
    # Group Auditor
    # ============================================================================
    def give_group_auditor_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Give a user auditor authority within a group."""
        result = self.connect(userid, group, {"base:auditor": True})
        return self._to_steps(result)

    def take_away_group_auditor_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Remove a user's auditor authority within a group."""
        result = self.connect(userid, group, {"base:auditor": False})
        return self._to_steps(result)

    # ============================================================================
    # Group Access
    # ============================================================================
    def give_group_access_attribute(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """
        Automatically make group data set profiles that a user
        creates accessible to all members of the group.
        """
        result = self.connect(userid, group, {"base:group_access": True})
        return self._to_steps(result)

    def take_away_group_access_attribute(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """
        Don't automatically make group data set profiles that
        a user creates accessible to all members of the group.
        """
        result = self.connect(userid, group, {"base:group_access": False})
        return self._to_steps(result)

    # ============================================================================
    # Base Functions
    # ============================================================================
    def connect(self, userid: str, group: str, traits: dict = {}) -> Union[dict, bytes]:
        """Create or change a group connection."""
        self._build_segment_trait_dictionary(traits)
        connection_request = ConnectionRequest(userid, group, "set")
        self._add_traits_directly_to_request_xml_with_no_segments(
            connection_request, alter=True
        )
        return self._make_request(connection_request)

    def delete(self, userid: str, group: str) -> Union[dict, bytes]:
        """Delete a group connection."""
        connection_request = ConnectionRequest(userid, group, "del")
        self._add_traits_directly_to_request_xml_with_no_segments(connection_request)
        return self._make_request(connection_request)
