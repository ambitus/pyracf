"""Exception to use when data returned by IRRSMO00 indicates that the request failed."""


class SecurityRequestError(Exception):
    """
    Raised when the return code of a security result returned by IRRSMO00 is NOT equal to 0.
    """

    def __init__(self, result: dict, request_xml: str) -> None:
        self.message = "Security request made to IRRSMO00 failed."
        self.request_xml = request_xml
        self.result = self.__check_result_type(result)
        self.message += (
            "\n\nSee results dictionary "
            + f"'{self.__class__.__name__}.result' for more details."
        )
        self.message = f"({self.__class__.__name__}) {self.message}"

    def __str__(self) -> str:
        return self.message

    def __check_result_type(self, result: dict) -> dict:
        not_profiles = ["returnCode", "reasonCode", "runningUserid"]
        for profile_type in result["securityResult"]:
            if profile_type in not_profiles:
                continue
            if "error" in result["securityResult"][profile_type]:
                return self.__organize_smo_error(result, profile_type)
        return result

    def __organize_smo_error(self, result: dict, profile_type: str) -> dict:
        command_result = {}
        command_result["image"] = self.request_xml.decode("utf-8")
        command_result["safReturnCode"] = result["securityResult"][profile_type][
            "error"
        ]["errorFunction"]
        command_result["returnCode"] = result["securityResult"][profile_type]["error"][
            "errorCode"
        ]
        command_result["reasonCode"] = result["securityResult"][profile_type]["error"][
            "errorReason"
        ]
        error_offset = result["securityResult"][profile_type]["error"]["errorOffset"]
        error_text = result["securityResult"][profile_type]["error"]["textInError"]
        error_message = (
            result["securityResult"][profile_type]["error"]["errorMessage"]
            + "\n"
            + f"Text in Error: '{error_text}'\n"
            + f"Approximate Offset of Text in Error: '{error_offset}'\n"
            + "Please note that for any text in error,"
            + " redacted values may skew offset calculations."
        )
        command_result["messages"] = [error_message]
        result["securityResult"][profile_type]["commands"] = [command_result]
        del result["securityResult"][profile_type]["error"]
        return result

    def contains_error_message(
        self, security_definition_tag: str, error_message_id: str
    ):
        """Checks to see if specific error message id appears in the security request error"""
        commands = self.result["securityResult"][security_definition_tag].get(
            "commands"
        )
        if not isinstance(commands, list):
            return False
        messages = commands[0].get("messages", [])
        if error_message_id in "".join(messages):
            return True
        else:
            return False
