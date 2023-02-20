import json

from pyracf.genprof.ResourceAdmin import ResourceAdmin


def main():
    profile_admin = ResourceAdmin()

    traits = {"resourcename": "BIKINI.BOTTOM.KRUSKRAB", "classname": "FACILITY"}

    result = profile_admin.extract(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
