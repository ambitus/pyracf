---
layout: default
grand_parent: User Admin
parent: Standard
---

# Auditor Authority

User administration functions for accessing and modifying a user's Auditor Authority. 
{: .fs-6 .fw-300 }

## `UserAdmin.has_auditor_authority()`

```python
def has_auditor_authority(self, userid: str) -> bool:
```

#### 📄 Description

Check if a user has **Auditor** authority.

#### 📥 Parameters
* `userid`<br>
  The userid of the user who's authority is being checked.

#### 📤 Returns
* `bool`<br>
  Returns `True` when the user has **Auditor** authority and `False` otherwise.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.is_auditor("squidwrd")
False
```

## `UserAdmin.give_auditor_authority()`

```python
def give_auditor_authority(self, userid: str) -> dict:
```

#### 📄 Description

Give a user **Auditor** authority.

#### 📥 Parameters
* `userid`<br>
  The userid of the user to give **Auditor** authority.

#### 📤 Returns
* `dict`<br>
  Returns a **Security Result Steps dictionary** or a **Concatenated Security Request XML string** if the `UserAdmin.generate_requests_only` class attribute is `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.give_auditor_authority("squidwrd")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  AUDITOR     '}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  AUDITOR     "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `UserAdmin.take_away_auditor_authority()`

```python
def take_away_auditor_authority(self, userid: str) -> dict:
```

#### 📄 Description

Remove a user's **Auditor** authority.

#### 📥 Parameters
* `userid`<br>
  The userid of the user to take **Auditor** authority away from.

#### 📤 Returns
* `dict`<br>
  Returns a **Security Result Steps dictionary** or a **Concatenated Security Request XML string** if the `UserAdmin.generate_requests_only` class attribute is `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.take_away_auditor_authority("squidwrd")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD  NOAUDITOR     '}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD  NOAUDITOR     "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```