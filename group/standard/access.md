---
layout: default
grand_parent: Group Admin
parent: Standard
---

# Group Access Attribute

Group administration functions for checking a user's Group Access Attribute. 
{: .fs-6 .fw-300 }

## `GroupAdmin.has_group_access_attribute()`

```python
def has_group_access_attribute(self, group: str, userid: str) -> Union[bool, bytes]:
```

#### 📄 Description

Check if a user has the **Access Attribute** within a group.

#### 📥 Parameters
* `group`<br>
  The group where the user's **Access Attribute** is being checked.

* `userid`<br>
  The **z/OS userid** of the user who's **Access Attribute** is being checked.

#### 📤 Returns
* `Union[bool,bytes]`<br>
  Returns `True` when the user has the **Access Attribute** within the specified group and `False` otherwise. If the `GroupAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import GroupAdmin
>>> group_admin = GroupAdmin()
>>> group_admin.has_group_access_attribute("testgrp0", "squidwrd")
False
```