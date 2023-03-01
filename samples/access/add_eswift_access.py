"""Give an id access to a resource."""

import json

from pyracf.access.access_admin import AccessAdmin


def main():
    """Entrypoint."""
    access_admin = AccessAdmin()

    traits = {
        "resourcename": "TESTING",
        "classname": "ELIJTEST",
        "access": "READ",
        "id": "ESWIFT",
    }

    result = access_admin.add(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
