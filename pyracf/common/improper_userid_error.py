"""Exception to use when attempting to set an invalid userid for pyRACF to run under."""


class UserIdError(Exception):
    """
    Raised when pyRACF would attempt to run as a userid
    that is not a string between 1 to 8 characters in length.
    """

    def __init__(self, userid: str) -> None:
        self.message = (
            f"Unable to run as userid '{userid}'. Userid must "
            + "be a string value between 1 to 8 characters in length."
        )

    def __str__(self) -> str:
        return self.message
