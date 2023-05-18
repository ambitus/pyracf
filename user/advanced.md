---
layout: default
parent: User Admin
---

# Advanced User Administration

User administration functions that should be used by power users to perform more complex tasks.

## Traits

&nbsp;

{: .note }
> _The `userid` trait is **always required**._

&nbsp;

{: .note }
> _All traits can be set to `False` in **[`UserAdmin.alter()`](#useradminalter)** to indicate that they should be removed._

&nbsp;

When using the **[`UserAdmin.add()`](#useradminadd)** and **[`UserAdmin.alter()`](#useradminalter)** functions, the following are valid user traits.

&nbsp;

| **Trait** | **Description** | **Valid Types** | **Segment** |
| `auditor` | Set to `True` to give the user **Auditor** authority or `False` otherwise. | Add: `bool`<br>Alter: `bool` | `base` |
| `home` | Set the user's **z/OS Unix System Services home directory**. | Add: `str`<br>Alter: `str`, `False` | `omvs` |
| `name` | Set the name of the person that the userid belongs to. | Add: `str`<br>Alter: `str`, `False` | `base` |
| `operations` | Set to `True` to give the user **Operator** authority or `False` otherwise. | Add: `bool`<br>Alter: `bool` | `base` |
| `owner` | Set the userid that owns the userid being altered/created. | Add: `str`<br>Alter: `str`,`False` | `base` |
| `password` | Set the user's password. | Add: `str`<br>Alter: `str`, `False` | `base` |
| `program` | `Union[str,bool]`: Set the user's **default shell**. | Add: `str`<br>Alter: `str`, `False` | `omvs` |
| `special` | Set to `True` to give the user **RACF Special** authority or `False` otherwise. | Add: `bool`<br>Alter: `bool` | `base` |
| `uid` | The user's **z/OS userid**. | Add: `str`<br>Alter: `str`, `False` | `base` |
| `userid` | Set the user's **z/OS Unix System Services UID**. | Add: `int`, `str`<br>Alter: `int`, `str`, `False` | `omvs` |

## Segments

When using the **[`UserAdmin.extract()`](#useradminextract)** function, the following are valid segments.

&nbsp;

| **Segment** | **Description** |
| `base` | The base segment that all userids have |
| `cics` | |
| `csdata` | |
| `dce` | |
| `dfp` | |
| `eim` | |
| `kerb` | |
| `language` | |
| `lnotes` | |
| `mfa` | |
| `nds` | |
| `netview` | |
| `omvs` | |
| `operparm` | |
| `ovm` | |
| `proxy` | |
| `tso` | |
| `workattr` | |

## `UserAdmin.add()`

```python
def add(self, traits: dict, generate_request_only=False) -> Union[dict,str]:
```

#### 📄 Description

Create a new **z/OS userid**.

#### 📥 Parameters
* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the user on creation. See **[Traits](#traits)** to see what all of the valid **User Traits** are.

* `generate_request_only`<br>
  **Optional** toggle that can be used to tell pyRACF to **ONLY** generate and return the **Security Request** without making any calls to the **IRRSMO00 API**.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result dictionary** or a **Security Request XML string** if the `generate_request_only` toggle is used.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

The following example **creates** a **new user** called `squidwrd` using the `userid` field in the `traits` dictionary and the rest of the traits specified are given to the userid on creation.

&nbsp;

```python
from pyracf import UserAdmin
user_admin = UserAdmin()

traits = {
    "name": "Squidward",
    "userid": "squidwrd",
    "password": "******",
    "owner": "leonard",
    "special": True,
    "operator": False,
    "uid": 2424,
    "home": "/u/squidwrd",
    "program": "/bin/sh",
}

user_admin.add(traits)
```

## `UserAdmin.alter()`

```python
def alter(self, traits: dict, generate_request_only=False) -> Union[dict,str]:
```

#### 📄 Description

Create a new **z/OS userid**.

#### 📥 Parameters
* `traits`<br>
  A dictionary of **traits/attributes** that should be altered. See **[Traits](#traits)** to see what all of the valid **User Traits** are.

* `generate_request_only`<br>
  **Optional** toggle that can be used to tell pyRACF to **ONLY** generate and return the **Security Request** without making any calls to the **IRRSMO00 API**.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result dictionary** or a **Security Request XML string** if the `generate_request_only` toggle is used.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

The following example **alters** userid `squidwrd` using the `userid` field in the `traits` dictionary and the rest of the traits specified are attributes that are altered.

&nbsp;

```python
from pyracf import UserAdmin
user_admin = UserAdmin()

traits = {
    "userid": "squidwrd",
    "special": False,
    "operator": True,
    "home": "/u/clarinet",
    "program": False,
}

user_admin.alter(traits)
```

## `UserAdmin.delete()`

```python
def delete(self, userid: str, generate_request_only=False) -> Union[dict,str]:
```

#### 📄 Description

Create a new **z/OS userid**.

#### 📥 Parameters
* `userid`<br>
  The z/OS userid to delete.

* `generate_request_only`<br>
  **Optional** toggle that can be used to tell pyRACF to **ONLY** generate and return the **Security Request** without making any calls to the **IRRSMO00 API**.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result dictionary** or a **Security Request XML string** if the `generate_request_only` toggle is used.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

```python
from pyracf import UserAdmin
user_admin = UserAdmin()
user_admin.delete("squdwrd")
```

## `UserAdmin.extract()`

```python
def extract(self, traits: str, generate_request_only=False) -> Union[dict,str]:
```

#### 📄 Description

Extract user profiles.

#### 📥 Parameters
* `traits`<br>
  A dictionary of segments to extract. Each segment must be a boolean value where `True` indicates that the segment should be extracted and `False` indicates that the segment should not be extracted. Any segments omitted from the dictionary will not be extracted. The base sgement is included always. Also note that `userid` must also be included in the dictionary to indicate which userid to extract profiles from. See **[Segments](#segmets)** to see what all of the valid **User Segments** are.

* `generate_request_only`<br>
  **Optional** toggle that can be used to tell pyRACF to **ONLY** generate and return the **Security Request** without making any calls to the **IRRSMO00 API**.

#### 📤 Returns
* `Union[dict,str]`<br>
  Returns a **Security Result dictionary** or a **Security Request XML string** if the `generate_request_only` toggle is used.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when both the **return code** and **reason code** of the **Security Result** are not equal to `0`.

#### 💻 Example

The following example **extract** userid `squidwrd`'s **base segment** and **OMVS segment**. The base segment is extracted by default and the **OMVS segment** is extracted because the `omvs` trait is set to `True`. The `mfa` trait is explicitely set to `False` to indicate that it should not be extracted. All other segments that are not specified are also not extracted.

&nbsp;

```python
from pyracf import UserAdmin
user_admin = UserAdmin()
traits = {
    "userid": "squidwrd",
    "omvs": True,
    "mfa": False,
}
user_admin.extract(traits)
```

```json
{
    "securityresult": {
        "user": {
            "name": "SQUIDWRD",
            "operation": "listdata",
            "requestid": "UserRequest",
            "commands": [
                {
                    "safreturncode": 0,
                    "returncode": 0,
                    "reasoncode": 0,
                    "image": "LISTUSER SQUIDWRD  OMVS    ",
                    "message": "MMAPAREAMAX= NONE",
                    "profile": {
                        "base": {
                            "groups": {
                                "SYS1": {
                                    "auth": "USE",
                                    "connectowner": "LEONARD",
                                    "connectdate": 23.046,
                                    "connects": 0,
                                    "uacc": null,
                                    "lastconnect": "UNKNOWN",
                                    "connectattributes": null,
                                    "revokedate": null,
                                    "resumedate": null
                                }
                            },
                            "user": "SQUIDWRD",
                            "name": "SQUIDWARD",
                            "owner": "LEONARD",
                            "created": 23.046,
                            "defaultgroup": "SYS1",
                            "passdate": 0.0,
                            "passinterval": 186,
                            "phrasedate": null,
                            "attributes": [],
                            "revokedate": null,
                            "resumedate": null,
                            "lastaccess": "23.046/07:13:09",
                            "classauthorizations": [],
                            "logonalloweddays": "ANYDAY",
                            "logonallowedtime": "ANYTIME",
                            "securitylevel": null,
                            "categoryauthorization": null,
                            "securitylabel": null
                        },
                        "omvs": {
                            "uid": 2424,
                            "home": "/u/clarinet",
                            "cputimemax": null,
                            "assizemax": null,
                            "fileprocmax": null,
                            "procusermax": null,
                            "threadsmax": null,
                            "mmapareamax": null
                        }
                    }
                }
            ]
        },
        "returncode": 0,
        "reasoncode": 0
    }
}
```
