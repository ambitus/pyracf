"""Exception to use when Alter operation would add a new profile."""


class AlterOperationError(Exception):
    """
    Raised when a profile passed into an Alter is not successfully extracted.
    """

    def __init__(self, profile_name: str, class_name: str) -> None:
        self.message = "Security request made to IRRSMO00 failed."
        admin_types = ["USER", "GROUP", "DATASET"]
        if class_name not in admin_types:
            self.message += (
                "\n\nTarget profile "
                + f"'{profile_name}' does not exist as a profile in the {class_name} class."
            )
        else:
            self.message += (
                "\n\nTarget profile "
                + f"'{profile_name}' does not exist as a {class_name} profile."
            )

    def __str__(self) -> str:
        return self.message
