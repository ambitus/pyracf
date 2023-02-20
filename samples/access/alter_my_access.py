import json

from pyracf.access.AccessAdmin import AccessAdmin


def main():
    access_admin = AccessAdmin()

    traits = {
        "resourcename": "BIKINI.BOTTOM.KRUSKRAB",
        "classname": "FACILITY",
        "access": "NONE",
        "id": "ESWIFT",
    }

    result = access_admin.alter(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
