---
layout: default
parent: Common
---

# Generate Requests Only

Generate request XML that is used to make security requests to IRRSMO00.
{: .fs-6 .fw-300 }

&nbsp;

**Generate Requests Only** mode can be enabled on any "Admin" object by setting the `generate_requests_only` class attribute to `True` through the class constructor. When enabled, IRRSMO00 request XML will be generated and returned to the user in the form of a **bytes object** without attempting to make a request to IRRSMO00.

## Example

###### Python REPL
```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(generate_requests_only=True)
>>> user_admin.add_class_authorizations("squidwrd", ["terminal", "xfacilit"])
b'<securityrequest xmlns="http://www.ibm.com/systems/zos/saf" xmlns:racf="http://www.ibm.com/systems/zos/racf"><user name="squidwrd" operation="set" requestid="UserRequest"><base><racf:clauth operation="add">terminal xfacilit</racf:clauth></base></user></securityrequest>'
```

###### IRRSMO00 Request XML
```xml
<securityrequest xmlns="http://www.ibm.com/systems/zos/saf" xmlns:racf="http://www.ibm.com/systems/zos/racf">
  <user name="squidwrd" operation="set" requestid="UserRequest">
    <base>
      <racf:clauth operation="add">terminal xfacilit</racf:clauth>
    </base>
  </user>
</securityrequest>
```
