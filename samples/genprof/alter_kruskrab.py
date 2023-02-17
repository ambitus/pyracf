from genprof.ResourceAdmin import ResourceAdmin
import json


def main():
    profile_admin = ResourceAdmin()

    traits = {
        "resourcename": "BIKINI.BOTTOM.KRUSKRAB",
        "classname": "FACILITY",
        "uacc": "Read",
        "owner": "eswift"
    }

    result = profile_admin.alter(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
