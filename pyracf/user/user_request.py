"""User Administration Request Builder."""

from pyracf.common.security_request import SecurityRequest


class UserRequest(SecurityRequest):
    """User Administration Request Builder."""

    def __init__(self, userid: str, function: str) -> None:
        super().__init__()
        self.security_definition.tag = "user"
        self.security_definition.attrib = {
            "name": userid,
            "operation": function,
            "requestid": "UserRequest",
        }
