---
layout: default
grand_parent: Dataset Admin
parent: Standard
---

# Dataset Access Attribute

Dataset administration functions for checking a user's Dataset Access Attribute. 
{: .fs-6 .fw-300 }

## `DatasetAdmin.get_your_access()`

```python
def get_your_access(self, dataset: str) -> Union[str, bytes, None]:
```

#### 📄 Description

Check **Your Access** for a dataset profile.

#### 📥 Parameters
* `dataset`<br>
  The **Dataset Profile** for which RACF should check the current user's access level.

#### 📤 Returns
* `Union[str,bytes,None]`<br>
  Returns `None` when the dataset profile has no **Your Access** defined, otherwise returns the access level as a string. If the `DatasetAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import DatasetAdmin
>>> dataset_admin = DatasetAdmin()
>>> dataset_admin.get_your_access("ESWIFT.TEST.T1136242.P3020470")
"read"
```