# pyRACF Documentation

pyRACF provides a simplified interface to IBMs security product Resource Access Control Facility aka RACF. Python programmers can use this as a way to manage their RACF environment without having to understand the underlying z/OS interfaces.

The pyRACF implementation relies on the R_SecMgtOper. The architectural decision for this interface can be found in the [choose-RACF-interface.md](../adr/choose-RACF-interface.md) file.

There is a small amount of C code written to connect Python with the underlying R_SecMgtOper macro and marshalling and demarshalling the data becomes relatively simple.

## Build

Information on how to build pyRACF is found in the [README.md](../README.md)
This will ultimately be replaced with a pypi version with a prebuilt dll.

## Use

This will evolve over time. Currently the examples found in the sample directory will provide some understanding of how to call the capabilities.

### Add a user

```shell
python3 samples/user/add_squidward.py
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

### Alter a User

```shell
python3 samples/user/alter_squidward.py
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

### Delete a User

```shell
python3 samples/user/delete_squidward.py
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

### Extract a User Profile

```shell
python3 samples/user/extract_squidward.py
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
                    "profile": {
                        "base": {
                            "user": "SQUIDWRD",
                            "name": "SQUIDWARD",
                            "owner": "LEONARD",
                            "created": 23.033,
                            "defaultgroup": "SYS1",
                            "passdate": 0.0,
                            "passinterval": 186,
                            "phrasedate": null,
                            "attributes": [
                                "OPERATIONS"
                            ],
                            "revokedate": null,
                            "resumedate": null,
                            "lastaccess": "23.033/11:48:10",
                            "classauthorizations": null,
                            "logonalloweddays": "ANYDAY",
                            "logonallowedtime": "ANYTIME",
                            "group": "SYS1",
                            "auth": "USE",
                            "connectowner": "LEONARD",
                            "connectdate": 23.033,
                            "connects": 0,
                            "uacc": null,
                            "lastconnect": "UNKNOWN",
                            "connectattributes": null,
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

### Add a General Resource Profile

```shell
python3 samples/genprof/add_kruskrab.py
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

### Alter a General Resource Profile

```shell
python3 samples/genprof/alter_kruskrab.py
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

### Delete a General Resource Profile

```shell
python3 samples/genprof/delete_kruskrab.py
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

### Extract a General Resource Profile

```shell
python3 samples/genprof/extract_kruskrab.py
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

### Add a Dataset Profile

```shell
python3 samples/dataset/add_testdsd.py
```

```json
{
    "securityresult": {
        "dataset": {
            "name": "ESWIFT.TEST.T1136242.P3020470",
            "operation": "set",
            "generic": "no",
            "requestid": "DatasetRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "ADDSD                ('ESWIFT.TEST.T1136242.P3020470') "
                },
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (None) OWNER       (eswift)"
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

### Alter a Dataset Profile

```shell
python3 samples/dataset/alter_testdsd.py
```

```json
{
    "securityresult": {
        "dataset": {
            "name": "ESWIFT.TEST.T1136242.P3020470",
            "operation": "set",
            "generic": "no",
            "requestid": "DatasetRequest",
            "info": [
                "Definition exists. Add command skipped due  to precheck option"
            ],
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (Read) OWNER       (eswift)"
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

### Delete a Dataset Profile

```shell
python3 samples/dataset/delete_testdsd.py
```

```json
{
    "securityresult": {
        "dataset": {
            "name": "ESWIFT.TEST.T1136242.P3020470",
            "operation": "del",
            "generic": "no",
            "requestid": "DatasetRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "DELDSD               ('ESWIFT.TEST.T1136242.P3020470') "
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```

### Extract a Dataset Profile

```shell
python3 samples/dataset/extract_testdsd.py
```

```json
{
    "securityresult": {
        "dataset": {
            "name": "ESWIFT.TEST.T1136242.P3020470",
            "operation": "listdata",
            "generic": "no",
            "requestid": "DatasetRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "LISTDSD  DATASET     ('ESWIFT.TEST.T1136242.P3020470') ",
                    "message": "NO INSTALLATION DATA",
                    "profile": {
                        "base": {
                            "level": 0,
                            "owner": "eswift",
                            "universal access": "read",
                            "warning": null,
                            "erase": null,
                            "auditing": "failures(read)",
                            "notify": null,
                            "your access": "alter",
                            "creation group": "sys1",
                            "dataset type": "non-vsam",
                            "volumes on which dataset resides": "usrat2",
                            "installation data": null
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

### Add a Profile Permission

```shell
python3 samples/access/add_my_access.py
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

### Alter a Profile Permission

```shell
python3 samples/access/alter_my_access.py
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

### Delete a Profile Permission

```shell
python3 samples/access/delete_my_access.py
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

### Set a RACF Option

```shell
python3 samples/setropts/setr_do_cmd.py
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

### List the RACF Options

```shell
python3 samples/setropts/setr_list.py
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

### `UserAdmin` getters and setters

#### `is_special` special getter

```python
>>> from user.UserAdmin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.is_special("squidwrd")
False
```

#### `set_special` speciall setter

```python
>>> from user.UserAdmin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_special("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'commands': [{'safreturncode': 8, 'returncode': 16, 'reasoncode': 8, 'image': 'ADDUSER SQUIDWRD ', 'messages': ['IKJ56702I INVALID USERID, SQUIDWRD']}, {'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  SPECIAL     '}]}, 'returncode': 4, 'reasoncode': 4}}
```

#### `get_uid` uid getter

```python
>>> from user.UserAdmin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_uid("squidwrd")
2424
```

#### `set_uid` uid setter

```python
>>> from user.UserAdmin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_uid("squidwrd", 1919)
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'commands': [{'safreturncode': 8, 'returncode': 16, 'reasoncode': 8, 'image': 'ADDUSER SQUIDWRD ', 'messages': ['IKJ56702I INVALID USERID, SQUIDWRD']}, {'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (UID         (1919))'}]}, 'returncode': 4, 'reasoncode': 4}}
```

### `ResourceAdmin` getters and setters

#### `get_uacc` uacc getter

```python
>>> from genprof.ResourceAdmin import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_uacc("BIKINI.BOTTOM.KRUSKRAB","FACILITY")
'read'
```

#### `set_uacc` uacc setter

```python
>>> from genprof.ResourceAdmin import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.set_uacc("BIKINI.BOTTOM.KRUSKRAB","FACILITY","ALTER")
{'securityresult': {'resource': {'name': 'BIKINI.BOTTOM.KRUSKRAB', 'class': 'FACILITY', 'operation': 'set', 'requestid': 'ResourceRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'RALTER  FACILITY             (BIKINI.BOTTOM.KRUSKRAB)  UACC        (ALTER)', 'messages': ['ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.'], 'message': 'ICH11009I RACLISTED PROFILES FOR FACILITY WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.'}]}, 'returncode': 0, 'reasoncode': 0}}
```

#### `get_your_acc`

```python
>>> from genprof.ResourceAdmin import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_your_acc("BIKINI.BOTTOM.KRUSKRAB","FACILITY")
'read'
```

### `DatasetAdmin` getters and setters

#### `get_uacc`

```python
>>> from dataset.DatasetAdmin import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.get_uacc("ESWIFT.TEST.T1136242.P3020470")
'alter'
```

#### `set_uacc`

```python
>>> from dataset.DatasetAdmin import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.set_uacc("ESWIFT.TEST.T1136242.P3020470","READ")
{'securityresult': {'dataset': {'name': 'ESWIFT.TEST.T1136242.P3020470', 'operation': 'set', 'generic': 'no', 'requestid': 'DatasetRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': "ALTDSD               ('ESWIFT.TEST.T1136242.P3020470')  UACC        (READ)"}]}, 'returncode': 0, 'reasoncode': 0}}
```

#### `get_your_acc` access getter

```python
>>> from dataset.DatasetAdmin import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.get_your_acc("ESWIFT.TEST.T1136242.P3020470")
'alter'
```

### `SetroptsAdmin` getters and setters

#### `get_password_rules`

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
