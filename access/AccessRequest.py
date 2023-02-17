from common.SecurityRequest import SecurityRequest


class AccessRequest(SecurityRequest):
    def __init__(self, resourcename: str, classname: str, function: str, generic: str = "no" , volid: str = '') -> None:
        super().__init__()
        self.security_definition.tag = "permission"

        self.security_definition.attrib = {
            "name": resourcename,
            "class": classname,
            "operation": function,
            "requestid": "AccessRequest"
        }

        if not volid == '':
            self.security_definition.attrib["volid"] = volid
        if not generic == "no":
            self.security_definition.attrib["generic"] = generic

