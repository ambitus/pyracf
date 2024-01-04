"""Exception to use when IRRSMO00 processes a request with RACF warnings or errors."""


class SecurityRequestError(Exception):
    """
    Raised when pyRACF does not raise a DownstreamFatalError, and the SAF Return Code
    of a security result returned by IRRSMO00 is non-zero.
    """

    def __init__(self, result: dict) -> None:
        self.message = "Security request made to IRRSMO00 failed."
        self.result = result
        self.message += (
            "\n\nSee results dictionary "
            + f"'{self.__class__.__name__}.result' for more details."
        )
        self.message = f"({self.__class__.__name__}) {self.message}"

    def __str__(self) -> str:
        return self.message

    def contains_error_message(
        self, security_definition_tag: str, error_message_id: str
    ):
        """Checks to see if specific error message id appears in the security request error."""
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
