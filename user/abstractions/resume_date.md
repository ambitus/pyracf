---
layout: default
grand_parent: User Admin
parent: Abstractions
---

# Resume Date

User Administration functions for accessing and modifying a user's Resume Date. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_resume_date()`

```python
def get_resume_date(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

Get a user's **Resume Date**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **Resume Date** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **Resume Date** or `None` if it is not set. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_resume_date("squidwrd")
'11/2/2023'
```

## `UserAdmin.set_resume_date()`

```python
def set_resume_date(self, userid: str, resume_date: Union[str, bool]) -> Union[dict, bytes]:
```

#### 📄 Description

Set a user's **Resume Date**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **Resume Date** is being set.

* `revoke_date`<br>
  The **Resume Date** to set for the specified user or `False` to delete the current value.

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
>>> user_admin.set_resume_date("squidwrd", "11/13/23")
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
            "image": "ALTUSER SQUIDWRD  RESUME      (11/13/23)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```