from racf.user.UserAdmin import UserAdmin
import json


def main():
    user_adimn = UserAdmin()
    traits = {
        "userid": "squidwrd",
        "omvs": True,
        "mfa": False,
    }
    result = user_adimn.extract(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
