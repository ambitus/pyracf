"""Extract a group profile."""

import json

from pyracf.group.group_admin import GroupAdmin


def main():
    """Entrypoint."""
    group_adimn = GroupAdmin()
    traits = {
        "groupname": "TESTGRP",
        "omvs": True,
    }
    result = group_adimn.extract(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
