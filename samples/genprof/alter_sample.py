"""Alter a general resource profile."""

import json

from pyracf.genprof.resource_admin import ResourceAdmin


def main():
    """Entrypoint."""
    profile_admin = ResourceAdmin()

    traits = {
        "resourcename": "TESTING",
        "classname": "ELIJTEST",
        "uacc": "Read",
        "owner": "eswift",
    }

    result = profile_admin.alter(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
