---
layout: default
parent: Common
---

# Null Response Error

Understanding the `NullResponseError` exception.
{: .fs-6 .fw-300 }

&nbsp;

{: .note }
> _pyRACF requires a response xml string from an internal call to the IRRSMO00 callable service to provide proper output. If the response string that pyRACF receives is empty, pyRACF raises a `NullResponseError` and terminate processing the response from IRRSMO00._

&nbsp;

After executing any operation, pyRACF expects a non-empty response string from IRRSMO00 in order to parse such a response and surface information back to the user. When pyRACF detects an empty response string, a `NullResponseError` is raised and processing terminates. It is possible that the command was executed prior to receiving a null response, but this is not the case for any known causes of this error.

&nbsp;

The only known cause of this error is that the user does not have `READ` authority to the `IRR.IRRSMO00.PRECHECK` attribute as outlined in [our dependencies note](../../index). If you are not certain if you have this authority or if this has been established in your environment, please consult our [Check for & set up RACF Authorizations](../check_for_and_setup_RACF_authorizations) documentation.

###### Python Script
```python
from pyracf import UserAdmin
from pyracf import NullResponseError

user_admin = UserAdmin()

try:
    user_admin.set_uid("squidwrd", 123456)
except AddOperationError as e:
    print(e.message)
```

###### Console Output
```console
Security request made to IRRSMO00 failed.

Check to see if proper RACF permissions are in place.
For `set` or `alter` functions, you must have at least READ access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class.
```