# Getters and Setters

## `get_password_rules`
```python
>>> from setropts.SetroptsAdmin import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.get_password_rules()
[{'minlength': 4, 'maxlength': 8, 'content': '********', 'legend': {'*': 'ANYTHING'}}]
```

## `refresh`
```python
>>> from setropts.SetroptsAdmin import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.refresh('FACILITY')
{'securityresult': {'systemsettings': {'operation': 'set', 'requestid': 'SetroptsRequest', 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'SETROPTS      RACLIST     (FACILITY) REFRESH     ', 'messages': ['ICH14063I SETROPTS command complete.'], 'message': 'ICH14063I SETROPTS command complete.'}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `get_class_types`
```python
>>> from setropts.SetroptsAdmin import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.get_class_types('FACILITY')
['active', 'generic profile', 'generic command', 'setr raclist']
```

&nbsp;

# Add's and Del's

## `raclist_add`
```python
>>> from setropts.SetroptsAdmin import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.raclist_add('ELIJTEST')
{'securityresult': {'systemsettings': {'operation': 'set', 'requestid': 'SetroptsRequest', 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'SETROPTS      RACLIST     (ELIJTEST)', 'messages': ['ICH14063I SETROPTS command complete.'], 'message': 'ICH14063I SETROPTS command complete.'}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `raclist_del`
```python
>>> from setropts.SetroptsAdmin import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.get_class_types('ELIJTEST')
{'securityresult': {'systemsettings': {'operation': 'set', 'requestid': 'SetroptsRequest', 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'SETROPTS    NORACLIST     (ELIJTEST)', 'messages': ['ICH14063I SETROPTS command complete.'], 'message': 'ICH14063I SETROPTS command complete.'}]}, 'returncode': 0, 'reasoncode': 0}}
```

Additional add and del commands as follows with samples not shown:

```python
audit_add(class_name)/audit_del(class_name)
classact_add(class_name)/classact_del(class_name)
classstat_add(class_name)/classstat_del(class_name)
gencmd_add(class_name)/gencmd_del(class_name)
generic_add(class_name)/generic_del(class_name)
genlist_add(class_name)/genlist_del(class_name)
global_add(class_name)/global_del(class_name)
```

&nbsp;

# Run Set RACF Options Samples

:warning: _Run samples from the `irrsmo00` directory._

## Set a RACF Option

```shell
$ python3 samples/setropts/setr_do_cmd.py
```

```json
{
    "securityresult": {
        "systemsettings": {
            "operation": "set",
            "requestid": "SetroptsRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "SETROPTS      RACLIST     (elijtest)",
                    "messages": [
                        "ICH14063I SETROPTS command complete."
                    ],
                    "message": "ICH14063I SETROPTS command complete."
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}

```

## List the RACF Options

```shell
$ python3 samples/setropts/setr_list.py
```

```json
{
    "securityresult": {
        "systemsettings": {
            "operation": "set",
            "requestid": "SetroptsRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "SETROPTS   LIST        ",
                    "message": "SECONDARY LANGUAGE DEFAULT : ENU",
                    "profile": {
                        "attributes": [
                            "initstats",
                            "when(program",
                            "--",
                            "basic)"
                        ],
                        "statistics": null,
                        "active classes": [
                            "dataset",
                            "user",
                            "group",
                            "acctnum",
                            "aceechk",
                            "acicspct",
                            "appl",
                            "bcicspct",
                            "cbind",
                            "ccicscmd",
                            "cdt",
                            "command",
                            "cpsmobj",
                            "cryptoz",
                            "csfkeys",
                            "csfserv",
                            "dceuuids",
                            "dcicsdct",
                            "digtcert",
                            "digtcrit",
                            "digtnmap",
                            "digtring",
                            "dsnr",
                            "ecicsdct",
                            "ejbrole",
                            "elijtest",
                            "facility",
                            "fcicsfct",
                            "field",
                            "gcicstrn",
                            "gcpsmobj",
                            "gcsfkeys",
                            "gejbrole",
                            "gmqadmin",
                            "gmqnlist",
                            "gmqproc",
                            "gmqqueue",
                            "gsdsf",
                            "gsomdobj",
                            "gxcsfkey",
                            "gxfacili",
                            "gzmfapla",
                            "hcicsfct",
                            "jcicsjct",
                            "jesspool",
                            "kcicsjct",
                            "ldap",
                            "logstrm",
                            "mcicsppt",
                            "mqadmin",
                            "mqcmds",
                            "mqconn",
                            "mqnlist",
                            "mqproc",
                            "mqqueue",
                            "ncicsppt",
                            "omcandl$",
                            "opercmds",
                            "pcicspsb",
                            "pmbr",
                            "program",
                            "ptktdata",
                            "ptktval",
                            "qcicspsb",
                            "racfvars",
                            "rcicsres",
                            "rdatalib",
                            "realm",
                            "rvarsmbr",
                            "scicstst",
                            "sdsf",
                            "servauth",
                            "server",
                            "somdobjs",
                            "started",
                            "surrogat",
                            "tapevol",
                            "tcicstrn",
                            "tsoauth",
                            "tsoproc",
                            "ucicstst",
                            "unixpriv",
                            "vcicscmd",
                            "wbem",
                            "wcicsres",
                            "xcsfkey",
                            "xfacilit",
                            "zmfapla",
                            "zmfcloud"
                        ],
                        "generic profile classes": [
                            "dataset",
                            "acctnum",
                            "acicspct",
                            "aims",
                            "appclu",
                            "appcport",
                            "appcserv",
                            "appcsi",
                            "appctp",
                            "appl",
                            "cbind",
                            "ccicscmd",
                            "cims",
                            "command",
                            "console",
                            "cpsmobj",
                            "cpsmxmp",
                            "csfkeys",
                            "csfserv",
                            "dasdvol",
                            "dasnames",
                            "dbnform",
                            "dcicsdct",
                            "devices",
                            "diracc",
                            "dirauth",
                            "dirsrch",
                            "dlfclass",
                            "dsnr",
                            "ejbrole",
                            "facility",
                            "fcicsfct",
                            "field",
                            "fims",
                            "fsobj",
                            "fssec",
                            "gmbr",
                            "ibmopc",
                            "infoman",
                            "jcicsjct",
                            "jesinput",
                            "jesjobs",
                            "jesspool",
                            "ldap",
                            "lfsclass",
                            "logstrm",
                            "mcicsppt",
                            "mgmtclas",
                            "mqadmin",
                            "mqchan",
                            "mqcmds",
                            "mqconn",
                            "mqnlist",
                            "mqproc",
                            "mqqueue",
                            "netcmds",
                            "netspan",
                            "nodes",
                            "nodmbr",
                            "nvasapdt",
                            "oims",
                            "omcandl$",
                            "opercmds",
                            "pcicspsb",
                            "perfgrp",
                            "pims",
                            "pmbr",
                            "procact",
                            "process",
                            "propcntl",
                            "psfmpl",
                            "ptktdata",
                            "ptktval",
                            "racfvars",
                            "racglist",
                            "rcicsres",
                            "rmtops",
                            "rodmmgr",
                            "rvarsmbr",
                            "scdmbr",
                            "scicstst",
                            "sdsf",
                            "seclmbr",
                            "servauth",
                            "server",
                            "sims",
                            "smessage",
                            "somdobjs",
                            "started",
                            "storclas",
                            "subsysnm",
                            "surrogat",
                            "tapevol",
                            "tcicstrn",
                            "tempdsn",
                            "terminal",
                            "tims",
                            "tsoauth",
                            "tsoproc",
                            "unixpriv",
                            "vmbatch",
                            "vmbr",
                            "vmcmd",
                            "vmmac",
                            "vmmdisk",
                            "vmnode",
                            "vmrdr",
                            "vmsegmt",
                            "vtamappl",
                            "vxmbr",
                            "writer",
                            "xcsfkey",
                            "xfacilit",
                            "zmfapla",
                            "zmfcloud"
                        ],
                        "generic command classes": [
                            "dataset",
                            "acctnum",
                            "acicspct",
                            "aims",
                            "appclu",
                            "appcport",
                            "appcserv",
                            "appcsi",
                            "appctp",
                            "appl",
                            "cbind",
                            "ccicscmd",
                            "cims",
                            "command",
                            "console",
                            "cpsmobj",
                            "cpsmxmp",
                            "csfkeys",
                            "csfserv",
                            "dasdvol",
                            "dasnames",
                            "dbnform",
                            "dcicsdct",
                            "devices",
                            "diracc",
                            "dirauth",
                            "dirsrch",
                            "dlfclass",
                            "dsnr",
                            "ejbrole",
                            "facility",
                            "fcicsfct",
                            "field",
                            "fims",
                            "fsobj",
                            "fssec",
                            "gmbr",
                            "ibmopc",
                            "infoman",
                            "jcicsjct",
                            "jesinput",
                            "jesjobs",
                            "jesspool",
                            "ldap",
                            "lfsclass",
                            "logstrm",
                            "mcicsppt",
                            "mgmtclas",
                            "mqadmin",
                            "mqchan",
                            "mqcmds",
                            "mqconn",
                            "mqnlist",
                            "mqproc",
                            "mqqueue",
                            "netcmds",
                            "netspan",
                            "nodes",
                            "nodmbr",
                            "nvasapdt",
                            "oims",
                            "omcandl$",
                            "opercmds",
                            "pcicspsb",
                            "perfgrp",
                            "pims",
                            "pmbr",
                            "procact",
                            "process",
                            "propcntl",
                            "psfmpl",
                            "ptktdata",
                            "ptktval",
                            "racfvars",
                            "racglist",
                            "rcicsres",
                            "rmtops",
                            "rodmmgr",
                            "rvarsmbr",
                            "scdmbr",
                            "scicstst",
                            "sdsf",
                            "seclmbr",
                            "servauth",
                            "server",
                            "sims",
                            "smessage",
                            "somdobjs",
                            "started",
                            "storclas",
                            "subsysnm",
                            "surrogat",
                            "tapevol",
                            "tcicstrn",
                            "tempdsn",
                            "terminal",
                            "tims",
                            "tsoauth",
                            "tsoproc",
                            "unixpriv",
                            "vmbatch",
                            "vmbr",
                            "vmcmd",
                            "vmmac",
                            "vmmdisk",
                            "vmnode",
                            "vmrdr",
                            "vmsegmt",
                            "vtamappl",
                            "vxmbr",
                            "writer",
                            "xcsfkey",
                            "xfacilit",
                            "zmfapla",
                            "zmfcloud"
                        ],
                        "genlist classes": null,
                        "global checking classes": [
                            "dataset",
                            "dsnr",
                            "sdsf",
                            "surrogat"
                        ],
                        "setr raclist classes": [
                            "acctnum",
                            "aceechk",
                            "appl",
                            "cbind",
                            "cdt",
                            "cpsmobj",
                            "cryptoz",
                            "csfkeys",
                            "csfserv",
                            "digtcert",
                            "digtcrit",
                            "digtnmap",
                            "digtring",
                            "dsnr",
                            "ejbrole",
                            "elijtest",
                            "facility",
                            "jesspool",
                            "opercmds",
                            "ptktdata",
                            "ptktval",
                            "racfvars",
                            "rdatalib",
                            "realm",
                            "sdsf",
                            "servauth",
                            "server",
                            "somdobjs",
                            "started",
                            "surrogat",
                            "tsoauth",
                            "tsoproc",
                            "unixpriv",
                            "wbem",
                            "xcsfkey",
                            "xfacilit",
                            "zmfapla",
                            "zmfcloud"
                        ],
                        "global=yes raclist only": null,
                        "automatic dataset protection": false,
                        "enhanced generic naming": true,
                        "real data set names": "inactive",
                        "jes-batchallracf": true,
                        "jes-xbmallracf": "inactive",
                        "jes-earlyverify": "inactive",
                        "protect-all": false,
                        "tape data set protection": true,
                        "security retention period": 0.0,
                        "erase-on-scratch": "inactive",
                        "list of groups access checking": "active.",
                        "inactive userids": "being automatically revoked after 255.",
                        "data set modelling": "being done for gdgs.",
                        "user data set modelling": true,
                        "group data set modelling": true,
                        "password processing options": {
                            "password encryption algorithm": "legacy",
                            "password change interval": 186.0,
                            "password minimum change interval": 0.0,
                            "mixed case password support": false,
                            "special characters": false,
                            "history": 0,
                            "revoke": 0,
                            "password expiration warning level": 10.0,
                            "rules": [
                                {
                                    "minlength": 4,
                                    "maxlength": 8,
                                    "content": "********",
                                    "legend": {
                                        "*": "ANYTHING"
                                    }
                                }
                            ]
                        },
                        "default rvary password": "in effect for the status function.",
                        "seclabel control": false,
                        "generic owner only": false,
                        "compatibility mode": false,
                        "multi-level quiet": false,
                        "multi-level stable": false,
                        "no write-down": false,
                        "multi-level active": false,
                        "catalogued data sets only,": false,
                        "njeuserid": "????????",
                        "undefineduser": "++++++++",
                        "addcreator": true,
                        "kerblvl": 0,
                        "multi-level file system": false,
                        "multi-level interprocess communications": false,
                        "multi-level name hiding": false,
                        "security label by system": false,
                        "primary language default": "enu",
                        "secondary language default": "enu",
                        "sessionkey interval": 30.0
                    }
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```