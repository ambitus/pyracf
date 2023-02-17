# Getters and Setters

## `get_uacc`
```python
>>> from genprof.ResourceAdmin import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_uacc("BIKINI.BOTTOM.KRUSKRAB","FACILITY")
'read'
```

## `set_uacc`
```python
>>> from genprof.ResourceAdmin import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.set_uacc("BIKINI.BOTTOM.KRUSKRAB","FACILITY","ALTER")
{'securityresult': {'resource': {'name': 'BIKINI.BOTTOM.KRUSKRAB', 'class': 'FACILITY', 'operation': 'set', 'requestid': 'ResourceRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'RALTER  FACILITY             (BIKINI.BOTTOM.KRUSKRAB)  UACC        (ALTER)', 'messages': ['ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.'], 'message': 'ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.'}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `get_your_acc`
```python
>>> from genprof.ResourceAdmin import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_your_acc("BIKINI.BOTTOM.KRUSKRAB","FACILITY")
'read'
```

&nbsp;

# Run General Resource Profile Administration Samples

:warning: _Run samples from the `irrsmo00` directory._

## Add a General Resource Profile

```shell
$ python3 samples/genprof/add_kruskrab.py
```

```json
{
    "securityresult": {
        "resource": {
            "name": "BIKINI.BOTTOM.KRUSKRAB",
            "class": "FACILITY",
            "operation": "set",
            "requestid": "ResourceRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "RDEFINE FACILITY             (BIKINI.BOTTOM.KRUSKRAB) ",
                    "messages": [
                        "ICH10006I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE ADDITION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
                    ],
                    "message": "ICH10006I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE ADDITION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
                },
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "RALTER  FACILITY             (BIKINI.BOTTOM.KRUSKRAB)  UACC        (None) OWNER       (eswift)",
                    "messages": [
                        "ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
                    ],
                    "message": "ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Alter a General Resource Profile

```shell
$ python3 samples/genprof/alter_kruskrab.py
```

```json
{
    "securityresult": {
        "resource": {
            "name": "BIKINI.BOTTOM.KRUSKRAB",
            "class": "FACILITY",
            "operation": "set",
            "requestid": "ResourceRequest",
            "info": [
                "Definition exists. Add command skipped due  to precheck option"
            ],
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "RALTER  FACILITY             (BIKINI.BOTTOM.KRUSKRAB)  UACC        (Read) OWNER       (eswift)",
                    "messages": [
                        "ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
                    ],
                    "message": "ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Delete a General Resource Profile

```shell
$ python3 samples/genprof/delete_kruskrab.py
```

```json
{
    "securityresult": {
        "resource": {
            "name": "BIKINI.BOTTOM.KRUSKRAB",
            "class": "FACILITY",
            "operation": "del",
            "requestid": "ResourceRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "RDELETE FACILITY             (BIKINI.BOTTOM.KRUSKRAB) ",
                    "messages": [
                        "ICH12002I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
                    ],
                    "message": "ICH12002I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Extract a General Resource Profile

```shell
$ python3 samples/genprof/extract_kruskrab.py
```

```json
{
    "securityresult": {
        "resource": {
            "name": "BIKINI.BOTTOM.KRUSKRAB",
            "class": "FACILITY",
            "operation": "listdata",
            "requestid": "ResourceRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "RLIST   FACILITY             (BIKINI.BOTTOM.KRUSKRAB) ",
                    "message": "NO USER TO BE NOTIFIED",
                    "profile": {
                        "base": {
                            "class": "facility",
                            "name": "bikini.bottom.kruskrab",
                            "level": 0,
                            "owner": "eswift",
                            "universal access": "read",
                            "your access": null,
                            "warning": null,
                            "installation data": null,
                            "application data": null,
                            "auditing": "failures(read)",
                            "notify": null,
                            "generic": false
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