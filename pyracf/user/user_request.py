"""User Administration Request Builder."""

from pyracf.common.security_request import SecurityRequest


class UserRequest(SecurityRequest):
    """User Administration Request Builder."""

    def __init__(self, userid: str, operation: str) -> None:
        super().__init__()
        self._security_definition.tag = "user"
        self._security_definition.attrib = {
            "name": userid,
            "operation": operation,
            "requestid": "UserRequest",
        }
