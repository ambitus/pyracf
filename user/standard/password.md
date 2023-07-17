---
layout: default
grand_parent: User Admin
parent: Standard
---

# Password

User administration functions for modifying a user's password. 
{: .fs-6 .fw-300 }

## `UserAdmin.set_password()`
<br>

{: .warning }
> * _All occurances of the specified password in the returned **Security Result Steps dictionary** or **Concatenated Security Request XML string** are redacted._
> * _When the `debug` class attribute is `True`, all occurances of the specified password will be redacted in debug messages produced by this function._

<br>
```python
def set_password(self, userid: str, password: str) -> dict:
```

#### 📄 Description

Change a user's **password**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user who's **password** is being changed.

* `password`<br>
  The **password** to assigned to the specified user.

#### 📤 Returns

* `Union[dict,str]`<br>
  Returns a **Security Result Steps dictionary** or a **Concatenated Security Request XML string** if the `UserAdmin.generate_requests_only` class attribute is `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_password("squidwrd", "K29521IO")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  PASSWORD    (********)'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  PASSWORD    (********)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```