import json

from pyracf.user.UserAdmin import UserAdmin


def main():
    user_admin = UserAdmin()

    traits = {
        "userid": "squidwrd",
        "special": False,
        "operator": True,
        "home": "/u/clarinet",
        "program": False,
    }

    result = user_admin.alter(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
