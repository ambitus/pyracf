---
layout: default
grand_parent: User Admin
parent: Standard
---

# z/OS Unix System Services Max CPU Time

User administration functions for accessing and modifying a user's z/OS Unix System Services Max CPU Time. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_omvs_max_cpu_time()`

```python
def get_omvs_max_cpu_time(self, userid: str) -> Union[int, None, bytes]:
```

#### 📄 Description

Get a user's **z/OS Unix System Services Max CPU Time**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Max CPU Time** is being requested.

#### 📤 Returns
* `Union[int, None, bytes]`<br>
  Returns the user's **z/OS Unix System Services Max CPU Time** or `None` if it is not set or if the user does not have an **OMVS segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_omvs_max_cpu_time("squidwrd")
1500
```

## `UserAdmin.set_omvs_max_cpu_time()`

```python
def set_omvs_max_cpu_time(
    self, userid: str, max_cpu_time: Union[int, bool]
) -> Union[dict, bytes]:
```

#### 📄 Description

Change a user's **z/OS Unix System Services Max CPU Time**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **z/OS Unix System Services Max CPU Time** is being set.

* `max_cpu_time`<br>
  The **z/OS Unix System Services Max CPU Time** to set for the specified user or `False` to delete the current value.

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
>>> user_admin.set_omvs_max_cpu_time("squidwrd", 3000)
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (CPUTIMEMAX  (3000))'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  OMVS     (CPUTIMEMAX  (3000))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```