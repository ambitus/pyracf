---
layout: default
grand_parent: General Resource Admin
parent: Abstractions
---

# Auditing Rules

General Resource Profile Administration functions for manipulating a General Resource Profile's Auditing Rules. 
{: .fs-6 .fw-300 }

## `ResourceAdmin.get_audit_rules()`

```python
def get_audit_rules(self, resource: str, class_name: str) -> Union[dict, bytes, None]:
```

#### 📄 Description

Check the **Audit Rules** for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should check the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being checked belongs to.

#### 📤 Returns
* `Union[dict, bytes, None]`<br>
  Returns `None` when the general resource profile has no **Auditing Rules** defined, otherwise returns the auditing rules as a dictionary. If the `ResourceAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_audit_rules("TESTING","ELIJTEST")
{"success": "update", "failures": "read"}
```

## `ResourceAdmin.clear_audit_successes()`

```python
def clear_audit_successes(self, resource: str, class_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any `Success` rules defined within the **Audit Rules** for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.clear_audit_successes("TESTING","ELIJTEST")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"success":"update","failures":"read"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( FAILURE (READ        ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "success": "update",
                    "failures": "read"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( FAILURE (READ        ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.clear_audit_failures()`

```python
def clear_audit_failures(self, resource: str, class_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any `Failures` rules defined within the **Audit Rules** for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.clear_audit_failures("TESTING","ELIJTEST")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"success":"update","failures":"read"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "success": "update",
                    "failures": "read"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.clear_audit_both_successes_and_failures()`

```python
def clear_audit_both_successes_and_failures(
    self,
    resource: str,
    class_name: str
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any `All` rules defined within the **Audit Rules** for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.clear_audit_both_successes_and_failures("TESTING","ELIJTEST")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"all":"read","success":"control"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (CONTROL     ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "all": "read",
                    "success": "control"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (CONTROL     ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.clear_all_audit_rules()`

```python
def clear_all_audit_rules(self, resource: str, class_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.clear_all_audit_rules("TESTING","ELIJTEST")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( NONE    )","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( NONE    )",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.overwrite_audit_by_successes()`

```python
def overwrite_audit_by_successes(
    self,
    resource: str,
    class_name: str,
    audit_success: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile and replace them with a `Success` rule.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `audit_success`<br>
  The **access_level** for which successes shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_successes("TESTING","ELIJTEST","alter")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (alter       ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (alter       ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.overwrite_audit_by_failures()`

```python
def overwrite_audit_by_failures(
    self,
    resource: str,
    class_name: str,
    audit_failures: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile and replace them with a `Failure` rule.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `audit_success`<br>
  The **access_level** for which failures shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_failures("TESTING","ELIJTEST","control")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( FAILURE (control     ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( FAILURE (control     ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.overwrite_audit_by_both_successes_and_failures()`

```python
def overwrite_audit_by_both_successes_and_failures(
    self,
    resource: str,
    class_name: str,
    audit_both: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile and replace them with an `All` rule.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `audit_success`<br>
  The **access_level** for which both successes and failures shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_both_successes_and_failures("TESTING","ELIJTEST","update")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( ALL     (update      ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( ALL     (update      ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.overwrite_audit_by_audit_alter_access()`

```python
def overwrite_audit_by_audit_alter_access(
    self,
    resource: str,
    class_name: str,
    access_attempt: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile and replace them with a rule auditing `alter` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `access_attempt`<br>
  The type of **attempt** (Success/Failure/All) for which alter access shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_audit_alter_access("TESTING","ELIJTEST","success")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( success (ALTER       ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( success (ALTER       ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.overwrite_audit_by_audit_control_access()`

```python
def overwrite_audit_by_audit_control_access(
    self,
    resource: str,
    class_name: str,
    access_attempt: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile and replace them with a rule auditing `control` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `access_attempt`<br>
  The type of **attempt** (Success/Failure/All) for which control access shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_audit_control_access("TESTING","ELIJTEST","failure")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( failure (CONTROL     ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( failure (CONTROL     ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.overwrite_audit_by_audit_read_access()`

```python
def overwrite_audit_by_audit_read_access(
    self,
    resource: str,
    class_name: str,
    access_attempt: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile and replace them with a rule auditing `read` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `access_attempt`<br>
  The type of **attempt** (Success/Failure/All) for which read access shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_audit_read_access("TESTING","ELIJTEST","success")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( success (READ        ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( failure (READ        ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.overwrite_audit_by_audit_update_access()`

```python
def overwrite_audit_by_audit_update_access(
    self,
    resource: str,
    class_name: str,
    access_attempt: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile and replace them with a rule auditing `update` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `access_attempt`<br>
  The type of **attempt** (Success/Failure/All) for which update access shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_audit_update_access("TESTING","ELIJTEST","failure")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( all     (UPDATE     ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( all     (UPDATE      ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.alter_audit_by_successes()`

