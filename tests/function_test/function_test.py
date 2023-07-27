import json
import os

from pyracf import UserAdmin


def main():
    user_admin = UserAdmin()
    userid = os.getlogin()
    profile = user_admin.extract(userid)
    json_profile = json.dumps(profile, indent=2)
    print(f"Profile extract for userid {userid} was successful:\n\n{json_profile}\n")


if __name__ == "__main__":
    main()
