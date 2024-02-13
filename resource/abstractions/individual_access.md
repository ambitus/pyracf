---
layout: default
grand_parent: General Resource Admin
parent: Abstractions
---

# Individual Access

General Resource Profile Administration functions for checking an Individual User's access to a General Resource Profile. 
{: .fs-6 .fw-300 }

## `ResourceAdmin.get_my_access()`

```python
def get_my_access(self, resource: str, class_name: str) -> Union[str, bytes, None]:
```

#### 📄 Description

Get the **Running User's** access to a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** to get the current user's access level for.

* `class_name`<br>
  The name of the **class** the specified general resource profile belongs to.

#### 📤 Returns
* `Union[str, bytes, None]`<br>
  Returns `None` when the general resource profile has no **Your Access** section defined for the running userid, otherwise the **Access Level** is returned as a string. If the `ResourceAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_my_access("TESTING","ELIJTEST")
"read"
```

## `ResourceAdmin.get_user_access()`

```python
def get_user_access(self, resource: str, class_name: str, userid: str) -> Union[str, bytes, None]:
```

#### 📄 Description

&nbsp;

{:.warning}
> _In order to use `get_user_access`, the caller must have at least `UPDATE` access to the `userid.IRRSMO00` resource in the `SURROGAT` class, where `userid` represents the specific userid you wish to check access for. Further information can be found outlined in [Our Dependencies Note](../../../index)._

&nbsp;

Get a **Specified User's** access to a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **general resource profile** to get the specified user's access level for.

* `class_name`<br>
  The name of the **class** the specified general resource profile belongs to.

* `userid`<br>
  The **z/OS Userid** whose access is being requested.

#### 📤 Returns
* `Union[str, bytes, None]`<br>
  Returns `None` when the general resource profile has no **Your Access** section defined for the specified userid, otherwise the **Access Level** is returned as a string. If the `ResourceAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `UserIdError`<br>
  Raises `UserIdError` when the **z/OS userid** provided is not a string value between 1 to 8 characters in length.
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_user_access("TESTING","ELIJTEST","SQUIDWRD")
"update"
```