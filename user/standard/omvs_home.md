---
layout: default
grand_parent: User Admin
parent: Standard
---

# z/OS Unix System Services Home

User administration functions for accessing and modifying a user's z/OS Unix System Services Home Directory. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_omvs_home()`

```python
def get_omvs_home(self, userid: str) -> Union[str, None]:
```

#### 📄 Description

Get a user's **z/OS Unix System Services Home Directory**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user who's **z/OS Unix System Services Home Directory** is being requested.

#### 📤 Returns
* `Union[str, None]`<br>
  Returns the user's **z/OS Unix System Services Home Directory** or `None` if the user does not have an **OMVS segment**.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_omvs_home("squidwrd")
'/u/squidwrd'
```

## `UserAdmin.set_omvs_home()`

```python
def set_omvs_home(self, userid: str, home_directory: str) -> dict:
```

#### 📄 Description

Change a user's **z/OS Unix System Services Home Directory**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user who's **z/OS Unix System Services Home Directory** is being changed.

* `home_directory`<br>
  The **z/OS Unix System Services Home Directory** to assign to the specified user.

#### 📤 Returns
* `Union[dict, str]`<br>
  Returns a **Security Result Steps dictionary** or a **Concatenated Security Request XML string** if the `UserAdmin.generate_requests_only` class attribute is `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_omvs_home("squidwrd", "/u/squidwrd")
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': "ALTUSER SQUIDWRD  OMVS     (HOME        ('/u/squidwrd'))"}]}, 'returnCode': 0, 'reasonCode': 0}}}
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