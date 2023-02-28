:warning: _Ensure that pyRACF is __[installed](../../README.md#installation)__ as a **Python package** before you run these samples._

# Run Access Administration Samples

:warning: _Run the following samples from the **root directory** of this **repository**._

## Add a Profile Permission

```shell
$ python3 samples/access/add_my_access.py
```

```json
{
    "securityresult": {
        "permission": {
            "name": "SAMPLE.TESTING.PROFILE",
            "class": "FACILITY",
            "operation": "set",
            "requestid": "AccessRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "PERMIT               SAMPLE.TESTING.PROFILE CLASS(FACILITY)  ACCESS      (READ) ID          (ESWIFT)",
                    "messages": [
                        "ICH06011I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED"
                    ],
                    "message": "ICH06011I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED"
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Alter a Profile Permission

```shell
$ python3 samples/access/alter_my_access.py
```

```json
{
    "securityresult": {
        "permission": {
            "name": "SAMPLE.TESTING.PROFILE",
            "class": "FACILITY",
            "operation": "set",
            "requestid": "AccessRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "PERMIT               SAMPLE.TESTING.PROFILE CLASS(FACILITY)  ACCESS      (NONE) ID          (ESWIFT)",
                    "messages": [
                        "ICH06011I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED"
                    ],
                    "message": "ICH06011I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED"
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

## Delete a Profile Permission

```shell
$ python3 samples/access/delete_my_access.py
```

```json
{
    "securityresult": {
        "permission": {
            "name": "SAMPLE.TESTING.PROFILE",
            "class": "FACILITY",
            "operation": "del",
            "requestid": "AccessRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "PERMIT               SAMPLE.TESTING.PROFILE CLASS(FACILITY)  DELETE       ID          (ESWIFT)",
                    "messages": [
                        "ICH06011I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED"
                    ],
                    "message": "ICH06011I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED"
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```