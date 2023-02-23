"""Run a Set RACF Options command."""

import json

from pyracf.setropts.setropts_admin import SetroptsAdmin


def main():
    """Entrypoint."""
    setropts_admin = SetroptsAdmin()

    traits = {"raclist": "elijtest"}

    result = setropts_admin.command(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
