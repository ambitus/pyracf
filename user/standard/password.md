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

<br>
```python
def set_password(self, userid: str, password: str) -> Union[dict, bytes]:
```

#### 📄 Description

{: .warning }
> * _pyRACF encodes the data it passes to RACF in Code Page IBM-1047._
> * _If you are entering a password with special or national characters, users logging on from terminals using differnt or international codepages may experience errors._
> * _Please consult a list of invariant characters to use for such passwords or phrases if this applies to you._

{: .warning }
> * _All occurances of the specified password in the returned **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** are redacted._
> * _When the `debug` class attribute is `True`, all occurances of the specified password will be redacted in debug messages produced by this function._

Change a user's **password**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **password** is being changed.

* `password`<br>
  The **password** to assigned to the specified user.

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