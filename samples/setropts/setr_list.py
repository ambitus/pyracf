from racf.setropts.SetroptsAdmin import SetroptsAdmin
import json

def main():
    setropts_admin = SetroptsAdmin()

    result = setropts_admin.list()
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
