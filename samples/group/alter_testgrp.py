"""Alter an existing group."""

import json

from pyracf.group.group_admin import GroupAdmin


def main():
    """Entrypoint."""
    group_admin = GroupAdmin(debug=True)

    traits = {
        "groupname": "TESTGRP0",
        "omvs:gid": "8484",
    }

    result = group_admin.alter(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
