"""Remove as id's connection to a group."""

import json

from pyracf.connection.connection_admin import ConnectionAdmin


def main():
    """Entrypoint."""
    connection_admin = ConnectionAdmin(debug=True)

    traits = {
        "groupname": "TESTGRP0",
        "userid": "ESWIFT",
    }

    result = connection_admin.delete(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
