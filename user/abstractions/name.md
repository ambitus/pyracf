---
layout: default
grand_parent: User Admin
parent: Abstractions
---

# Name

User Administration functions for accessing and modifying a user's Name. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_name()`

```python
def get_name(self, userid: str) -> Union[str, None, bytes]:
```

#### 📄 Description

Get a user's **Name**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **Name** is being requested.

#### 📤 Returns
* `Union[str, None, bytes]`<br>
  Returns the user's **Name** or `None` if it is not set. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

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
>>> user_admin.get_name("squidwrd")
'squidward tentacles'
```

## `UserAdmin.set_name()`

```python
def set_name(self, userid: str, name: Union[str, bool]) -> Union[dict, bytes]:
```

#### 📄 Description

Set a user's **Name**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's **Name** is being set.

* `revoke_date`<br>
  The **Name** to give to the specified user or `False` to delete the current value.

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
>>> user_admin.set_name("squidwrd", "Squidward Tortellini")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': "ALTUSER SQUIDWRD     NAME        ('Squidward Tortellini')"}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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
            "image": "ALTUSER SQUIDWRD     NAME        ('Squidward Tortellini')"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```