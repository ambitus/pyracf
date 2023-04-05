"""Remove as id's access to a resource."""

import json

from pyracf.access.access_admin import AccessAdmin


def main():
    """Entrypoint."""
    access_admin = AccessAdmin()

    traits = {"resourcename": "TESTING", "classname": "ELIJTEST", "id": "ESWIFT"}

    result = access_admin.delete(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()