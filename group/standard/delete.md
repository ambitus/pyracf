---
layout: default
grand_parent: Group Admin
parent: Standard
---

# Delete

Delete a group.
{: .fs-6 .fw-300 }

## `GroupAdmin.delete()`

```python
def delete(self, group: str) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .warning }
> _Note that in order to delete a group, you must remove all **subgroups**, **user connections**, and **group data sets** from it. Failure to do so will result in a `SecurityRequestError` that contains a **Security Result dictionary** that will contain the message `IKJ56702I INVALID GROUP, <group>` in the `messages` list._

&nbsp;


Delete a **group**.

#### 📥 Parameters
* `group`<br>
  The **group** to delete.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `GroupAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import GroupAdmin
>>> group_admin = GroupAdmin()
>>> group_admin.delete("testgrp0")
{'securityResult': {'group': {'name': 'TESTGRP0', 'operation': 'del', 'requestId': 'GroupRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'DELGROUP TESTGRP0'}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "group": {
      "name": "TESTGRP0",
      "operation": "del",
      "requestId": "GroupRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "DELGROUP TESTGRP0"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```