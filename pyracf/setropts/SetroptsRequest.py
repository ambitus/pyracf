from pyracf.common.SecurityRequest import SecurityRequest


class SetroptsRequest(SecurityRequest):
    def __init__(self) -> None:
        super().__init__()
        self.security_definition.tag = "systemsettings"
        self.security_definition.attrib = {
            "operation": 'set',
            "requestid": "SetroptsRequest"
        }
