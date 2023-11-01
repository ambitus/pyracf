---
layout: default
grand_parent: Setropts Admin
parent: Abstractions
---

# Class Attributes

Setropts administration function for accessing the RACF Options Lists that a specified class belongs to. 
{: .fs-6 .fw-300 }

## `SetroptsAdmin.get_class_attributes()`

```python
def get_class_attributes(self, class_name: str) -> Union[List[str], bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _This functionality is currently considered **Experimental** due to it's dependency on **[`SetroptsAdmin.list_racf_options()`](../../base/list_racf_options#setroptsadminlist_racf_options)**. See **[`SetroptsAdmin.list_racf_options()`](../../base/list_racf_options#setroptsadminlist_racf_options)** for more details._

&nbsp;

Get the **Class Attributes** for a specified class.

#### 📥 Parameters
* `class_name`<br>
  The name of the **class** that setropts administration should obtain information on from RACF Options.

#### 📤 Returns
* `Union[List[str], bytes]`<br>
  Returns the setropts's **Class Attributes**. If the `SetroptsAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.get_class_attributes("FACILITY")
["active", "genericProfile", "genericCommand", "raclist"]
```