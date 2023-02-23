"""Delete a user."""

import json

from pyracf.user.user_admin import UserAdmin


def main():
    """Entrypoint."""
    user_admin = UserAdmin()

    result = user_admin.delete("squidwrd")
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
