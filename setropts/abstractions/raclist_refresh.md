---
layout: default
grand_parent: Setropts Admin
parent: Abstractions
---

# Raclist Refresh

Refresh a RACLISTed class.
{: .fs-6 .fw-300 }

## `SetroptsAdmin.refresh_raclist()`

```python
def refresh_raclist(self, class_names: Union[str, List[str]]) -> Union[dict, bytes]:
```

#### 📄 Description

Refresh a RACLISTed **class**.

#### 📥 Parameters
* `class_name`<br>
  The RACLISTed **class** to refresh.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `SetroptsAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.refresh_raclist("ELIJTEST")
{'step1': {'securityResult': {'systemSettings': {'operation': 'set', 'requestId': 'SetroptsRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'SETROPTS      RACLIST     (ELIJTEST) REFRESH     ', 'messages': ['ICH14063I SETROPTS command complete.']}]}, 'returnCode': 0, 'reasonCode': 0}}}
```

###### Security Result Dictionary as JSON
```json
{
  "step1":{
    "securityResult":{
      "systemSettings":{
        "operation":"set",
        "requestId":"SetroptsRequest",
        "commands":[
          {
            "safReturnCode":0,
            "returnCode":0,
            "reasonCode":0,
            "image":"SETROPTS      RACLIST     (ELIJTEST) REFRESH     ",
            "messages":[
              "ICH14063I SETROPTS command complete."
            ]
          }
        ]
      },
      "returnCode":0,
      "reasonCode":0
    }
  }
}
```