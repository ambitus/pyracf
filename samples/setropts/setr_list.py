"""List RACF Options."""

import json

from pyracf.setropts.setropts_admin import SetroptsAdmin


def main():
    """Entrypoint."""
    setropts_admin = SetroptsAdmin()

    result = setropts_admin.list_ropts()
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
