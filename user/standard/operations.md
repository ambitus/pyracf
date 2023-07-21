---
layout: default
grand_parent: User Admin
parent: Standard
---

# Operations Authority

User administration functions for accessing and modifying a user's Operations Authority. 
{: .fs-6 .fw-300 }

## `UserAdmin.has_operations_authority()`

```python
def has_operations_authority(self, userid: str) -> Union[bool, bytes]:
```

#### 📄 Description

Check if a user has **Operations** authority.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user who's authority is being checked.

#### 📤 Returns
* `Union[bool, bytes]`<br>
  Returns `True` when the user has **Operations** authority and `False` otherwise. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.has_operations_authority("squidwrd")
False
```

## `UserAdmin.give_operations_authority()`

```python
def give_operations_authority(self, userid: str) -> Union[dict, bytes]:
```

#### 📄 Description

Give a user **Operations** authority.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to give **Operations** authority.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **return code** or **reason code** of a **Security Result** is not equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.give_operations_authority("squidwrd")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  OPERATIONS  '}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  OPERATIONS  "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `UserAdmin.take_away_operations_authority()`

```python
def take_away_operations_authority(self, userid: str) -> Union[dict, bytes]:
```

#### 📄 Description

Remove a user's **Operations** authority.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to take **Operator** authority away from.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **return code** or **reason code** of a **Security Result** is not equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.take_away_operations_authority("squidwrd")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  NOOPERATIONS  '}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  NOOPERATIONS  "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```