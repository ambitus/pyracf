---
layout: default
grand_parent: User Admin
parent: Abstractions
---

# Owner

User Administration functions for accessing and modifying a user's Owner. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_owner()`

```python
def get_owner(self, userid: str) -> Union[str, bytes]:
```

#### 📄 Description

Get a user's **Owner**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **Owner** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **Owner**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_owner("squidwrd")
'ekrabs'
```

## `UserAdmin.set_owner()`

```python
def set_owner(self, userid: str, name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Set a user's **Owner**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **Owner** is being set.

* `revoke_date`<br>
  The **Owner** to set for the specified user.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_owner("squidwrd", "plankton")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  OWNER       (plankton)'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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
            "image": "ALTUSER SQUIDWRD  OWNER       (plankton)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```