---
layout: default
grand_parent: Group Admin
parent: Standard
---

# Profile Extract

Functions for extracting a group's profile data. 
{: .fs-6 .fw-300 }

## `GroupAdmin.extract()`

```python
def extract(
    self, userid: str, segments: dict = {}, profile_only: bool = False
) -> Union[dict, bytes]:
```

#### 📄 Description

Extract a group's profile data.

#### 📥 Parameters
* `userid`<br>
  The **group** to extract segment data from.

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

The following example **extracts** group `testgrp0`'s **base segment** and **OMVS segment**. The base segment is extracted by default and the **OMVS segment** is extracted because the `omvs` key in the `segments` dictionary is set to `True`. All other segments that are not specified are not extracted. Also note that if any segments were specified in the `segments` dictionary with a value of `False`, those segments also would not be extracted.

###### Python REPL
```python
>>> from pyracf import GroupAdmin
>>> group_admin = GroupAdmin()
>>> group_admin.extract("testgrp0", segments={"omvs": True})
{'securityResult': {'group': {'name': 'TESTGRP0', 'operation': 'listdata', 'requestId': 'GroupRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'LISTGRP TESTGRP0  OMVS    ', 'profiles': [{'base': {'name': 'testgrp0', 'superiorGroup': 'sys1', 'owner': 'eswift', 'created': '5/30/2023', 'installationData': None, 'modelDataSet': None, 'terminalUniversalAccess': True, 'subgroups': [], 'users': [{'userid': 'eswift', 'access': 'use', 'accessCount': 0, 'universalAccess': None, 'connectAttributes': ['special'], 'revokeDate': None, 'resumeDate': None}, {'userid': 'leonard', 'access': 'use', 'accessCount': 0, 'universalAccess': None, 'connectAttributes': ['operations'], 'revokeDate': None, 'resumeDate': None}]}, 'omvs': {'gid': 4545}}]}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "group": {
      "name": "TESTGRP0",
      "operation": "listdata",
      "requestId": "GroupRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "LISTGRP TESTGRP0  OMVS    ",
          "profiles": [
            {
              "base": {
                "name": "testgrp0",
                "superiorGroup": "sys1",
                "owner": "eswift",
                "created": "5/30/2023",
                "installationData": null,
                "modelDataSet": null,
                "terminalUniversalAccess": true,
                "subgroups": [],
                "users": [
                  {
                    "userid": "eswift",
                    "access": "use",
                    "accessCount": 0,
                    "universalAccess": null,
                    "connectAttributes": [
                      "special"
                    ],
                    "revokeDate": null,
                    "resumeDate": null
                  },
                  {
                    "userid": "leonard",
                    "access": "use",
                    "accessCount": 0,
                    "universalAccess": null,
                    "connectAttributes": [
                      "operations"
                    ],
                    "revokeDate": null,
                    "resumeDate": null
                  }
                ]
              },
              "omvs": {
                "gid": 4545
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