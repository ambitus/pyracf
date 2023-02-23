"""Alter an existing user."""

import json

from pyracf.user.user_admin import UserAdmin


def main():
    """Entrypoint."""
    user_admin = UserAdmin()

    traits = {
        "userid": "squidwrd",
        "special": False,
        "operator": True,
        "home": "/u/clarinet",
        "program": False,
    }

    result = user_admin.alter(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
