from pyracf.user.UserAdmin import UserAdmin
import json
import random
import string


def main():
    user_admin = UserAdmin()

    traits = {
        "name": "Squidward",
        "userid": "squidwrd",
        "password": "".join(random.choices(string.ascii_letters + string.digits, k=8)),
        "owner": "leonard",
        "special": True,
        "operator": False,
        "uid": "2424",
        "home": "/u/squidwrd",
        "program": "/bin/sh"
    }

    result = user_admin.add(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
