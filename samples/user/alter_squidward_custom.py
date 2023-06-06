"""Alter an existing user."""

import json

from pyracf.user.user_admin import UserAdmin


def main():
    """Entrypoint."""
    user_admin = UserAdmin()

    traits = {
        "userid": "squidwrd",
        "special": False,
        "home": "/u/clarinet",
        "program": False,
        "testcsfld": "testval",
    }

    update_segments = {
        "csdata" : {
            'tstcsfld' : 'tstcsfld'
        }
    }

    result = user_admin.alter(traits,debug=True)
    print(json.dumps(result, indent=4))

    user_admin.add_field_data(update_segments)
    print('added field data')
    result = user_admin.alter(traits)

    user_admin.extract("squidwrd")



if __name__ == "__main__":
    main()
