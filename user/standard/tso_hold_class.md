---
layout: default
grand_parent: User Admin
parent: Standard
---

# TSO Hold Class

User administration functions for accessing and modifying a user's TSO Hold Class. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_tso_hold_class()`

```python
def get_tso_hold_class(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

Get a user's **TSO Hold Class**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **TSO Hold Class** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **TSO Hold Class** or `None` if it is not set or if the user does not have a **TSO segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_tso_hold_class("squidwrd")
'A'
```

## `UserAdmin.set_tso_hold_class()`

```python
def set_tso_hold_class(
    self, userid: str, hold_class: Union[str, bool]
) -> Union[dict, bytes]:
```

#### 📄 Description

Change a user's **TSO Hold Class**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **TSO Hold Class** is being changed.

* `hold_class`<br>
  The **TSO Hold Class** to set for the specified user or `False` to delete the current value.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_tso_hold_class("squidwrd", "P")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  TSO      (HOLDCLASS   (P))'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  TSO      (HOLDCLASS   (P))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```