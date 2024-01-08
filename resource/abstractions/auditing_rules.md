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
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_audit_rules("TESTING","ELIJTEST")
{"success": "update", "failures": "read"}
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
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.
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

## `ResourceAdmin.overwrite_audit_by_attempt()`

```python
def overwrite_audit_by_attempt(
    self,
    resource: str,
    class_name: str,
    successes: Union[str, None] = None,
    failure: Union[str, None] = None,
    all: Union[str, None] = None,
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile and replace them with `Success`, `Failure`, or `All` rule(s).

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `success`<br>
  The **access_level** for which successes shall be audited. Ignore this operand to specify a different "attempt" type.

* `failure`<br>
  The **access_level** for which failures shall be audited. Ignore this operand to specify a different "attempt" type.

* `all`<br>
  The **access_level** for which both successes and failures shall be audited. Ignore this operand to specify a different "attempt" type.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_attempt("TESTING","ELIJTEST",success="alter")
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

## `ResourceAdmin.overwrite_audit_by_access_level()`

```python
def overwrite_audit_by_access_level(
    self,
    resource: str,
    class_name: str,
    alter: Union[str, None] = None,
    control: Union[str, None] = None,
    read: Union[str, None] = None,
    update: Union[str, None] = None,
) -> Union[dict, bytes]:
```

#### 📄 Description

Clear any rules defined within the **Audit Rules** for a general resource profile and replace them with a rule auditing `alter`, `control`, `read`, or `update` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `alter`<br>
  The type of **attempt** (Success/Failure/All) for which alter access shall be audited. Ignore this operand to specify a different "access level".

* `control`<br>
  The type of **attempt** (Success/Failure/All) for which control access shall be audited. Ignore this operand to specify a different "access level".

* `read`<br>
  The type of **attempt** (Success/Failure/All) for which read access shall be audited. Ignore this operand to specify a different "access level".

* `update`<br>
  The type of **attempt** (Success/Failure/All) for which update access shall be audited. Ignore this operand to specify a different "access level".

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_access_leve("TESTING","ELIJTEST",alter="success")
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

## `ResourceAdmin.alter_audit_by_attempt()`

```python
def alter_audit_by_attempt(
    self,
    resource: str,
    class_name: str,
    success: Union[str, None] = None,
    failure: Union[str, None] = None,
    all: Union[str, None] = None,
) -> Union[dict, bytes]:
```

#### 📄 Description

Preserves any rules defined within the **Audit Rules** for a general resource profile and add new `Success`, `Failure`, or `All` rule(s).

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `success`<br>
  The **access_level** for which successes shall be audited. Ignore this operand to specify a different "attempt" type.

* `failure`<br>
  The **access_level** for which failures shall be audited. Ignore this operand to specify a different "attempt" type.

* `all`<br>
  The **access_level** for which both successes and failures shall be audited. Ignore this operand to specify a different "attempt" type.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_attempt("TESTING","ELIJTEST",success="control")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) SUCCESS (CONTROL     ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
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

## `ResourceAdmin.alter_audit_by_access_level()`

```python
def alter_audit_by_access_level(
    self,
    resource: str,
    class_name: str,
    alter: Union[str, None] = None,
    control: Union[str, None] = None,
    read: Union[str, None] = None,
    update: Union[str, None] = None,
) -> Union[dict, bytes]:
```

#### 📄 Description

Preserves any rules defined within the **Audit Rules** for a general resource profile and add new rule(s) auditing `alter`, `control`, `read`, or `update` access attempts.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** for which RACF should change the audit rules.

* `class_name`<br>
  The name of the **class** the general resource profile being changed belongs to.

* `alter`<br>
  The type of **attempt** (Success/Failure/All) for which alter access shall be audited. Ignore this operand to specify a different "access level".

* `control`<br>
  The type of **attempt** (Success/Failure/All) for which control access shall be audited. Ignore this operand to specify a different "access level".

* `read`<br>
  The type of **attempt** (Success/Failure/All) for which read access shall be audited. Ignore this operand to specify a different "access level".

* `update`<br>
  The type of **attempt** (Success/Failure/All) for which update access shall be audited. Ignore this operand to specify a different "access level".

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_access_level("TESTING","ELIJTEST",alter="success")
{"step1":{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"set","requestId":"ResourceRequest","info":["Definition exists. Add command skipped due  to precheck option"],"commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RALTER  ELIJTEST             (TESTING)  AUDIT( SUCCESS (UPDATE      ) FAILURE (READ        ) success (ALTER       ))","messages":["ICH11009I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}}
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
