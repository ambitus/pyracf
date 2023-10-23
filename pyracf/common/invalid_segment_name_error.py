"""Exception to use when the user passes invalid segment name(s) on an extract request."""


class InvalidSegmentNameError(Exception):
    """
    Raised when a user passes an invalid segment name on an extract request.
    """

    def __init__(self, invalid_segments: list) -> None:
        self.message = "Building of Security Request failed.\n\n"
        for segment in invalid_segments:
            self.message += (
                "Could not find "
                + f"'{segment}' in valid segments for the requested operation.\n"
            )

    def __str__(self) -> str:
        return self.message
