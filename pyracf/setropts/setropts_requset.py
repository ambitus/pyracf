"""Set RCAF Options Administration Request Builder."""

from pyracf.common.security_request import SecurityRequest


class SetroptsRequest(SecurityRequest):
    """Set RCAF Options Administration Request Builder."""

    def __init__(self) -> None:
        super().__init__()
        self.security_definition.tag = "systemsettings"
        self.security_definition.attrib = {
            "operation": "set",
            "requestid": "SetroptsRequest",
        }
