"""Exception to use when attempting to set an invalid userid for pyRACF to run under."""


class ImproperUserIDError(Exception):
    """
    Raised when pyRACF would attempt to establish itself to
    run under a passed 'userid' that is not a string of 1 to 8 characters.
    """

    def __init__(self, userid: str) -> None:
        self.message = (
            "Cannot run under this userid."
            + f"{userid} is not a string from 1 to 8 characters in length."
        )

    def __str__(self) -> str:
        return self.message