```python
def alter_audit_by_successes(
    self,
    resource: str,
    class_name: str,
    audit_success: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Preserves any rules defined within the **Audit Rules** for a general resource profile and add a new a `Success` rule.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `audit_success`<br>
  The **access_level** for which successes shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_successes("TESTING","ELIJTEST","control")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"success":"update","failures":"read"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) SUCCESS (CONTROL     ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "success": "update",
                    "failures": "read"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) SUCCESS (CONTROL     ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.alter_audit_by_failures()`

```python
def alter_audit_by_failures(
    self,
    resource: str,
    class_name: str,
    audit_failures: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Preserves any rules defined within the **Audit Rules** for a general resource profile and add a new a `Failure` rule.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `audit_success`<br>
  The **access_level** for which failures shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_failures("TESTING","ELIJTEST","control")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"success":"update","failures":"read"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) FAILURE (CONTROL     ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "success": "update",
                    "failures": "read"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) FAILURE (CONTROL     ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.alter_audit_by_both_successes_and_failures()`

```python
def alter_audit_by_both_successes_and_failures(
    self,
    resource: str,
    class_name: str,
    audit_both: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Preserves any rules defined within the **Audit Rules** for a general resource profile and add a new an `All` rule.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `audit_success`<br>
  The **access_level** for which both successes and failures shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_both_successes_and_failures("TESTING","ELIJTEST","update")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"all":"read","success":"control"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (CONTROL     ) ALL     (READ        ) ALL     (UPDATE     ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "all": "read",
                    "success": "control"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (CONTROL     ) ALL     (READ        ) ALL     (UPDATE     ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.alter_audit_by_audit_alter_access()`

```python
def alter_audit_by_audit_alter_access(
    self,
    resource: str,
    class_name: str,
    access_attempt: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Preserves any rules defined within the **Audit Rules** for a general resource profile and add a new a rule auditing `alter` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `access_attempt`<br>
  The type of **attempt** (Success/Failure/All) for which alter access shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_audit_alter_access("TESTING","ELIJTEST","success")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"success":"update","failures":"read"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) success (ALTER       ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "success": "update",
                    "failures": "read"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) success (ALTER       ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.alter_audit_by_audit_control_access()`

```python
def alter_audit_by_audit_control_access(
    self,
    resource: str,
    class_name: str,
    access_attempt: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Preserves any rules defined within the **Audit Rules** for a general resource profile and add a new a rule auditing `control` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `access_attempt`<br>
  The type of **attempt** (Success/Failure/All) for which control access shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_audit_control_access("TESTING","ELIJTEST","success")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"success":"update","failures":"read"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) success (CONTROL     ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "success": "update",
                    "failures": "read"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) success (CONTROL     ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.alter_audit_by_audit_read_access()`

```python
def alter_audit_by_audit_read_access(
    self,
    resource: str,
    class_name: str,
    access_attempt: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Preserves any rules defined within the **Audit Rules** for a general resource profile and add a new a rule auditing `read` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `access_attempt`<br>
  The type of **attempt** (Success/Failure/All) for which read access shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_audit_read_access("TESTING","ELIJTEST","success")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"success":"update","failures":"read"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) success (READ        ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "success": "update",
                    "failures": "read"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) success (READ        ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `ResourceAdmin.alter_audit_by_audit_update_access()`

```python
def alter_audit_by_audit_update_access(
    self,
    resource: str,
    class_name: str,
    access_attempt: str,
) -> Union[dict, bytes]:
```

#### 📄 Description

Preserves any rules defined within the **Audit Rules** for a general resource profile and add a new a rule auditing `update` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `access_attempt`<br>
  The type of **attempt** (Success/Failure/All) for which update access shall be audited.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_audit_update_access("TESTING","ELIJTEST","failure")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"success":"update","failures":"read"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}},"step2":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( FAILURE (READ        ) failure (UPDATE      ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "listdata",
        "requestId": "ResourceRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RLIST   ELIJTEST             (TESTING) ",
            "profiles": [
              {
                "base": {
                  "class": "elijtest",
                  "name": "testing",
                  "level": 0,
                  "owner": "eswift",
                  "universalAccess": "read",
                  "yourAccess": "read",
                  "warning": null,
                  "installationData": null,
                  "applicationData": null,
                  "auditing": {
                    "success": "update",
                    "failures": "read"
                  },
                  "notify": null,
                  "generic": false
                }
              }
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
    "securityResult": {
      "resource": {
        "name": "TESTING",
        "class": "ELIJTEST",
        "operation": "set",
        "requestId": "ResourceRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "RALTER  ELIJTEST             (TESTING)  AUDIT( FAILURE (READ        ) failure (UPDATE      ))",
            "messages": [
              "ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
            ]
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```