---
layout: default
grand_parent: General Resource Admin
parent: Standard
---

# Your Access

Resource administration functions for checking the user's access to a General Resource Profile. 
{: .fs-6 .fw-300 }

## `ResourceAdmin.get_your_access()`

```python
def get_your_access(self, resource: str, class_name: str) -> Union[str, bytes, None]:
```

#### 📄 Description

Check **Your Access** for a general resource profile.

#### 📥 Parameters
* `resource`<br>
  The **Resource** profile for which RACF should check the current user's access level.

* `class_name`<br>
  The name of the **class** the resource profile being checked belongs to.

#### 📤 Returns
* `Union[str,bytes,None]`<br>
  Returns `None` when the resource profile has no **Your Access** defined, otherwise returns the access level as a string. If the `ResourceAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.get_your_access("TESTING","ELIJTEST")
"read"
```