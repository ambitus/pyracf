---
layout: default
grand_parent: General Resource Admin
parent: Standard
---

# Profile Extract

Functions for extracting a general resource profile's data. 
{: .fs-6 .fw-300 }

## `ResourceAdmin.extract()`

```python
def extract(
    self, data_set: str, resource: str, class_name:str, segments: dict = {}, profile_only: bool = False
) -> Union[dict, bytes]:
```

#### 📄 Description

Extract a **general resource** profile's data.

#### 📥 Parameters
* `resource`<br>
  The name of the **resource** profile being extracted.

* `class_name`<br>
  The name of the **class** the resource profile being extracted belongs to.

* `segments`<br>
  A dictionary of segments to extract. Each segment must be a boolean value where `True` indicates that the segment should be extracted and `False` indicates that the segment should not be extracted. Any segments omitted from the dictionary will not be extracted. The base sgement is included always.

* `profile_only`<br>
  When set to `True`, only the extracted profile will be returned instead of returning the entire **Security Result dictionary**.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `UserAdmin.generate_request_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **extracts** the **base segment** of the general resource profile `TESTING` in the `ELIJTEST` class. The base segment is extracted by default no other segments are specified or extracted. Also note that if any segments were specified in the `segments` dictionary with a value of `False`, those segments also would not be extracted.

###### Python REPL
```python
>>> from pyracf import ResourceAdmin
>>> resource_admin = ResourceAdmin()
>>> resource_admin.extract("TESTING","ELIJTEST")
{"securityResult":{"resource":{"name":"TESTING","class":"ELIJTEST","operation":"listdata","requestId":"ResourceRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"RLIST   ELIJTEST             (TESTING) ","profiles":[{"base":{"class":"elijtest","name":"testing","level":0,"owner":"eswift","universalAccess":"read","yourAccess":"read","warning":null,"installationData":null,"applicationData":null,"auditing":{"failures":"read"},"notify":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "resource": {
      "name": "TESTING",
      "class": "ELIJTEST",
      "operation": "listdata",
      "requestId": "ResourceRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "RLIST   ELIJTEST             (TESTING) ",
          "profiles": [
            {
              "base": {
                "class": "elijtest",
                "name": "testing",
                "level": 0,
                "owner": "eswift",
                "universalAccess": "read",
                "yourAccess": "read",
                "warning": null,
                "installationData": null,
                "applicationData": null,
                "auditing": {
                  "failures": "read"
                },
                "notify": null,
                "generic": false
              }
            }
          ]
        }
      ]
    },
    "returnCode": 0,
    "reasonCode": 0
  }
}
```

