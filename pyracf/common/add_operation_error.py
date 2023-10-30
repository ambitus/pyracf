"""Exception to use when Add operation would alter an existing profile."""


class AddOperationError(Exception):
    """
    Raised when a profile cannot be added because it already exists.
    """

    def __init__(self, profile_name: str, class_name: str) -> None:
        self.message = "Refusing to make security request to IRRSMO00."
        admin_types = ["user", "group", "dataSet"]
        if class_name not in admin_types:
            self.message += (
                "\n\nTarget profile "
                + f"'{profile_name}' already exists as a profile in the '{class_name}' class."
            )
        else:
            self.message += (
                "\n\nTarget profile "
                + f"'{profile_name}' already exists as a '{class_name}' profile."
            )

    def __str__(self) -> str:
        return self.message
