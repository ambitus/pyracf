---
layout: default
grand_parent: Group Admin
parent: Abstractions
---

# Group Auditor Authority

Group Administration functions for checking a user's Group Auditor Authority. 
{: .fs-6 .fw-300 }

## `GroupAdmin.has_group_auditor_authority()`

```python
def has_group_auditor_authority(self, group: str, userid: str) -> Union[bool, bytes]:
```

#### 📄 Description

Check if a user has **Auditor** authority within a group.

#### 📥 Parameters
* `group`<br>
  The **group** where the user's authority is being checked.

* `userid`<br>
  The **z/OS userid** of the user whose authority is being checked.

#### 📤 Returns
* `Union[bool, bytes]`<br>
  Returns `True` when the user has **Auditor** authority within the specified group and `False` otherwise. If the `GroupAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import GroupAdmin
>>> group_admin = GroupAdmin()
>>> group_admin.has_group_auditor_authority("testgrp0", "squidwrd")
False
```