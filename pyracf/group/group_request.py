"""Group Administration Request Builder."""

from pyracf.common.security_request import SecurityRequest


class GroupRequest(SecurityRequest):
    """Group Administration Request Builder."""

    def __init__(self, groupid: str, operation: str) -> None:
        super().__init__()
        self._security_definition.tag = "group"
        self._security_definition.attrib = {
            "name": groupid,
            "operation": operation,
            "requestid": "GroupRequest",
        }
