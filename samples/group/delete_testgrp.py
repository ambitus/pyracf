"""Delete a group."""

import json

from pyracf.group.group_admin import GroupAdmin


def main():
    """Entrypoint."""
    group_admin = GroupAdmin(debug=True)

    result = group_admin.delete("TESTGRP0")
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
