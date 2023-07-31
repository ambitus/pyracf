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
    def delete(
        self,
        resource: str,
        class_name: str,
        auth_id: str,
        volume: Union[str, None] = None,
        generic: bool = False,
    ) -> Union[dict, bytes]:
```

#### 📄 Description

Delete a specified **permission**

#### 📥 Parameters
* `resource`<br>
  The **resource profile** to delete this permission from.
* `class_name`<br>
  The **class** that the specified resource profile belongs to.
* `auth_id`<br>
  The **z/OS userid or group name** of the user or group to receive the permission.
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