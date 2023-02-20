from pyracf.access.AccessAdmin import AccessAdmin
import json

def main():
    access_admin = AccessAdmin()

    traits = {
        "resourcename": "BIKINI.BOTTOM.KRUSKRAB",
        "classname": "FACILITY",
        "id": "ESWIFT"
    }

    result = access_admin.delete(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
