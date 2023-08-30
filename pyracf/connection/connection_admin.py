"""RACF Connection Administration."""

from typing import Union

from pyracf.common.security_admin import SecurityAdmin
from pyracf.connection.connection_request import ConnectionRequest


class ConnectionAdmin(SecurityAdmin):
    """RACF Connection Administration."""

    _valid_segment_traits = {
        "base": {
            "base:adsp": "racf:adsp",
            "base:auditor": "racf:auditor",
            "base:auth": "racf:auth",
            "base:cgauthda": "racf:cgauthda",
            "base:cginitct": "racf:cginitct",
            "base:cgljdate": "racf:cgljdate",
            "base:cgljtime": "racf:cgljtime",
            "base:group": "racf:group",
            "base:group_access": "racf:grpacc",
            "base:operations": "racf:oper",
            "base:owner": "racf:owner",
            "base:resume": "racf:resume",
            "base:revoke": "racf:revoke",
            "base:revokefl": "racf:revokefl",
            "base:special": "racf:special",
            "base:uacc": "racf:uacc",
        }
    }

    def __init__(
        self,
        debug: bool = False,
        generate_requests_only: bool = False,
        update_existing_segment_traits: Union[dict, None] = None,
        overwrite_segment_traits: Union[dict, None] = None,
    ) -> None:
        super().__init__(
            "groupConnection",
            debug=debug,
            generate_requests_only=generate_requests_only,
            update_existing_segment_traits=update_existing_segment_traits,
            overwrite_segment_traits=overwrite_segment_traits,
        )

    # ============================================================================
    # Group Special
    # ============================================================================
    def give_group_special_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Give a user RACF special authority within a group."""
        result = self.alter(userid, group, {"base:special": True})
        return self._to_steps(result)

    def take_away_group_special_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Remove a user's RACF special authoritiy within a group."""
        result = self.alter(userid, group, {"base:special": False})
        return self._to_steps(result)

    # ============================================================================
    # Group Operations
    # ============================================================================
    def give_group_operations_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Give a user operations authority within a group."""
        result = self.alter(userid, group, {"base:operations": True})
        return self._to_steps(result)

    def take_away_group_operations_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Remove a user's operations authority within a group."""
        result = self.alter(userid, group, {"base:operations": False})
        return self._to_steps(result)

    # ============================================================================
    # Group Auditor
    # ============================================================================
    def give_group_auditor_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Give a user auditor authority within a group."""
        result = self.alter(userid, group, {"base:auditor": True})
        return self._to_steps(result)

    def take_away_group_auditor_authority(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """Remove a user's auditor authority within a group."""
        result = self.alter(userid, group, {"base:auditor": False})
        return self._to_steps(result)

    # ============================================================================
    # Group Access
    # ============================================================================
    def set_group_access_attribute(self, userid: str, group: str) -> Union[dict, bytes]:
        """
        Automatically make group data set profiles that a user
        creates accessible to all members of the group.
        """
        result = self.alter(userid, group, {"base:group_access": True})
        return self._to_steps(result)

    def remove_group_access_attribute(
        self, userid: str, group: str
    ) -> Union[dict, bytes]:
        """
        Don't automatically make group data set profiles that
        a user creates accessible to all members of the group.
        """
        result = self.alter(userid, group, {"base:group_access": False})
        return self._to_steps(result)

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(self, userid: str, group: str, traits: dict = {}) -> Union[dict, bytes]:
        """Create a new group connection."""
        self._build_segment_dictionaries(traits)
        connection_request = ConnectionRequest(userid, group, "set")
        self._add_traits_directly_to_request_xml_with_no_segments(connection_request)
        return self._make_request(connection_request)

    def alter(self, userid: str, group: str, traits: dict = {}) -> Union[dict, bytes]:
        """Alter an existing group connection."""
        self._build_segment_dictionaries(traits)
        connection_request = ConnectionRequest(userid, group, "set")
        self._add_traits_directly_to_request_xml_with_no_segments(
            connection_request, alter=True
        )
        return self._make_request(connection_request)

    def delete(self, userid: str, group: str) -> Union[dict, bytes]:
        """Delete a group connection."""
        self._clear_state()
        connection_request = ConnectionRequest(userid, group, "del")
        self._add_traits_directly_to_request_xml_with_no_segments(connection_request)
        return self._make_request(connection_request)
