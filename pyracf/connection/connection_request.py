"""Connection Request Builder."""

from pyracf.common.security_request import SecurityRequest


class ConnectionRequest(SecurityRequest):
    """Connection Request Builder."""

    def __init__(
        self,
        userid,
        groupname,
        operation: str,
    ) -> None:
        super().__init__()
        self.security_definition.tag = "groupconnection"
        self.security_definition.attrib.update(
            {
                "name": userid,
                "group": groupname,
                "operation": operation,
                "requestid": "ConnectionRequest",
            }
        )