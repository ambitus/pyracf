---
layout: default
grand_parent: User Admin
parent: Base Functions
---

# Delete

Delete a z/OS userid.
{: .fs-6 .fw-300 }

## `UserAdmin.delete()`

```python
def delete(self, userid: str) -> Union[dict, bytes]:
```

#### 📄 Description

Delete a **z/OS userid**.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** to delete.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

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
>>> user_admin.delete("squdwrd")
{'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'del', 'requestId': 'UserRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'DELUSER SQUIDWRD'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "user": {
      "name": "SQUIDWRD",
      "operation": "del",
      "requestId": "UserRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "DELUSER SQUIDWRD"
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0,
    "runningUserid": "testuser"
  }
}
```