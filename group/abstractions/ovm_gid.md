---
layout: default
grand_parent: Group Admin
parent: Abstractions
---

# z/VM Open Extensions GID

Group Administration functions for accessing and modifying a group's z/VM Open Extensions GID. 
{: .fs-6 .fw-300 }

## `GroupAdmin.get_ovm_gid()`

```python
def get_ovm_gid(self, group: str) -> Union[int, None, bytes]:
```

#### 📄 Description

Get a group's **z/VM Open Extensions GID**.

#### 📥 Parameters
* `group`<br>
  The group who's **z/VM Open Extensions GID** is being requested.

#### 📤 Returns
* `Union[int, None, bytes]`<br>
  Returns the group's **z/VM Open Extensions GID** or `None` if the group does not have an **OVM segment**. If the `GroupAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

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
>>> group_admin.get_ovm_gid("testgrp0")
512
```

## `GroupAdmin.set_ovm_gid()`

```python
def set_ovm_uid(self, group: str, gid: int) -> Union[dict, bytes]:
```

#### 📄 Description

Change a group's **z/VM Open Extensions GID**.

#### 📥 Parameters
* `group`<br>
  The group who's **z/VM Open Extensions GID** is being changed.

* `gid`<br>
  The **z/VM Open Extensions GID** to set for the specified group.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `GroupAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **group** cannot be altered because it does **NOT** exist.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import GroupAdmin
>>> group_admin = GroupAdmin()
>>> group_admin.set_ovm_gid("testgrp0", 256)
{'step1': {'securityResult': {'group': {'name': 'TESTGRP0', 'operation': 'set', 'requestId': 'GroupRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'ALTGROUP TESTGRP0  OVM      (GID         (256))'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "group": {
        "name": "TESTGRP0",
        "operation": "set",
        "requestId": "GroupRequest",
        "info": [
          "Definition exists. Add command skipped due  to precheck option"
        ],
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "ALTGROUP TESTGRP0  OVM      (GID         (256))"
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```