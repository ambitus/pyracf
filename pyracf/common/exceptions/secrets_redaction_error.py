"""Exception to use when Additional Secrets could not be Redacted."""

from typing import List


class SecretsRedactionError(Exception):
    """
    Raised when a specified secret cannot be redacted because it does not map to a segement:trait.
    """

    def __init__(
        self, profile_type: str = "", bad_secret_traits: List[str] = []
    ) -> None:
        profile_map = {
            "user": "User",
            "group": "Group",
            "dataSet": "Data Set",
            "resource": "General Resource",
            "permission": "Access",
            "groupConnection": "Group Connection",
            "systemSettings": "Setropts",
        }
        self.message = (
            f"Cannot add specified additional secrets to {profile_map[profile_type]} "
            + "administration."
        )

        if bad_secret_traits:
            for trait in bad_secret_traits:
                self.message = self.message + (
                    f"\nCould not map {trait} to a valid segment trait."
                )
        else:
            self.message = self.message + (
                f"\n{profile_map[profile_type]} administration does"
                + " not support additional secrets redaction."
            )

    def __str__(self) -> str:
        return self.message
