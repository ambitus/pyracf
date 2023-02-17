# Setters and Getters

## `is_special`

```python
>>> from user.UserAdmin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.is_special("squidwrd")
False
```

## `set_special`

```python
>>> from user.UserAdmin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_special("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'commands': [{'safreturncode': 8, 'returncode': 16, 'reasoncode': 8, 'image': 'ADDUSER SQUIDWRD ', 'messages': ['IKJ56702I INVALID USERID, SQUIDWRD']}, {'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  SPECIAL     '}]}, 'returncode': 4, 'reasoncode': 4}}
```

## `get_uid`

```python
>>> from user.UserAdmin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_uid("squidwrd")
2424
```

## `set_uid`

```python
>>> from user.UserAdmin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_uid("squidwrd", 1919)
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'commands': [{'safreturncode': 8, 'returncode': 16, 'reasoncode': 8, 'image': 'ADDUSER SQUIDWRD ', 'messages': ['IKJ56702I INVALID USERID, SQUIDWRD']}, {'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (UID         (1919))'}]}, 'returncode': 4, 'reasoncode': 4}}
```

&nbsp;

# Run User Administration Samples

:warning: _Run samples from the `irrsmo00` directory._

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