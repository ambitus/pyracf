"""Exception to use when the user passes bad segment name(s) on an extract request."""


class SegmentError(Exception):
    """
    Raised when a user passes a bad segment name on an extract request.
    """

    def __init__(self, bad_segments: list, profile_type: str) -> None:
        self.message = "Unable to build Security Request.\n\n"
        for segment in bad_segments:
            self.message += (
                f"'{segment}' is not a known segment for '{profile_type}'.\n"
            )

    def __str__(self) -> str:
        return self.message
