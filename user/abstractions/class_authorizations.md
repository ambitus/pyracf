---
layout: default
grand_parent: User Admin
parent: Abstractions
---

# Class Authorizations

User Administration functions for accessing and modifying a user's Class Authorizations. 
{: .fs-6 .fw-300 }

## `UserAdmin.get_class_authorizations()`

```python
def get_class_authorizations(self, userid: str) -> Union[List[str], bytes]:
```

#### 📄 Description

Get a user's **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user whose **Class Authorizations** is being requested.

#### 📤 Returns
* `Union[List[str], bytes]`<br>
  Returns the user's **Class Authorizations**. If the `UserAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

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
>>> user_admin.get_class_authorizations("squidwrd")
['facility', 'terminal', 'xfacilit']
```

## `UserAdmin.set_class_authorizations()`

```python
def set_class_authorizations(
    self, userid: str, class_authorizations: List[str]
) -> Union[dict, bytes]:
```

#### 📄 Description

Overwrite a user's existing **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user whose **Class Authorizations** are being overwritten.

* `class_authorizations`<br>
  A list of one or more **Class Authorizations** that will become the user's new **Class Authorizations**.

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
>>> user_admin.set_class_authorizations("squidwrd", ["facility", "terminal", "xfacilit"])
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD   NOCLAUTH      (terminal xfacilit)'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}, 'step2': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD     CLAUTH      (facility terminal xfacilit)'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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
) -> Union[dict, bytes]:
```

#### 📄 Description

Add new **Class Authorizations** to a user's existing **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to add **Class Authorizations** to.

* `class_authorizations`<br>
  <br>

  {: .note }
  > _May be a **string value** or a **list of string values**._

  <br>
  One or more **Class Authorazitons** to add. 

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
>>> user_admin.add_class_authorizations("squidwrd", ["terminal", "xfacilit"])
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD     CLAUTH      (terminal xfacilit)'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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
) -> Union[dict, bytes]:
```

#### 📄 Description

Remove **Class Authorizations** to a user's existing **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to remove **Class Authorizations** from.

* `class_authorizations`<br>
  <br>

  {: .note }
  > _May be a **string value** or a **list of string values**._

  <br>
  One or more **Class Authorazitons** to remove.

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
>>> user_admin.remove_class_authorizations("squidwrd", ["facility", "terminal"])
{'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD   NOCLAUTH      (facility terminal)'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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

## `UserAdmin.remove_all_class_authorizations()`

```python
def remove_all_class_authorizations(self, userid: str) -> Union[dict, bool, bytes]:
```

#### 📄 Description

Delete all of a user's **Class Authorizations**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user whose class authorizations will be deleted.

#### 📤 Returns
* `Union[dict, bool, bytes]`<br>
  Returns a **Security Result Steps dictionary**, **Concatenated Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is `True`, or `False` if the user has no **Class Authorizations** to delete.

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
>>> user_admin.delete_all_class_authorizations("squidwrd")
>>> {'step1': {'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestId': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTUSER SQUIDWRD   NOCLAUTH      (facility terminal xfacilit)'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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