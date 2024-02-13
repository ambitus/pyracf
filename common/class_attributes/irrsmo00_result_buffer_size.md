---
layout: default
grand_parent: Common
parent: Class Attributes
---

# IRRSMO00 Result Buffer Size

Customize the size of the result buffer that IRRSMO00 uses.
{: .fs-6 .fw-300 }

&nbsp;

{: .note}
> _Changes made using the functionality described here are scoped to the target "Admin" object instance._

&nbsp;

{: .note}
> _**IRRSMO00 Result Buffer Size** defaults to **16KB**._

&nbsp;

{: .note}
> _The **IRRSMO00 Result Buffer** is a **Stack Allocated** structure that gets created and released on every **Security Request**._

&nbsp;

{: .warning}
> _**IRRSMO00 Result Buffer Size** must be an integer value **greater than or equal to** `10000`, otherwise `ValueError` will be raised. Avoid values greater than `100000000` **(100MB)**. Large values can result in a `SIGKILL` signal being raised, which will result in the Python process that pyRACF is running under be killed._

&nbsp;

The **IRRSMO00 Result Buffer Size** can be set on any "Admin" object by setting the size of the IRRSMO00 result buffer in **bytes** using the `irrsmo00_result_buffer_size` class attribute through the class contructor. When set, every **IRRSMO00 Result Buffer** will be created with the size that is specified.

## Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(irrsmo00_result_buffer_size=32768)
```
