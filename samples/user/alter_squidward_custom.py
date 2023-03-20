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

    update_segments = {
        "csdata" : {
            'jobrole' : 'jobrole'
        }
    }

    ca_segments = {
        "base" : {
            'special' : 'acf2:special'
        },
        "csdata" : {
            'jobrole' : 'jobrole'
        }
    }

    over_segments= {
        "csdata" : {
            'jobrole' : 'jobrole'
        }
    }

    result = user_admin.alter(traits)
    print(json.dumps(result, indent=4))

    user_admin.add_field_data(update_segments)
    traits['jobrole'] = 'cashier'
    print('added field data')
    result = user_admin.alter(traits)
    print(json.dumps(result, indent=4))
    user_admin = UserAdmin()

    user_admin.add_field_data(ca_segments)
    print('overwrote ca field data')
    result = user_admin.alter(traits)
    print(json.dumps(result, indent=4))
    user_admin = UserAdmin()

    user_admin.overwrite_field_data(over_segments)
    print('overwrote all field data')
    result = user_admin.alter(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
