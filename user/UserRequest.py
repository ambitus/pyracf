from common.SecurityRequest import SecurityRequest


class UserRequest(SecurityRequest):
    def __init__(self, userid: str, function: str) -> None:
        super().__init__()
        self.security_definition.tag = "user"
        self.security_definition.attrib = {
            "name": userid,
            "operation": function,
            "requestid": "UserRequest"
        }
