"""List RACF Options."""

import json

from pyracf.setropts.setropts_admin import SetroptsAdmin


def main():
    """Entrypoint."""
    setropts_admin = SetroptsAdmin()

    test_class = "ELIJTEST"

    result = setropts_admin.refresh(test_class)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
