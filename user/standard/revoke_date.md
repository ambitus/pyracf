---
layout: default
grand_parent: User Admin
parent: Standard
---

# Revoke Date

User administration functions for accessing and modifying a user's Revoke Date. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_revoke_date()`

```python
def get_revoke_date(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

&nbsp;

{: .stable }
> 

&nbsp;

Get a user's **Revoke Date**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **Revoke Date** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **Revoke Date** or `None` if it is not set. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_revoke_date("squidwrd")
'10/22/2023'
```

## `UserAdmin.set_revoke_date()`

```python
def set_revoke_date(self, userid: str, revoke_date: Union[str, bool]) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .stable }
> 

&nbsp;

Set a user's **Revoke Date**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **Revoke Date** is being set.

* `revoke_date`<br>
  The **Revoke Date** to set for the specified user or `False` to delete the current value.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_revoke_date("squidwrd", "10/23/23")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  REVOKE      (10/23/23)'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  REVOKE      (10/23/23)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```