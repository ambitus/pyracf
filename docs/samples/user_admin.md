:warning: _Ensure that pyRACF is __[installed](../../README.md#installation)__ as a **Python package** before you run these samples._

# Setters and Getters

## `is_special`

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.is_special("squidwrd")
False
```

## `set_special`

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_special("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  SPECIAL     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `del_special`
```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.del_special("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  NOSPECIAL     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `is_auditor`

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.is_auditor("squidwrd")
False
```

## `set_auditor`

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_auditor("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  AUDITOR     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `del_auditor`
```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.del_auditor("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  NOAUDITOR     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `is_operations`

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.is_operations("squidwrd")
False
```

## `set_operations`

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_operations("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  OPERATIONS     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `del_operations`
```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.del_operations("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  NOOPERATIONS     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `get_uid`

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_uid("squidwrd")
2424
```

## `set_uid`

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_uid("squidwrd", 1919)
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'commands': [{'safreturncode': 8, 'returncode': 16, 'reasoncode': 8, 'image': 'ADDUSER SQUIDWRD ', 'messages': ['IKJ56702I INVALID USERID, SQUIDWRD']}, {'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (UID         (1919))'}]}, 'returncode': 4, 'reasoncode': 4}}
```

Additional set, add, del and no commands as follows with samples not shown:

```python
add_category(userid, category_name)/del_category(userid, category_name)
set_clauth(userid, clauth_name)/add_clauth(userid, clauth_name)/del_clauth(userid, clauth_name)/no_clauth(userid)
add_mfapolnm(userid, mfapolnm_name)/del_mfapolnm(userid, mfapolnm_name)
set_cics_opclass(userid, opclass_name)/add_cics_opclass(userid, opclass_name)/del_cics_opclass(userid, opclass_name)/no_cics_opclass(userid)
set_netview_opclass(userid, opclass_name)/add_netview_opclass(userid, opclass_name)/del_netview_opclass(userid, opclass_name)/no_netview_opclass(userid)
set_domain(userid, domain_name)/add_domain(userid, domain_name)/del_domain(userid, domain_name)/no_domains(userid)
set_mscope(userid, mscope_name)/add_mscope(userid, mscope_name)/del_mscope(userid, mscope_name)/no_mscope(userid)
```

&nbsp;

# Run User Administration Samples

:warning: _Run the following samples from the **root directory** of this **repository**._

## Add a user

```shell
$ python3 samples/user/add_squidward.py
```

```json
{
    "securityresult": {
        "user": {
            "name": "SQUIDWRD",
            "operation": "set",
            "requestid": "UserRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "ADDUSER SQUIDWRD ",
                    "message": "ICH01024I User SQUIDWRD is defined as PROTECTED."
                },
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "ALTUSER SQUIDWRD     NAME        ('Squidward') PASSWORD    (********) OWNER       (leonard) SPECIAL      OMVS     (UID         (2424) HOME        ('/u/squidwrd') PROGRAM     ('/bin/sh'))"
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Alter a User

```shell
$ python3 samples/user/alter_squidward.py
```

```json
{
    "securityresult": {
        "user": {
            "name": "SQUIDWRD",
            "operation": "set",
            "requestid": "UserRequest",
            "commands": [
                {
                    "safreturncode": 8,
                    "returncode": 16,
                    "reasoncode": 8,
                    "image": "ADDUSER SQUIDWRD ",
                    "message": "IKJ56702I INVALID USERID, SQUIDWRD"
                },
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "ALTUSER SQUIDWRD  NOSPECIAL      OPERATIONS   OMVS     (HOME        ('/u/clarinet') NOPROGRAM     )"
                }
            ]
        },
        "returncode": 4,
        "reasoncode": 4
    }
}
```

## Delete a User

```shell
$ python3 samples/user/delete_squidward.py
```

```json
{
    "securityresult": {
        "user": {
            "name": "SQUIDWRD",
            "operation": "del",
            "requestid": "UserRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "DELUSER SQUIDWRD"
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Extract a User Profile

```shell
$ python3 samples/user/extract_squidward.py
```

```json
{
    "securityresult": {
        "user": {
            "name": "SQUIDWRD",
            "operation": "listdata",
            "requestid": "UserRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "LISTUSER SQUIDWRD  OMVS    ",
                    "message": "MMAPAREAMAX= NONE",
                    "profile": {
                        "base": {
                            "groups": {
                                "SYS1": {
                                    "auth": "USE",
                                    "connectowner": "LEONARD",
                                    "connectdate": 23.046,
                                    "connects": 0,
                                    "uacc": null,
                                    "lastconnect": "UNKNOWN",
                                    "connectattributes": null,
                                    "revokedate": null,
                                    "resumedate": null
                                }
                            },
                            "user": "SQUIDWRD",
                            "name": "SQUIDWARD",
                            "owner": "LEONARD",
                            "created": 23.046,
                            "defaultgroup": "SYS1",
                            "passdate": 0.0,
                            "passinterval": 186,
                            "phrasedate": null,
                            "attributes": [],
                            "revokedate": null,
                            "resumedate": null,
                            "lastaccess": "23.046/07:13:09",
                            "classauthorizations": [],
                            "logonalloweddays": "ANYDAY",
                            "logonallowedtime": "ANYTIME",
                            "securitylevel": null,
                            "categoryauthorization": null,
                            "securitylabel": null
                        },
                        "omvs": {
                            "uid": 2424,
                            "home": "/u/clarinet",
                            "cputimemax": null,
                            "assizemax": null,
                            "fileprocmax": null,
                            "procusermax": null,
                            "threadsmax": null,
                            "mmapareamax": null
                        }
                    }
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```