import json

from pyracf.genprof.ResourceAdmin import ResourceAdmin


def main():
    profile_admin = ResourceAdmin()

    traits = {
        "resourcename": "BIKINI.BOTTOM.KRUSKRAB",
        "classname": "FACILITY",
        "uacc": "None",
        "owner": "eswift",
    }

    result = profile_admin.add(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
