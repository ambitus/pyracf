from access.AccessAdmin import AccessAdmin
import json

def main():
    access_admin = AccessAdmin()

    traits = {
        "resourcename": "BIKINI.BOTTOM.KRUSKRAB",
        "classname": "FACILITY",
        "access": "READ",
        "id": "ESWIFT"
    }

    result = access_admin.add(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
