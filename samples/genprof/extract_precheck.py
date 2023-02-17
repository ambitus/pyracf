from genprof.ResourceAdmin import ResourceAdmin
import json


def main():
    profile_admin = ResourceAdmin()

    traits = {
        "resourcename": "IRR.IRRSMO00.PRECHECK",
        "classname": "XFACILIT"
    }

    result = profile_admin.extract(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
