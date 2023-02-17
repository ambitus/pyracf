from setropts.SetroptsAdmin import SetroptsAdmin
import json

def main():
    setropts_admin = SetroptsAdmin()

    traits = {
        'noraclist': 'elijtest'
    }

    result = setropts_admin.command(traits)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
