---
layout: default
grand_parent: User Admin
parent: Standard
---

# Class Authorizations

User administration functions for accessing and modifying a user's Class Authorizations. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_class_authorizations()`

```python
  def get_class_authorizations(self, userid: str) -> List[str]:
```

#### 📄 Description

Get a user's **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user who's **Class Authorizations** is being requested.

#### 📤 Returns
* `List[str]`<br>
  Returns the user's **Class Authorizations**.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_class_authorizations("squidwrd")
['facility', 'terminal', 'xfacilit']
```

## `UserAdmin.set_class_authorizations()`

```python
def set_class_authorizations(
    self, userid: str, class_authorizations: List[str]
) -> dict:
```

#### 📄 Description

Overwrite a user's existing **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user who's **Class Authorizations** are being overwritten.

* `class_authorizations`<br>
  A list of one or more **Class Authorizations** that will become the user's new **Class Authorizations**.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result Steps dictionary** or a **Concatenated Security Request XML string** if the `UserAdmin.generate_requests_only` class attribute is `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_class_authorizations("squidwrd", ["facility", "terminal", "xfacilit"])
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD   NOCLAUTH      (terminal xfacilit)'}]}, 'returnCode': 0, 'reasonCode': 0}}, 'step2': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD     CLAUTH      (facility terminal xfacilit)'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD   NOCLAUTH      (terminal xfacilit)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  },
  "step2": {
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
            "image": "ALTUSER SQUIDWRD     CLAUTH      (facility terminal xfacilit)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `UserAdmin.add_class_authorizations()`

```python
def add_class_authorizations(
    self, userid: str, class_authorizations: Union[str, List[str]]
) -> dict:
```

#### 📄 Description

Add new **Class Authorizations** to a user's existing **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user to add **Class Authorizations** to.

* `class_authorizations`<br>
  <br>

  {: .note }
  > _May be a **string value** or a **list of string values**._

  <br>
  One or more **Class Authorazitons** to add. 

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result Steps dictionary** or a **Concatenated Security Request XML string** if the `UserAdmin.generate_requests_only` class attribute is `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.add_class_authorizations("squidwrd", ["terminal", "xfacilit"])
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD     CLAUTH      (terminal xfacilit)'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD     CLAUTH      (terminal xfacilit)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `UserAdmin.remove_class_authorizations()`

```python
def remove_class_authorizations(
    self, userid: str, class_authorizations: Union[str, List[str]]
) -> dict:
```

#### 📄 Description

Remove **Class Authorizations** to a user's existing **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user to remove **Class Authorizations** from.

* `class_authorizations`<br>
  <br>

  {: .note }
  > _May be a **string value** or a **list of string values**._

  <br>
  One or more **Class Authorazitons** to remove.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result Steps dictionary** or a **Concatenated Security Request XML string** if the `UserAdmin.generate_requests_only` class attribute is `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.remove_class_authorizations("squidwrd", ["facility", "terminal"])
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD   NOCLAUTH      (facility terminal)'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD   NOCLAUTH      (facility terminal)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `UserAdmin.delete_all_class_authorizations()`

```python
def delete_all_class_authorizations(self, userid: str) -> Union[dict, False]:
```

#### 📄 Description

Delete all of a user's **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The userid of the user who's class authorizations will be deleted.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result Steps dictionary**, a **Concatenated Security Request XML string** if the `UserAdmin.generate_requests_only` class attribute is `True`, or `False` if the user has no **Class Authorizations** to delete.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.delete_all_class_authorizations("squidwrd")
>>> {'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD   NOCLAUTH      (facility terminal xfacilit)'}]}, 'returnCode': 0, 'reasonCode': 0}}}
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
            "image": "ALTUSER SQUIDWRD   NOCLAUTH      (facility terminal xfacilit)"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```