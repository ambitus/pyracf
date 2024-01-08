---
layout: default
grand_parent: Data Set Admin
parent: Abstractions
---

# Your Access

Data Set Profile Administration functions for checking the user's access to a data set profile. 
{: .fs-6 .fw-300 }

## `DataSetAdmin.get_your_access()`

```python
def get_your_access(self, data_set: str) -> Union[str, bytes, None]:
```

#### 📄 Description

Check **Your Access** for a data set profile.

#### 📥 Parameters
* `data_set`<br>
  The **data set profile** for which RACF should check the current user's access level.

#### 📤 Returns
* `Union[str, bytes, None]`<br>
  Returns `None` when the data set profile has no **Your Access** defined, otherwise returns the access level as a string. If the `DataSetAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import DataSetAdmin
>>> data_set_admin = DataSetAdmin()
>>> data_set_admin.get_your_access("ESWIFT.TEST.T1136242.P3020470")
"read"
```