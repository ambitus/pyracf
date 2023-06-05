"""Create a new group."""

import json

from pyracf.group.group_admin import GroupAdmin


def main():
    """Entrypoint."""
    group_admin = GroupAdmin(debug=True)

    traits = {
        "groupname": "TESTGRP0",
        "omvs:gid": "3434",
    }

    result = group_admin.add(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
