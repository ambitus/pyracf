"""Connect an id to a group."""

import json

from pyracf.connection.connection_admin import ConnectionAdmin


def main():
    """Entrypoint."""
    connection_admin = ConnectionAdmin(debug=True)

    traits = {
        "groupname": "TESTGRP0",
        "userid": "ESWIFT",
        "operator": True,
    }

    result = connection_admin.add(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
