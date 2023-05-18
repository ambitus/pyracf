---
layout: default
parent: User Admin
---

# Standard User Administration

User administration functions that should be used for most common use cases.

## `UserAdmin.is_special()`

```python
def is_special(self, userid: str) -> bool:
```

#### 📄 Description

&nbsp;

{: .note }
> _Having **RACF Special** authority is analogous to having **Root** authority on Linux._

&nbsp;

Check if a user has **RACF Special** authority.

#### 📥 Parameters
* `userid`<br>
  The ID of the user who authority we are checking.

#### 📤 Returns
* `bool`<br>
  Returns `True` when the user has **RACF Special** authority and `False` otherwise.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.is_special("squidwrd")
False
```

## `UserAdmin.set_special()`

```python
def set_special(self, userid: str, generate_request_only=False) -> dict:
```

#### 📄 Description

&nbsp;

{: .note }
> _Having **RACF Special** authority is analogous to having **Root** authority on Linux._

&nbsp;

Give a user **RACF Special** authority.

#### 📥 Parameters
* `userid`<br>
  The ID of the user to give **RACF Special** authority.

* `generate_request_only`<br>
  **Optional** toggle that can be used to tell pyRACF to **ONLY** generate and return the **Security Request** without making any calls to the **IRRSMO00 API**.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result dictionary** or a **Security Request XML string** if the `generate_request_only` toggle is used.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_special("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  SPECIAL     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `UserAdmin.del_special()`

```python
def del_special(self, userid: str, generate_request_only=False) -> dict:
```

#### 📄 Description

&nbsp;

{: .note }
> _Having **RACF Special** authority is analogous to having **Root** authority on Linux._

&nbsp;

Remove a user's **RACF Special** authority.

#### 📥 Parameters
* `userid`<br>
  The ID of the user to take RACF **Special** authority away from.

* `generate_request_only`<br>
  **Optional** toggle that can be used to tell pyRACF to **ONLY** generate and return the **Security Request** without making any calls to the **IRRSMO00 API**.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result dictionary** or a **Security Request XML string** if the `generate_request_only` toggle is used.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.del_special("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  NOSPECIAL     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `UserAdmin.is_auditor()`

```python
def is_auditor(self, userid: str) -> bool:
```

#### 📄 Description

Check if a user has **Auditor** authority.

#### 📥 Parameters
* `userid`<br>
  The ID of the user who's authority we are checking.

#### 📤 Returns
* `bool`<br>
  Returns `True` when the user has **Auditor** authority and `False` otherwise.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.is_auditor("squidwrd")
False
```

## `UserAdmin.set_auditor()`

```python
def set_auditor(self, userid: str) -> dict:
```

#### 📄 Description

Give a user **Auditor** authority.

#### 📥 Parameters
* `userid`<br>
  The ID of the user to give **Auditor** authority.

#### 📤 Returns
* `dict`<br>
  Returns a **Security Result dictionary**.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_auditor("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  AUDITOR     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `UserAdmin.del_auditor()`

```python
def del_auditor(self, userid: str) -> dict:
```

#### 📄 Description

Remove a user's **Auditor** authority.

#### 📥 Parameters
* `userid`<br>
  The ID of the user to take **Auditor** authority away from.

#### 📤 Returns
* `dict`<br>
  Returns a **Security Result dictionary**.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.del_auditor("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  NOAUDITOR     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `UserAdmin.is_operations()`

```python
def is_operations(self, userid: str) -> bool:
```

#### 📄 Description

Check if a user has **Operator** authority.

#### 📥 Parameters
* `userid`<br>
  The ID of the user who's authority we are checking.

#### 📤 Returns
* `bool`<br>
  Returns `True` when the user has **Operator** authority and `False` otherwise.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.is_operations("squidwrd")
False
```

## `UserAdmin.set_operations()`

```python
def set_operations(self, userid: str) -> dict:
```

#### 📄 Description

Give a user **Operator** authority.

#### 📥 Parameters
* `userid`<br>
  The ID of the user to give **Operator** authority.

#### 📤 Returns
* `dict`<br>
  Returns a **Security Result dictionary**.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_operations("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  OPERATIONS     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `UserAdmin.del_operations()`

```python
def del_operations(self, userid: str) -> dict:
```

#### 📄 Description

Remove a user's **Operator** authority.

#### 📥 Parameters
* `userid`<br>
  The ID of the user to take **Operator** authority away from.

#### 📤 Returns
* `dict`<br>
  Returns a **Security Result dictionary**.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.del_operations("squidwrd")
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  NOOPERATIONS     '}]}, 'returncode': 0, 'reasoncode': 0}}
```

## `UserAdmin.get_uid()`

```python
def get_uid(self, userid: str) -> Union[int,None]:
```

#### 📄 Description

Get a user's **z/OS Unix System Services UID**.

#### 📥 Parameters
* `userid`<br>
  The ID of the user who's **z/OS Unix System Services UID** is being requested.

#### 📤 Returns
* `Union[int,None]`<br>
  Returns the user's **z/OS Unix System Services UID** or `None` if the user does not have an **OMVS segment**.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_uid("squidwrd")
2424
```

## `set_uid`

```python
def set_uid(self, userid: str, uid: int, generate_request_only=False) -> dict:
```

#### 📄 Description

Change a user's **z/OS Unix System Services UID**.

#### 📥 Parameters
* `userid`<br>
  The ID of the user who's **z/OS Unix System Services UID** is being changed.

* `generate_request_only`<br>
  **Optional** toggle that can be used to tell pyRACF to **ONLY** generate and return the **Security Request** without making any calls to the **IRRSMO00 API**.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result dictionary** or a **Security Request XML string** if the `generate_request_only` toggle is used.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
>>> from pyracf.user.user_admin import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.set_uid("squidwrd", 1919)
{'securityresult': {'user': {'name': 'SQUIDWRD', 'operation': 'set', 'requestid': 'UserRequest', 'commands': [{'safreturncode': 8, 'returncode': 16, 'reasoncode': 8, 'image': 'ADDUSER SQUIDWRD ', 'messages': ['IKJ56702I INVALID USERID, SQUIDWRD']}, {'safreturncode': 0, 'returncode': 0, 'reasoncode': 0, 'image': 'ALTUSER SQUIDWRD  OMVS     (UID         (1919))'}]}, 'returncode': 4, 'reasoncode': 4}}
```