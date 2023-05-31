"""RACF Connection Administration."""

from pyracf.common.security_admin import SecurityAdmin
from pyracf.connection.connection_request import ConnectionRequest


class ConnectionAdmin(SecurityAdmin):
    """RACF Connection Administration."""

    def __init__(self, debug=False) -> None:
        super().__init__(debug=debug)
        self.valid_segment_traits = {
            "base": {
                "adsp": "racf:adsp",
                "auditor": "racf:auditor",
                "auth": "racf:auth",
                "cgauthda": "racf:cgauthda",
                "cginitct": "racf:cginitct",
                "cgljdate": "racf:cgljdate",
                "cgljtime": "racf:cgljtime",
                "group": "racf:group",
                "grpacc": "racf:grpacc",
                "oper": "racf:oper",
                "owner": "racf:owner",
                "resume": "racf:resume",
                "revoke": "racf:revoke",
                "revokefl": "racf:revokefl",
                "special": "racf:special",
                "uacc": "racf:uacc",
            }
        }

    def set_group_special(
        self, userid: str, group_name: str, generate_request_only=False
    ) -> dict:
        return self.alter(
            {"userid": userid, "groupname": group_name, "special": True},
            generate_request_only=generate_request_only,
        )

    def set_group_operations(
        self, userid: str, group_name: str, generate_request_only=False
    ) -> dict:
        return self.alter(
            {"userid": userid, "groupname": group_name, "oper": True},
            generate_request_only=generate_request_only,
        )

    def set_group_auditor(
        self, userid: str, group_name: str, generate_request_only=False
    ) -> dict:
        return self.alter(
            {"userid": userid, "groupname": group_name, "auditor": True},
            generate_request_only=generate_request_only,
        )

    def set_grpacc(
        self, userid: str, group_name: str, generate_request_only=False
    ) -> dict:
        return self.alter(
            {"userid": userid, "groupname": group_name, "grpacc": True},
            generate_request_only=generate_request_only,
        )

    def del_group_special(
        self, userid: str, group_name: str, generate_request_only=False
    ) -> dict:
        return self.alter(
            {"userid": userid, "groupname": group_name, "special": False},
            generate_request_only=generate_request_only,
        )

    def del_group_operations(
        self, userid: str, group_name: str, generate_request_only=False
    ) -> dict:
        return self.alter(
            {"userid": userid, "groupname": group_name, "oper": False},
            generate_request_only=generate_request_only,
        )

    def del_group_auditor(
        self, userid: str, group_name: str, generate_request_only=False
    ) -> dict:
        return self.alter(
            {"userid": userid, "groupname": group_name, "auditor": False},
            generate_request_only=generate_request_only,
        )

    def del_grpacc(
        self, userid: str, group_name: str, generate_request_only=False
    ) -> dict:
        return self.alter(
            {"userid": userid, "groupname": group_name, "grpacc": False},
            generate_request_only=generate_request_only,
        )

    def add(self, traits: dict, generate_request_only=False) -> dict:
        """Create a new group connection."""
        userid = traits["userid"]
        groupname = traits["groupname"]
        self.build_segment_dictionaries(traits)
        connection_request = ConnectionRequest(userid, groupname, "set")
        self.build_segments(connection_request)
        return self.make_request(
            connection_request, generate_request_only=generate_request_only
        )

    def alter(self, traits: dict, generate_request_only=False) -> dict:
        """Alter an existing group connection."""
        userid = traits["userid"]
        groupname = traits["groupname"]
        self.build_segment_dictionaries(traits)
        connection_request = ConnectionRequest(userid, groupname, "set")
        self.build_segments(connection_request, alter=True)
        return self.make_request(
            connection_request, generate_request_only=generate_request_only
        )

    def delete(self, traits: dict, generate_request_only=False) -> dict:
        """Delete a group connection."""
        userid = traits["userid"]
        groupname = traits["groupname"]
        self.build_segment_dictionaries(traits)
        connection_request = ConnectionRequest(userid, groupname, "del")
        self.build_segments(connection_request)
        return self.make_request(
            connection_request, generate_request_only=generate_request_only
        )

    def build_segments(
        self, connection_request: ConnectionRequest, alter=False
    ) -> None:
        """Build XML representation of segments."""
        for segment, traits in self.segment_traits.items():
            if segment == "base":
                connection_request.build_segment(
                    "", traits, self.trait_map, alter=alter
                )
        # Clear segments for new request
        self.segment_traits = {}
