---
layout: default
grand_parent: General Resource Admin
parent: Standard
---

# Profile Extract

Extract a general resource profile's profile data. 
{: .fs-6 .fw-300 }

## `ResourceAdmin.extract()`

```python
def extract(
    self, 
    data_set: str, 
    resource: str, 
    class_name: str, 
    segments: List[str] = [], 
    profile_only: bool = False
) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Profile data extracted for experimental **Segments** and **Traits** are considered **Experimental**. See [Segments](../../advanced/segments_traits_operators#segments) and [Traits](../../advanced/segments_traits_operators#traits) for more details._

&nbsp;

{: .warning }
> _Note that it is recommended to extract profile data using the provided **Getter** functions in most cases._
>
> &nbsp;
>
> ❌
> ```python
> profile = resource_admin.extract("TESTING","ELIJTEST", profile_only=True)
> if profile["base"]["universalAccess"] == "read":
>     # Do something
> ```
> ✅
> ```python
> if resource_admin.get_universal_access("TESTING","ELIJTEST") == "read"
>   # Do something.
> ```

&nbsp;

Extract a **general resource profile's** data.

#### 📥 Parameters
* `resource`<br>
  The name of the **general resource profile** being extracted.

* `class_name`<br>
  The name of the **class** the general resource profile being extracted belongs to.

* `segments`<br>
  A list of additional **segments** to extract. The base segment is extracted by default, but providing one or more additional segment keys for other segments in the form of a list will result in those segments being extracted as well.

* `profile_only`<br>
  When set to `True`, only the extracted profile will be returned instead of returning the entire **Security Result dictionary**.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

The following example **extracts** the **base segment** of the general resource profile `TESTING` in the `ELIJTEST` class. The base segment is extracted by default whether or not other segments are specified in the `segments` list.

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

