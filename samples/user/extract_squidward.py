"""Extract a user profile."""

import json

from pyracf.user.user_admin import UserAdmin


def main():
    """Entrypoint."""
    user_adimn = UserAdmin()
    traits = {
        "userid": "squidwrd",
        "omvs": True,
        "mfa": False,
    }
    result = user_adimn.extract(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
