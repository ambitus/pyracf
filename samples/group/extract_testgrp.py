"""Extract a group profile."""

import json

from pyracf.group.group_admin import GroupAdmin


def main():
    """Entrypoint."""
    group_admin = GroupAdmin(debug=True)
    traits = {
        "groupname": "TESTGRP0",
        "omvs": True,
    }
    result = group_admin.extract(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
