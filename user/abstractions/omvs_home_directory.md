---
layout: default
grand_parent: User Admin
parent: Abstractions
---

# z/OS Unix System Services Home Directory

User Administration functions for accessing and modifying a user's z/OS Unix System Services Home Directory. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_omvs_home_directory()`

```python
def get_omvs_home_directory(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

Get a user's **z/OS Unix System Services Home Directory**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user whose **z/OS Unix System Services Home Directory** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **z/OS Unix System Services Home Directory** or `None` if it is not set or the user does not have an **OMVS segment**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

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
>>> user_admin.get_omvs_home_directory("squidwrd")
'/u/squidwrd'
```

## `UserAdmin.set_omvs_home_directory()`

```python
def set_omvs_home_directory(
    self, userid: str, home_directory: Union[str, bool]
  ) -> Union[dict, bytes]:
```

#### 📄 Description

Change a user's **z/OS Unix System Services Home Directory**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user whose **z/OS Unix System Services Home Directory** is being set.

* `home_directory`<br>
  The **z/OS Unix System Services Home Directory** to set for the specified user or `False` to delete the current value.

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
>>> user_admin.set_omvs_home_directory("squidwrd", "/u/squidwrd")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': "ALTUSER SQUIDWRD  OMVS     (HOME        ('/u/squidwrd'))"}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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
            "image": "ALTUSER SQUIDWRD  OMVS     (HOME        ('/u/squidwrd'))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```