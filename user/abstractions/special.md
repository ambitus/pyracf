---
layout: default
grand_parent: User Admin
parent: Abstractions
---

# Special Authority

User Administration functions for accessing and modifying a user's RACF Special Authority. 
{: .fs-6 .fw-300 }

## `UserAdmin.has_special_authority()`

```python
def has_special_authority(self, userid: str) -> Union[bool, bytes]:
```

#### 📄 Description

&nbsp;

{: .note }
> _Having **RACF Special** authority is analogous to having **Root** authority on Linux._

&nbsp;

Check if a user has **RACF Special** authority.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user whose authority is being checked.

#### 📤 Returns
* `Union[bool, bytes]`<br>
  Returns `True` when the user has **RACF Special** authority and `False` otherwise. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

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
>>> user_admin.has_special_authority("squidwrd")
False
```

## `UserAdmin.give_special_authority()`

```python
def give_special_authority(self, userid: str) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .note }
> _Having **RACF Special** authority is analogous to having **Root** authority on Linux._

&nbsp;

Give a user **RACF Special** authority.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to give **RACF Special** authority.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

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
>>> user_admin.give_special_authority("squidwrd")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  SPECIAL     '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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
            "image": "ALTUSER SQUIDWRD  SPECIAL     "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `UserAdmin.take_away_special_authority()`

```python
def take_away_special_authority(self, userid: str) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .note }
> _Having **RACF Special** authority is analogous to having **Root** authority on Linux._

&nbsp;

Take away a user's **RACF Special** authority.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to take **RACF Special** authority away from.

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
>>> user_admin.take_away_special_authority("squidwrd")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  NOSPECIAL     '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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
            "image": "ALTUSER SQUIDWRD  NOSPECIAL     "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```