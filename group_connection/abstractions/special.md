---
layout: default
grand_parent: Group Connection Admin
parent: Abstractions
---

# Group Special Authority

Group Connection Administration functions for modifying a user's Group Special Authority. 
{: .fs-6 .fw-300 }

## `GroupAdmin.give_group_special_authority()`

```python
def give_group_special_authority(self, userid: str, group: str) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .note }
> _Having **RACF Special** authority is analogous to having **Root** authority on Linux._

&nbsp;

Give a user **RACF Special** authority within a group.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to give **RACF Special** authority to within a group.
* `group`<br>
  The group to give the user **RACF Special** authority in.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **concatenated Security Request XML bytes** if the `ConnectionAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ConnectionAdmin
>>> connection_admin = ConnectionAdmin()
>>> connection_admin.give_group_special_authority("squidwrd", "testgrp0")
{'step1': {'securityResult': {'groupConnection': {'name': 'SQUIDWRD', 'group': 'TESTGRP0', 'operation': 'set', 'requestId': 'ConnectionRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'CONNECT SQUIDWRD  GROUP       (TESTGRP0) SPECIAL     '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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
            "image": "CONNECT SQUIDWRD  GROUP       (TESTGRP0) SPECIAL     "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```

## `GroupAdmin.take_away_group_special_authority()`

```python
def take_away_group_special_authority(self, userid: str, group: str) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .note }
> _Having **RACF Special** authority is analogous to having **Root** authority on Linux._

&nbsp;

Take away a user's **RACF Special** authority within a group.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** of the user to take **RACF Special** authority away from within a group.
* `group`<br>
  The group to take away the user's **RACF Special** in.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ConnectionAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> connection_admin.take_away_group_special_authority("squidwrd", "testgrp0")
{'step1': {'securityResult': {'groupConnection': {'name': 'SQUIDWRD', 'group': 'TESTGRP0', 'operation': 'set', 'requestId': 'ConnectionRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'CONNECT SQUIDWRD  GROUP       (TESTGRP0) NOSPECIAL     '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}}
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
            "image": "CONNECT SQUIDWRD  GROUP       (TESTGRP0) NOSPECIAL     "
          }
        ]
      },
      "returnCode": 0,
      "reasonCode": 0
    }
  }
}
```