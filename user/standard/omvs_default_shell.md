---
layout: default
grand_parent: User Admin
parent: Standard
---

# z/OS Unix System Services Default Shell

User administration functions for accessing and modifying a user's z/OS Unix System Services Default Shell. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_omvs_default_shell()`

```python
def get_omvs_default_shell(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

&nbsp;

{: .stable }
> 

&nbsp;

Get a user's **z/OS Unix System Services Default Shell**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Default Shell** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **z/OS Unix System Services Default Shell** or `None` if it is not set or if the user does not have an **OMVS segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_omvs_default_shell("squidwrd")
'/bin/sh'
```

## `UserAdmin.set_omvs_default_shell()`

```python
def set_omvs_default_shell(
    self, userid: str, default_shell: Union[str, bool]
) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .stable }
> 

&nbsp;

Change a user's **z/OS Unix System Services Default Shell**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Default Shell** is being changed.

* `default_shell`<br>
  The filesystem path to the **z/OS Unix System Services Default Shell** set for the specified user or `False` to delete the current value.

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
>>> user_admin.set_omvs_default_shell("squidwrd", "/bin/bash")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': "ALTUSER SQUIDWRD  OMVS     (PROGRAM     ('/bin/bash'))"}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  OMVS     (PROGRAM     ('/bin/bash'))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```