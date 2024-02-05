"""Exception to use when the user passes bad segment-trait name(s) on an add/alter request."""


class SegmentTraitError(Exception):
    """
    Raised when a user passes a bad segment-trait combination in the traits dictionary.
    """

    def __init__(self, bad_traits: list, profile_type: str) -> None:
        self.message = "Unable to build Security Request.\n\n"
        for trait in bad_traits:
            self.message += (
                f"'{trait}' is not a known segment-trait "
                + f"combination for '{profile_type}'.\n"
            )

    def __str__(self) -> str:
        return self.message
