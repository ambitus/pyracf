---
layout: default
grand_parent: User Admin
parent: Base Functions
---

# Profile Extract

Extract a user's profile data. 
{: .fs-6 .fw-300 }

## `UserAdmin.extract()`

```python
def extract(
    self, userid: str, segments: List[str] = [], profile_only: bool = False
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
> profile = user_admin.extract(squidwrd, segments=["omvs"], profile_only=True)
> if profile["omvs"]["defaultShell"] == "/bin/sh":
>     # Do something
> ```
> ✅
> ```python
> if user_admin.get_omvs_default_shell("squidwrd") == "/bin/sh"
>   # Do something.
> ```

&nbsp;

Extract a **user's** profile data.

#### 📥 Parameters
* `userid`<br>
  The **z/OS userid** to extract segment data from.

* `segments`<br>
  A list of additional **segments** to extract. The base segment is extracted by default, but providing one or more additional segment keys for other segments in the form of a list will result in those segments being extracted as well.

* `profile_only`<br>
  When set to `True`, only the extracted profile will be returned instead of returning the entire **Security Result dictionary**.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `UserAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `SegmentError`<br>
  Raises `SegmentError` when the list of **segments** provided contains one or more **unknown** segments.

#### 💻 Example

The following example **extracts** userid `squidwrd`'s **base segment** and **OMVS segment**. The base segment is extracted by default and the **OMVS segment** is extracted because `omvs` is provided in the `segments` list. All other segments that are not specified are not extracted.

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.extract("squidwrd", segments=["omvs"])
{'securityResult': {'user': {'name': 'SQUIDWRD', 'operation': 'listdata', 'requestId': 'UserRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'LISTUSER SQUIDWRD  OMVS    ', 'profiles': [{'base': {'user': 'squidwrd', 'name': None, 'owner': 'leonard', 'created': '7/11/2023', 'defaultGroup': 'sys1', 'passwordDate': None, 'passwordInterval': 186, 'passphraseDate': None, 'attributes': [], 'revokeDate': None, 'resumeDate': None, 'lastAccess': '7/11/2023 10:27 AM', 'classAuthorizations': [], 'logonAllowedDays': 'anyday', 'logonAllowedTime': 'anytime', 'groups': {'SYS1': {'auth': 'use', 'connectOwner': 'leonard', 'connectDate': '7/11/2023', 'connects': 0, 'uacc': None, 'lastConnect': None, 'connectAttributes': [], 'revokeDate': None, 'resumeDate': None}}, 'securityLevel': None, 'categoryAuthorization': None, 'securityLabel': None}, 'omvs': {'uid': None, 'homeDirectory': '/u/squidwrd', 'defaultShell': '/bin/sh', 'maxCpuTime': None, 'maxAddressSpaceSize': None, 'maxFilesPerProcess': None, 'maxProcesses': None, 'maxThreads': None, 'maxFileMappingPages': None}}]}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
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
                "name": null,
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
                    "lastConnect": null,
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
                "homeDirectory": "/u/squidwrd",
                "defaultShell": "/bin/sh",
                "maxCpuTime": null,
                "maxAddressSpaceSize": null,
                "maxFilesPerProcess": null,
                "maxProcesses": null,
                "maxThreads": null,
                "maxFileMappingPages": null
              }
            }
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