# Run Access Administration Samples

:warning: _Run samples from the `irrsmo00` directory._

## Add a Profile Permission

```shell
$ python3 samples/access/add_my_access.py
```

```json
{
    "securityresult": {
        "permission": {
            "name": "BIKINI.BOTTOM.KRUSKRAB",
            "class": "FACILITY",
            "operation": "set",
            "requestid": "AccessRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "PERMIT               BIKINI.BOTTOM.KRUSKRAB CLASS(FACILITY)  ACCESS      (READ) ID          (ESWIFT)",
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
            "name": "BIKINI.BOTTOM.KRUSKRAB",
            "class": "FACILITY",
            "operation": "set",
            "requestid": "AccessRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "PERMIT               BIKINI.BOTTOM.KRUSKRAB CLASS(FACILITY)  ACCESS      (NONE) ID          (ESWIFT)",
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
            "name": "BIKINI.BOTTOM.KRUSKRAB",
            "class": "FACILITY",
            "operation": "del",
            "requestid": "AccessRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "PERMIT               BIKINI.BOTTOM.KRUSKRAB CLASS(FACILITY)  DELETE       ID          (ESWIFT)",
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