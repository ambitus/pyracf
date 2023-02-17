from user.UserAdmin import UserAdmin
import json


def main():
    user_admin = UserAdmin()

    result = user_admin.delete("squidwrd")
    print(json.dumps(result, indent=4))

if __name__ == "__main__":
    main()
