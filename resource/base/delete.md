---
layout: default
grand_parent: General Resource Admin
parent: Base Functions
---

# Delete

Delete a general resource profile.
{: .fs-6 .fw-300 }

## `ResourceAdmin.delete()`

```python
def delete(self, resource: str, class_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Delete an existing **general resource profile**.

#### 📥 Parameters
* `resource`<br>
  The name of the **general resource profile** being deleted.

* `class_name`<br>
  The name of the **class** the general resource profile being deleted belongs to.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.delete("TESTING","ELIJTEST")
{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"del","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RDELETE ELIJTEST             (TESTING) ","messages":["ICH12002I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED."]}]},"returnCode":0,"reasonCode":0}}
```

###### Security Result Dictionary as JSON
```json

{
  "securityResult": {
    "resource": {
      "name": "TESTING",
      "class": "ELIJTEST",
      "operation": "del",
      "requestId": "ResourceRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "RDELETE ELIJTEST             (TESTING) ",
          "messages": [
            "ICH12002I RACLISTED PROFILES FOR ELIJTEST WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0,
    "runningUserid": "testuser"
  }
}
```