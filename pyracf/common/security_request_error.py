"""Exception to use when data returned by IRRSMO00 indicates that the request failed."""


class SecurityRequestError(Exception):
    """
    Raised when IRRSMO0 request fails and result contains an "error" section.
    """

    def __init__(self, results: dict) -> None:
        self.message = "Security request made to IRRSMO00 failed."
        self.results = results
        self.message += (
            "\n\nSee results dictionary "
            + f"'{self.__class__.__name__}.results' for more details."
        )
        self.message = f"({self.__class__.__name__}) {self.message}"

    def __str__(self) -> str:
        return self.message
