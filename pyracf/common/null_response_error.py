"""Exception to use when no data is returned by IRRSMO00."""


class NullResponseError(Exception):
    """
    Raised when the no xml string is returned by IRRSMO00.
    """

    def __init__(self, xml_str: str) -> None:
        self.message = "Security request made to IRRSMO00 failed."
        self.xml_data = xml_str
        self.message += (
            "\n\nCheck to see if proper RACF permissions are in place.\n"
            + "For `set` or `alter` functions, you must have at least READ "
            + "access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class."
        )
        self.message = f"({self.__class__.__name__}) {self.message}"

    def __str__(self) -> str:
        return self.message
