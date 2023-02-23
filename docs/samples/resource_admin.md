:warning: _Ensure that pyRACF is __[installed](../../README.md#installation)__ as a **Python package** before you run these samples._

# Getters and Setters

## `get_uacc`
```python
>>> from pyracf.genprof.resource_admin import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_uacc("BIKINI.BOTTOM.KRUSKRAB","FACILITY")
'read'
```

## `set_uacc`
```python
>>> from pyracf.genprof.resource_admin import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.set_uacc("BIKINI.BOTTOM.KRUSKRAB","FACILITY","ALTER")
{'securityresult': {'resource': {'name': 'BIKINI.BOTTOM.KRUSKRAB', 'class': 'FACILITY', 'operation': 'set', 'requestid': 'ResourceRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'RALTER  FACILITY             (BIKINI.BOTTOM.KRUSKRAB)  UACC        (ALTER)', 'messages': ['ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.'], 'message': 'ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.'}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `get_your_acc`
```python
>>> from pyracf.genprof.resource_admin import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_your_acc("BIKINI.BOTTOM.KRUSKRAB","FACILITY")
'read'
```

Additional set, add, del and no commands as follows with samples not shown:

```python
add_category(resource_name, class_name, category_name)/del_category(resource_name, class_name, category_name)
add_member(resource_name, class_name, member_name)/del_member(resource_name, class_name, member_name)
add_volume(resource_name, class_name, volume_name)/del_volume(resource_name, class_name, volume_name)
set_jobname(resource_name, class_name, jobname_name)/add_jobname(resource_name, class_name, jobname_name)/del_jobname(resource_name, class_name, jobname_name)/no_jobnames(resource_name, class_name)
set_crtlbl(resource_name, class_name, crtlbl_name)/add_crtlbl(resource_name, class_name, crtlbl_name)/del_crtlbl(resource_name, class_name, crtlbl_name)/no_crtlbls(resource_name, class_name)
set_keylbl(resource_name, class_name, keylbl_name)/add_keylbl(resource_name, class_name, keylbl_name)/del_keylbl(resource_name, class_name, keylbl_name)/no_keylbls(resource_name, class_name)
set_factor(resource_name, class_name, factor_name)/add_factor(resource_name, class_name, factor_name)/del_factor(resource_name, class_name, factor_name)/no_factors(resource_name, class_name)
set_child(resource_name, class_name, child_name)/add_child(resource_name, class_name, child_name)/del_child(resource_name, class_name, child_name)/no_children(resource_name, class_name)
set_group(resource_name, class_name, group_name)/add_group(resource_name, class_name, group_name)/del_group(resource_name, class_name, group_name)/no_groups(resource_name, class_name)
set_resource(resource_name, class_name, tme_resource_name)/add_resource(resource_name, class_name, tme_resource_name)/del_resource(resource_name, class_name, tme_resource_name)/no_resources(resource_name, class_name)
set_role(resource_name, class_name, role_name)/add_role(resource_name, class_name, role_name)/del_role(resource_name, class_name, role_name)/no_roles(resource_name, class_name) 
```

&nbsp;

# Run General Resource Profile Administration Samples

:warning: _Run the following samples from the **root directory** of this **repository**._

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