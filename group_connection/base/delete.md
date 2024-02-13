---
layout: default
grand_parent: Group Connection Admin
parent: Base Functions
---

# Delete

Delete a user's connection to a group
{: .fs-6 .fw-300 }

## `ConnectionAdmin.delete()`

```python
def delete(self, userid: str, group: str) -> Union[dict, bytes]:
```

#### 📄 Description

Delete a user's **connection** to a group.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user whose **connection** to a group is being deleted.
* `group`<br>
  The group to delete the users **connection** from.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ConnectionAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ConnectionAdmin
>>> connection_admin = ConnectionAdmin()
>>> connection_admin.delete("squidwrd", "testgrp0")
{'securityResult': {'groupConnection': {'name': 'SQUIDWRD', 'group': 'TESTGRP0', 'operation': 'del', 'requestId': 'ConnectionRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'REMOVE  SQUIDWRD  GROUP       (TESTGRP0)'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "groupConnection": {
      "name": "SQUIDWRD",
      "group": "TESTGRP0",
      "operation": "del",
      "requestId": "ConnectionRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "REMOVE  SQUIDWRD  GROUP       (TESTGRP0)"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0,
    "runningUserid": "testuser"
  }
}
```