---
layout: default
grand_parent: Data Set Admin
parent: Standard
---

# Profile Extract

Extract a data set profile's profile data. 
{: .fs-6 .fw-300 }

## `DataSetAdmin.extract()`

```python
def extract(
    self,
    data_set: str,
    segments: List[str] = [],
    volume: Union[str, None] = None,
    generic: bool = False,
    profile_only: bool = False,
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
> profile = data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470", profile_only=True)
> if profile["base"]["universalAccess"] == "read":
>     # Do something
> ```
> ✅
> ```python
> if data_set_admin.get_universal_access("ESWIFT.TEST.T1136242.P3020470") == "read":
>   # Do something.
> ```

&nbsp;

Extract a **data set profile's** data.

#### 📥 Parameters
* `data_set`<br>
  The **data set profile** to extract segment data from.

* `segments`<br>
  A list of additional **segments** to extract. The base segment is extracted by default, but providing one or more additional segment keys for other segments in the form of a list will result in those segments being extracted as well.

* `volume`<br>
  A single **volume** name for this data set profile. This argument is optional. If `generic=True` is specified, volume is ignored.

* `generic`<br>
  A bool indicating whether to treat this profile as **generic** or not. This argument is optional and defaults to `False`.

* `profile_only`<br>
  When set to `True`, only the extracted profile will be returned instead of returning the entire **Security Result dictionary**.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `DataSetAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `SegmentError`<br>
  Raises `SegmentError` when the list of **segments** provided contains one or more **unknown** segments.

#### 💻 Example

The following example **extracts** the **base segment** of the data set profile `ESWIFT.TEST.T1136242.P3020470`. The base segment is extracted by default whether or not other segments are specified in the `segments` list.

###### Python REPL
```python
>>> from pyracf import DataSetAdmin
>>> data_set_admin = DataSetAdmin()
>>> data_set_admin.extract("ESWIFT.TEST.T1136242.P3020470")
{"securityResult":{"dataSet":{"name":"ESWIFT.TEST.T1136242.P3020470","operation":"listdata","generic":"no","requestId":"DatasetRequest","commands":[{"safReturnCode":0,"returnCode":0,"reasonCode":0,"image":"LISTDSD  DATASET     ('ESWIFT.TEST.T1136242.P3020470')","profiles":[{"base":{"name":"eswift.test.t1136242.p3020470","level":0,"owner":"eswift","universalAccess":"read","warning":null,"erase":null,"auditing":{"failures":"read"},"notify":null,"yourAccess":"alter","creationGroup":"sys1","dataSetType":"non-vsam","volumes":["usrat2"],"installationData":null,"generic":false}}]}]},"returnCode":0,"reasonCode":0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult": {
    "dataSet": {
      "name": "ESWIFT.TEST.T1136242.P3020470",
      "operation": "listdata",
      "generic": "no",
      "requestId": "DatasetRequest",
      "commands": [
        {
          "safReturnCode": 0,
          "returnCode": 0,
          "reasonCode": 0,
          "image": "LISTDSD  DATASET     ('ESWIFT.TEST.T1136242.P3020470')",
          "profiles": [
            {
              "base": {
                "name": "eswift.test.t1136242.p3020470",
                "level": 0,
                "owner": "eswift",
                "universalAccess": "read",
                "warning": null,
                "erase": null,
                "auditing": {
                  "failures": "read"
                },
                "notify": null,
                "yourAccess": "alter",
                "creationGroup": "sys1",
                "dataSetType": "non-vsam",
                "volumes": [
                  "usrat2"
                ],
                "installationData": null,
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

