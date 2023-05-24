"""Remove as id's access to a resource."""
"""Change an id's connection to a group."""

import json

from pyracf.access.access_admin import AccessAdmin


def main():
    """Entrypoint."""
    access_admin = AccessAdmin()

    traits = {
        "groupname": "TESTGRP",
        "userid": "ESWIFT",
    }

    result = access_admin.delete(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()