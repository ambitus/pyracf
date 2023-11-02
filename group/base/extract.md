---
layout: default
grand_parent: Group Admin
parent: Base Functions
---

# Profile Extract

Extract a group's profile data. 
{: .fs-6 .fw-300 }

## `GroupAdmin.extract()`

```python
def extract(
    self, group: str, segments: List[str] = [], profile_only: bool = False
) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Profile data extracted for experimental **Segments** and **Traits** are considered **Experimental**. See [Segments](../segments_traits_operators#segments) and [Traits](../segments_traits_operators#traits) for more details._

&nbsp;

{: .warning }
> _Note that it is recommended to extract profile data using the provided **Getter** functions in most cases._
>
> &nbsp;
>
> ❌
> ```python
> profile = group_admin.extract("testgrp0", segments=["omvs"], profile_only=True)
> if profile["omvs"]["gid"] == 4545:
>     # Do something
> ```
> ✅
> ```python
> if resource_admin.get_omvs_gid("testgrp0") == 4545:
>   # Do something.
> ```

&nbsp;

Extract a **group's** profile data.

#### 📥 Parameters
* `group`<br>
  The **group** to extract segment data from.

* `segments`<br>
  A list of additional **segments** to extract. The base segment is extracted by default, but providing one or more additional segment keys for other segments in the form of a list will result in those segments being extracted as well.

* `profile_only`<br>
  When set to `True`, only the extracted profile will be returned instead of returning the entire **Security Result dictionary**.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `GroupAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `SegmentError`<br>
  Raises `SegmentError` when the list of **segments** provided contains one or more **unknown** segments.

#### 💻 Example

The following example **extracts** group `testgrp0`'s **base segment** and **OMVS segment**. The base segment is extracted by default and the **OMVS segment** is extracted because `omvs` is provided in the `segments` list. All other segments that are not specified are not extracted.

###### Python REPL
```python
>>> from pyracf import GroupAdmin
>>> group_admin = GroupAdmin()
>>> group_admin.extract("testgrp0", segments=["omvs"])
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