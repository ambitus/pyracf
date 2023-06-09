"""RACF Connection Administration."""

from pyracf.common.security_admin import SecurityAdmin
from pyracf.connection.connection_request import ConnectionRequest


class ConnectionAdmin(SecurityAdmin):
    """RACF Connection Administration."""

    def __init__(
        self, debug: bool = False, generate_requests_only: bool = False
    ) -> None:
        super().__init__(
            "groupconnection",
            debug=debug,
            generate_requests_only=generate_requests_only,
        )
        self._valid_segment_traits = {
            "base": {
                "base:adsp": "racf:adsp",
                "base:auditor": "racf:auditor",
                "base:auth": "racf:auth",
                "base:cgauthda": "racf:cgauthda",
                "base:cginitct": "racf:cginitct",
                "base:cgljdate": "racf:cgljdate",
                "base:cgljtime": "racf:cgljtime",
                "base:group": "racf:group",
                "base:grpacc": "racf:grpacc",
                "base:operations": "racf:oper",
                "base:owner": "racf:owner",
                "base:resume": "racf:resume",
                "base:revoke": "racf:revoke",
                "base:revokefl": "racf:revokefl",
                "base:special": "racf:special",
                "base:uacc": "racf:uacc",
            }
        }

    # ============================================================================
    # Group Special
    # ============================================================================
    def give_group_special_authority(self, userid: str, group: str) -> dict:
        result = self.alter(userid, group, {"base:special": True})
        return self._to_steps(result)

    def take_away_group_special_authority(self, userid: str, group: str) -> dict:
        result = self.alter(userid, group, {"base:special": False})
        return self._to_steps(result)

    # ============================================================================
    # Group Operations
    # ============================================================================
    def give_group_operations_authority(self, userid: str, group: str) -> dict:
        result = self.alter(userid, group, {"base:operations": True})
        return self._to_steps(result)

    def take_away_group_operations_authority(self, userid: str, group: str) -> dict:
        result = self.alter(userid, group, {"base:operations": False})
        return self._to_steps(result)

    # ============================================================================
    # Group Auditor
    # ============================================================================
    def give_group_auditor_authority(self, userid: str, group: str) -> dict:
        result = self.alter(userid, group, {"base:auditor": True})
        return self._to_steps(result)

    def take_away_group_auditor_authority(self, userid: str, group: str) -> dict:
        result = self.alter(userid, group, {"base:auditor": False})
        return self._to_steps(result)

    # ============================================================================
    # Group Access
    # ============================================================================
    def set_group_access_attribute(self, userid: str, group: str) -> dict:
        result = self.alter(userid, group, {"base:grpacc": True})
        return self._to_steps(result)

    def remove_group_access_attribute(self, userid: str, group: str) -> dict:
        result = self.alter(userid, group, {"base:grpacc": False})
        return self._to_steps(result)

    # ============================================================================
    # Base Functions
    # ============================================================================
    def add(self, userid: str, group: str, traits: dict = {}) -> dict:
        """Create a new group connection."""
        self._build_segment_dictionaries(traits)
        connection_request = ConnectionRequest(userid, group, "set")
        self._add_traits_directly_to_request_xml_with_no_segments(connection_request)
        return self._make_request(connection_request)

    def alter(self, userid: str, group: str, traits: dict = {}) -> dict:
        """Alter an existing group connection."""
        self._build_segment_dictionaries(traits)
        connection_request = ConnectionRequest(userid, group, "set")
        self._add_traits_directly_to_request_xml_with_no_segments(
            connection_request, alter=True
        )
        return self._make_request(connection_request)

    def delete(self, userid: str, group: str) -> dict:
        """Delete a group connection."""
        connection_request = ConnectionRequest(userid, group, "del")
        self._add_traits_directly_to_request_xml_with_no_segments(connection_request)
        return self._make_request(connection_request)
