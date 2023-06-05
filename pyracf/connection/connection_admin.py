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
                "base:oper": "racf:oper",
                "base:owner": "racf:owner",
                "base:resume": "racf:resume",
                "base:revoke": "racf:revoke",
                "base:revokefl": "racf:revokefl",
                "base:special": "racf:special",
                "base:uacc": "racf:uacc",
            }
        }

    def set_group_special(self, userid: str, group: str) -> dict:
        return self.alter(userid, group, {"base:special": True})

    def set_group_operations(self, userid: str, group: str) -> dict:
        return self.alter(userid, group, {"base:oper": True})

    def set_group_auditor(self, userid: str, group: str) -> dict:
        return self.alter(userid, group, {"base:auditor": True})

    def set_grpacc(self, userid: str, group: str) -> dict:
        return self.alter(userid, group, {"base:grpacc": True})

    def del_group_special(self, userid: str, group: str) -> dict:
        return self.alter(
            userid,
            group,
            {"base:special": False},
        )

    def del_group_operations(self, userid: str, group: str) -> dict:
        return self.alter(userid, group, {"base:oper": False})

    def del_group_auditor(self, userid: str, group: str) -> dict:
        return self.alter(userid, group, {"base:auditor": False})

    def del_grpacc(self, userid: str, group: str) -> dict:
        return self.alter(userid, group, {"base:grpacc": False})

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
