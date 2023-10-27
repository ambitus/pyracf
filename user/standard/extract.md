---
layout: default
grand_parent: User Admin
parent: Standard
---

# Profile Extract

Functions for extracting a user's profile data. 
{: .fs-6 .fw-300 }

## `UserAdmin.extract()`

```python
def extract(
    self, userid: str, segments: dict = {}, profile_only: bool = False
) -> Union[dict, bytes]:
```

#### 📄 Description

Extract a **user's** profile data.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** to extract segment data from.

* `segments`<br>
  A list of segments to extract. Any segments omitted from the list will not be extracted. The base sgement is included always.

* `profile_only`<br>
  When set to `True`, only the extracted profile will be returned instead of returning the entire **Security Result dictionary**.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `SegmentError`<br>
  Raises `SegmentError` when the list of **segments** supplied contains at least one unknown segment.

#### 💻 Example

The following example **extracts** userid `squidwrd`'s **base segment** and **OMVS segment**. The base segment is extracted by default and the **OMVS segment** is extracted because the `omvs` key in the `segments` dictionary is set to `True`. All other segments that are not specified are not extracted. Also note that if any segments were specified in the `segments` dictionary with a value of `False`, those segments also would not be extracted.

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.extract("squidwrd", segments={"omvs": True})
{'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'listdata', 'requestId': 'UserRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'LISTUSER SQUIDWRD  OMVS    ', 'profiles': [{'base': {'user': 'squidwrd', 'name': 'unknown', 'owner': 'leonard', 'created': '7/11/2023', 'defaultGroup': 'sys1', 'passwordDate': None, 'passwordInterval': 186, 'passphraseDate': None, 'attributes': [], 'revokeDate': None, 'resumeDate': None, 'lastAccess': '7/11/2023 10:27 AM', 'classAuthorizations': [], 'logonAllowedDays': 'anyday', 'logonAllowedTime': 'anytime', 'groups': {'SYS1': {'auth': 'use', 'connectOwner': 'leonard', 'connectDate': '7/11/2023', 'connects': 0, 'uacc': None, 'lastConnect': 'unknown', 'connectAttributes': [], 'revokeDate': None, 'resumeDate': None}}, 'securityLevel': None, 'categoryAuthorization': None, 'securityLabel': None}, 'omvs': {'uid': None, 'home': '/u/squidwrd', 'program': '/bin/sh', 'cputimemax': None, 'assizemax': None, 'fileprocmax': None, 'procusermax': None, 'threadsmax': None, 'mmapareamax': None}}]}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "user": {
      "name": "SQUIDWRD",
      "operation": "listdata",
      "requestId": "UserRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "LISTUSER SQUIDWRD  OMVS    ",
          "profiles": [
            {
              "base": {
                "user": "squidwrd",
                "name": "unknown",
                "owner": "leonard",
                "created": "7/11/2023",
                "defaultGroup": "sys1",
                "passwordDate": null,
                "passwordInterval": 186,
                "passphraseDate": null,
                "attributes": [],
                "revokeDate": null,
                "resumeDate": null,
                "lastAccess": "7/11/2023 10:27 AM",
                "classAuthorizations": [],
                "logonAllowedDays": "anyday",
                "logonAllowedTime": "anytime",
                "groups": {
                  "SYS1": {
                    "auth": "use",
                    "connectOwner": "leonard",
                    "connectDate": "7/11/2023",
                    "connects": 0,
                    "uacc": null,
                    "lastConnect": "unknown",
                    "connectAttributes": [],
                    "revokeDate": null,
                    "resumeDate": null
                  }
                },
                "securityLevel": null,
                "categoryAuthorization": null,
                "securityLabel": null
              },
              "omvs": {
                "uid": null,
                "home": "/u/squidwrd",
                "program": "/bin/sh",
                "cputimemax": null,
                "assizemax": null,
                "fileprocmax": null,
                "procusermax": null,
                "threadsmax": null,
                "mmapareamax": null
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