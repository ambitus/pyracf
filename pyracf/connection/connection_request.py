"""Connection Request Builder."""

from pyracf.common.security_request import SecurityRequest


class ConnectionRequest(SecurityRequest):
    """Connection Request Builder."""

    def __init__(
        self,
        userid: str,
        groupname: str,
        operation: str,
    ) -> None:
        super().__init__()
        self._security_definition.tag = "groupconnection"
        self._security_definition.attrib.update(
            {
                "name": userid,
                "group": groupname,
                "operation": operation,
                "requestid": "ConnectionRequest",
            }
        )
