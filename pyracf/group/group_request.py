"""Group Administration Request Builder."""

from pyracf.common.security_request import SecurityRequest


class GroupRequest(SecurityRequest):
    """Group Administration Request Builder."""

    def __init__(self, groupid: str, function: str) -> None:
        super().__init__()
        self.security_definition.tag = "group"
        self.security_definition.attrib = {
            "name": groupid,
            "operation": function,
            "requestid": "GroupRequest",
        }
