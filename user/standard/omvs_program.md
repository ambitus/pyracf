---
layout: default
grand_parent: User Admin
parent: Standard
---

# z/OS Unix System Services Program

User administration functions for accessing and modifying a user's z/OS Unix System Services Program/Default Shell. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_omvs_program()`

```python
def get_omvs_program(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

Get a user's **z/OS Unix System Services Program/Default Shell**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Program/Default Shell** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **z/OS Unix System Services Program/Default Shell** or `None` if the user does not have an **OMVS segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_omvs_program("squidwrd")
'/bin/sh'
```

## `UserAdmin.set_omvs_program()`

```python
def set_omvs_program(self, userid: str, program: str) -> Union[dict, bytes]:
```

#### 📄 Description

Change a user's **z/OS Unix System Services Program/Default Shell**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Program/Default Shell** is being changed.

* `program`<br>
  The filesystem path to the **z/OS Unix System Services Program/Default Shell** to assign to the specified user.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does not exist in the environment.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_omvs_program("squidwrd", "/bin/sh")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': "ALTUSER SQUIDWRD  OMVS     (PROGRAM     ('/bin/sh'))"}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  OMVS     (PROGRAM     ('/bin/sh'))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```