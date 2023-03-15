"""Extract a general resource profile."""

import json

from pyracf.genprof.resource_admin import ResourceAdmin


def main():
    """Entrypoint."""
    profile_admin = ResourceAdmin()

    traits = {"resourcename": "IRR.IRRSMO00.PRECHECK", "classname": "XFACILIT"}

    result = profile_admin.extract(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
