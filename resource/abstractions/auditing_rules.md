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

Get the **Auditing Rules** for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** whose **Auditing Rules** will be requested.

* `class_name`<br>
  The name of the **class** the specified general resource profile belongs to.

#### 📤 Returns
* `Union[dict, bytes, None]`<br>
  Returns `None` when the general resource profile has no **Auditing Rules** defined, otherwise the **Auditing Rules** are returned as a dictionary. If the `ResourceAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_audit_rules("TESTING", "ELIJTEST")
{"success": "update", "failures": "read"}
```

## `ResourceAdmin.remove_all_audit_rules()`

```python
def remove_all_audit_rules(self, resource: str, class_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Remove all **Auditing Rules** defined for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** whose **Auditing Rules** will be removed.

* `class_name`<br>
  The name of the **class** the specified general resource profile belongs to.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.remove_all_audit_rules("TESTING", "ELIJTEST")
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

&nbsp;

{: .note }
> _Valid values for **Access Attempts** are limited to the **Access Level** values of `alter`, `control`, `read`, and `update`._

&nbsp;

{:.warning}
> _Using an **Access Level** value more than once is **NOT** allowed._

&nbsp;

Remove all currently defined **Auditing Rules** for a general resource profile and replace them with the new **Auditing Rules** specified by **Access Attempt**.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** whose **Auditing Rules** will be overwritten.

* `class_name`<br>
  The name of the **class** the specified general resource profile belongs to.

* `success`<br>
  The **Access Level** which **Successes** should be audited for.

* `failure`<br>
  The **Access Level** which **Failures** should be audited for.

* `all`<br>
  The **Access Level** which both **Successes** and **Failures** should be audited for.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `ValueError`<br>
  Raises `ValueError` when values passed for one or more **Access Attempts** do not represent a valid **Access Level** or when two or more **Access Attempts** specify the same **Access Level**.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_attempt("TESTING", "ELIJTEST", success="alter")
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

&nbsp;

{: .note }
> _Valid values for **Access Levels** are limited to the **Access Attempt** values of `success`, `failure`, and `all`._

&nbsp;

Remove all currently defined **Auditing Rules** for a general resource profile and replace them with the new **Auditing Rules** specified by **Access Level**.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** whose **Auditing Rules** will be overwritten.

* `class_name`<br>
  The name of the **class** the specified general resource profile belongs to.

* `alter`<br>
  The type of **Access Attempt** which **Alter** attempts should be audited for.

* `control`<br>
  The type of **Access Attempt** which **Control** attempts should be audited for.

* `read`<br>
  The type of **Access Attempt** which **Read** attempts should be audited for.

* `update`<br>
  The type of **Access Attempt** which **Update** attempts should be audited for.


#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.overwrite_audit_by_access_leve("TESTING", "ELIJTEST", alter="success")
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

&nbsp;

{: .note }
> _Valid values for **Access Attempts** are limited to the **Access Level** values of `alter`, `control`, `read`, and `update`._

&nbsp;

{:.warning}
> _Using an **Access Level** value more than once is **NOT** allowed._

&nbsp;

Alter the **Auditing Rules** of a general resource profile specified by **Access Attempt**.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** whose **Auditing Rules** will be altered.

* `class_name`<br>
  The name of the **class** the specified general resource profile belongs to.

* `success`<br>
  The **Access Level** which **Successes** should be audited for.

* `failure`<br>
  The **Access Level** which **Failures** should be audited for.

* `all`<br>
  TThe **Access Level** which both **Successes** and **Failures** should be audited for.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `ValueError`<br>
  Raises `ValueError` when values passed for one or more **Access Attempts** do not represent a valid **Access Level** or when two or more **Access Attempts** specify the same **Access Level**.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_attempt("TESTING", "ELIJTEST", success="control")
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

&nbsp;

{: .note }
> _Valid values for **Access Levels** are limited to the **Access Attempt** values of `success`, `failure`, and `all`._

&nbsp;

Alter the **Auditing Rules** of a general resource profile specified by **Access Level**.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** whose **Auditing Rules** will be altered.

* `class_name`<br>
  The name of the **class** the specified general resource profile belongs to.

* `alter`<br>
  The type of **Access Attempt** which **Alter** attempts should be audited for.

* `control`<br>
  The type of **Access Attempt** which **Control** attempts should be audited for.

* `read`<br>
  The type of **Access Attempt** which **Read** attempts should be audited for.

* `update`<br>
  The type of **Access Attempt** which **Update** attempts should be audited for.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **general resource profile** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.alter_audit_by_access_level("TESTING", "ELIJTEST", alter="success")
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
