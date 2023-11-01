---
layout: default
grand_parent: User Admin
parent: Standard
---

# z/OS Unix System Services Max Address Space Size

User administration functions for accessing and modifying a user's z/OS Unix System Services Max Address Space Size. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_omvs_max_address_space_size()`

```python
def get_omvs_max_address_space_size(self, userid: str) -> Union[int, None, bytes]:
```

#### 📄 Description

Get a user's **z/OS Unix System Services Max Address Space Size**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Max Address Space Size** is being requested.

#### 📤 Returns
* `Union[int, None, bytes]`<br>
  Returns the user's **z/OS Unix System Services Max Address Space Size** or `None` if it is not set or if the user does not have an **OMVS segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_omvs_max_address_space_size("squidwrd")
10485760
```

## `UserAdmin.set_omvs_max_address_space_size()`

```python
def set_omvs_max_address_space_size(
    self, userid: str, max_address_space_size: Union[int, bool]
) -> Union[dict, bytes]:
```

#### 📄 Description

Change a user's **z/OS Unix System Services Max Address Space Size**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Max Address Space Size** is being set.

* `max_address_space_size`<br>
  The **z/OS Unix System Services Max Address Space Size** to set for the specified user or `False` to delete the current value.

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
>>> user_admin.set_omvs_max_address_space_size("squidwrd", 20971520)
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (ASSIZEMAX   (20971520))'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  OMVS     (ASSIZEMAX   (20971520))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```