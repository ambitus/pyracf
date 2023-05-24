"""Connect an id to a group."""

import json

from pyracf.group.group_admin import GroupAdmin


def main():
    """Entrypoint."""
    group_admin = GroupAdmin()

    traits = {
        "groupname": "TESTGRP",
        "userid": "ESWIFT",
        "operator": True,
    }

    result = group_admin.add(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
