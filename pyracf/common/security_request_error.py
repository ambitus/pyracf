"""Exception to use when data returned by IRRSMO00 indicates that the request failed."""


class SecurityRequestError(Exception):
    """
    Raised when the return code of a security result returned by IRRSMO00 is NOT equal to 0.
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
