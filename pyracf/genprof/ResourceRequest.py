from pyracf.common.SecurityRequest import SecurityRequest


class ResourceRequest(SecurityRequest):
    def __init__(self, resourcename: str, classname: str, function: str) -> None:
        super().__init__()
        self.security_definition.tag = "resource"
        self.security_definition.attrib = {
            "name": resourcename,
            "class": classname,
            "operation": function,
            "requestid": "ResourceRequest"
        }
