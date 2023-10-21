"""Exception to use when the user passes invalid segment-trait(s) in the traits dictionary."""


class InvalidSegmentTraitError(Exception):
    """
    Raised when a user passes an invalid segment-trait combination in the traits dictionary.
    """

    def __init__(self, invalid_traits: list) -> None:
        self.message = "Building of Security Request failed.\n\n"
        for trait in invalid_traits:
            self.message += (
                "Could not find "
                + f"'{trait}' in valid segment traits for the requested operation.\n"
            )

    def __str__(self) -> str:
        return self.message
