"""Alter an existing user."""

import json

from pyracf.user.user_admin import UserAdmin


def main():
    """Entrypoint."""
    user_admin = UserAdmin(debug=True)

    traits = {
        "userid": "squidwrd",
        "special": False,
        "home": "/u/clarinet",
        "program": False,
        "csdata:testcsfld": "testval",
    }

    extract_traits = {
        "userid": "squidwrd",
        "omvs": True,
        "csdata": True,
    }

    update_segments = {"csdata": {"tstcsfld": "tstcsfld"}}

    user_admin.add_field_data(update_segments)
    print("added field data")
    result = user_admin.alter(traits)

    user_admin.extract(extract_traits)


if __name__ == "__main__":
    main()
