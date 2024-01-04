---
layout: default
grand_parent: Group Connection Admin
parent: Abstractions
---

# Group Auditor Authority

Group Connection Administration functions for modifying a user's Group Auditor Authority. 
{: .fs-6 .fw-300 }

## `GroupAdmin.give_group_auditor_authority()`

```python
def give_group_auditor_authority(self, userid: str, group: str) -> Union[dict, bytes]:
```

#### 📄 Description

Give a user **Auditor** authority within a group.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to give **Auditor** authority to within a group.
* `group`<br>
  The group to give the user **Auditor** authority in.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **concatenated Security Request XML bytes** if the `ConnectionAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ConnectionAdmin
>>> connection_admin = ConnectionAdmin()
>>> connection_admin.give_group_auditor_authority("squidwrd", "testgrp0")
{'step1': {'securityResult': {'groupConnection': {'name': 'SQUIDWRD', 'group': 'TESTGRP0', 'operation': 'set', 'requestId': 'ConnectionRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'CONNECT SQUIDWRD  GROUP       (TESTGRP0) AUDITOR     '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "groupConnection": {
        "name": "SQUIDWRD",
        "group": "TESTGRP0",
        "operation": "set",
        "requestId": "ConnectionRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "CONNECT SQUIDWRD  GROUP       (TESTGRP0) AUDITOR     "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `GroupAdmin.take_away_group_auditor_authority()`

```python
def take_away_group_auditor_authority(self, userid: str, group: str) -> Union[dict, bytes]:
```

#### 📄 Description

Take away a user's **Auditor** authority within a group.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to take **Auditor** authority away from within a group.
* `group`<br>
  The group to take away the user's **Auditor** in.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ConnectionAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> connection_admin.take_away_group_auditor_authority("squidwrd", "testgrp0")
{'step1': {'securityResult': {'groupConnection': {'name': 'SQUIDWRD', 'group': 'TESTGRP0', 'operation': 'set', 'requestId': 'ConnectionRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'CONNECT SQUIDWRD  GROUP       (TESTGRP0) NOAUDITOR     '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1": {
    "securityResult": {
      "groupConnection": {
        "name": "SQUIDWRD",
        "group": "TESTGRP0",
        "operation": "set",
        "requestId": "ConnectionRequest",
        "commands": [
          {
            "safReturnCode": 0,
            "returnCode": 0,
            "reasonCode": 0,
            "image": "CONNECT SQUIDWRD  GROUP       (TESTGRP0) NOAUDITOR     "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```