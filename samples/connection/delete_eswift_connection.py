"""Remove as id's connection to a group."""

import json

from pyracf.group.group_admin import GroupAdmin


def main():
    """Entrypoint."""
    group_admin = GroupAdmin()

    traits = {
        "groupname": "TESTGRP",
        "userid": "ESWIFT",
    }

    result = group_admin.delete(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
