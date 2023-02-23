from user.UserAdmin import UserAdmin
import json
import random
import string


def main():
    user_admin = UserAdmin()
    uid = "SQUILM"

    traits = {
        "name": "Squilliam",
        "userid": uid,
        "password": "".join(random.choices(string.ascii_letters + string.digits, k=8)),
        "owner": "eswift",
        "special": False,
        "operator": False,
        "uid": "9458",
        "home": "/u/squiliam",
        "program": "/bin/sh"
    }

    result = user_admin.add(traits)
    print(json.dumps(result, indent=4))

    print(user_admin.set_cics_opclass(uid,'TEST1')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.add_cics_opclass(uid,'TEST2')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.del_cics_opclass(uid,'TEST3')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.no_cics_opclass(uid)['securityresult']['user']['commands'][0]['image'])

    print(user_admin.set_netview_opclass(uid,'TEST4')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.add_netview_opclass(uid,'TEST5')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.del_netview_opclass(uid,'TEST6')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.no_netview_opclass(uid)['securityresult']['user']['commands'][0]['image'])

    print(user_admin.set_domain(uid,'TEST7')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.add_domain(uid,'TEST8')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.del_domain(uid,'TEST9')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.no_domains(uid)['securityresult']['user']['commands'][0]['image'])

    print(user_admin.add_category(uid,'TEST10')['securityresult']['user']['commands'][0]['image'])
    print(user_admin.del_category(uid,'TEST11')['securityresult']['user']['commands'][0]['image'])

    result = user_admin.delete(uid)
    print(json.dumps(result, indent=4))


if __name__ == "__main__":
    main()
