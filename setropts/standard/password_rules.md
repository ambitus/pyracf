---
layout: default
grand_parent: Setropts Admin
parent: Standard
---

# Get Password Rules

Setropts administration functions for obtaining the system's password rules. 
{: .fs-6 .fw-300 }

## `SetroptsAdmin.get_password_rules()`

```python
def get_password_rules(self) -> Union[dict, bytes]:
```

#### 📄 Description

Obtain the **Password Rules** for a system.

#### 📥 Parameters
  This method has no parameters.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a dictionary of the **Password Rules** for the system. If the `SetroptsAdmin.generate_requests_only` class attribute is set to `True`, **concatenated Security Request XML bytes** will be returned.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.get_password_rules()
{"rules":[{"minLength":4,"maxLength":8,"content":"********"}],"legend":{"A":"alpha","C":"consonant","L":"alphanumeric","N":"numeric","V":"vowel","W":"no vowel","*":"anything","c":"mixed consonant","m":"mixed numeric","v":"mixed vowel","$":"national","s":"special","x":"mixed all"}}
```