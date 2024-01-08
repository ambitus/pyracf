---
layout: default
grand_parent: User Admin
parent: Abstractions
---

# TSO Logon Procedure

User Administration functions for accessing and modifying a user's TSO Logon Procedure. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_tso_logon_procedure()`

```python
def get_tso_logon_procedure(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

Get a user's **TSO Logon Procedure**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **TSO Logon Procedure** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **TSO Logon Procedure** or `None` if it is not set or if the user does not have a **TSO segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_tso_logon_procedure("squidwrd")
'proc'
```

## `UserAdmin.set_tso_logon_procedure()`

```python
def set_tso_logon_procedure(
    self, userid: str, logon_procedure: Union[str, bool]
) -> Union[dict, bytes]:
```

#### 📄 Description

Change a user's **TSO Logon Procedure**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **TSO Logon Procedure** is being changed.

* `logon_procedure`<br>
  The **TSO Logon Procedure** to set for the specified user or `False` to delete the current value.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_tso_logon_procedure("squidwrd", "TOASTER")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  TSO      (PROC        (TOASTER))'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "user": {
        "name": "SQUIDWRD",
        "operation": "set",
        "requestId": "UserRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "ALTUSER SQUIDWRD  TSO      (PROC        (TOASTER))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```