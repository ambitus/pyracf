---
layout: default
grand_parent: Access Admin
parent: Standard
---

# Delete

Delete a user's access to a group
{: .fs-6 .fw-300 }

## `AccessAdmin.delete()`

```python
def delete(self, userid: str, group: str) -> Union[dict, bytes]:
```

#### 📄 Description

Delete a specified **permission**

#### 📥 Parameters
* `resource`<br>
  The **resource profile** to grant this permission to.
* `class`<br>
  The **class** that the specified resource profile belongs to.
* `auth_id`<br>
  The **z/OS userid or group name** of the user or group to receive the permission.


* `traits`<br>
  A dictionary of **traits/attributes** that should be assigned to this permission for the specified user to the specified resource. See [Traits](../segments_traits_operators#traits) to see what all of the valid **Access Traits** are.

* `volume`<br>
  The **volume** that the specified dataset resides on (ignored unless the **class** is `DATASET`).
* `generic`<br>
  Specifies whether the resource is **generic** or not (ignored unless the **class** is `DATASET`).

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `AccessAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import AccessAdmin
>>> access_admin = AccessAdmin()
>>> access_admin.delete("TESTING", "ELIJTEST", "ESWIFT")
{'securityResult': {'permission': {'name': 'TESTING', 'class': 'ELIJTEST', 'operation': 'del', 'requestId': 'AccessRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'PERMIT               TESTING CLASS(ELIJTEST)  DELETE       ID          (ESWIFT)', 'messages': ['ICH06011I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED']}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "permission": {
      "name": "TESTING",
      "class": "ELIJTEST",
      "operation": "del",
      "requestId": "AccessRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "PERMIT               TESTING CLASS(ELIJTEST)  DELETE       ID          (ESWIFT)",
          "messages": [
            "ICH06011I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED"
          ]
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```