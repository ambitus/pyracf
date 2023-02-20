import json

from pyracf.genprof.ResourceAdmin import ResourceAdmin


def main():
    profile_admin = ResourceAdmin()

    resourcename = "IRR.IRRSMO00.PRECHECK"
    classname = "XFACILIT"

    result = profile_admin.delete(resourcename, classname)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
