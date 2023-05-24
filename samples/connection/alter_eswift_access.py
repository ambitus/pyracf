"""Change an id's connection to a group."""

import json

from pyracf.access.access_admin import AccessAdmin


def main():
    """Entrypoint."""
    access_admin = AccessAdmin()

    traits = {
        "groupname": "TESTGRP",
        "userid": "ESWIFT",
        "operator": False,
        "special": True,
    }

    result = access_admin.add(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
