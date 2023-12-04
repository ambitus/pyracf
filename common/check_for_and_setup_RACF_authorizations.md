---
layout: default
parent: Common
---

# Check for & set up RACF Authorizations

How to check for & set up RACF Authorizations
{: .fs-6 .fw-300 }

&nbsp;

In order to use `set` or `alter` functions in pyRACF, users must have `READ` authority to the `IRR.IRRSMO00.PRECHECK` attribute as outlined in [our dependencies note](../../index).

&nbsp;

To streamline this configuration, we have included a sample script in the "pyracf/scripts" folder in this library. The function defined there is externally callable so that you can verify your level of access, or define the `IRR.IRRSMO00.PRECHECK` profile with no universal access. We encourage you to expand on this sample in your environment using other pyRACF functions in resource or access administrations to ensure the correct users and groups can access this resource and use pyRACF.

## Example

###### Python Script
```python
from pyracf import setup_precheck

setup_precheck()
```

###### Console Output
```
IRR.IRRSMO00.PRECHECK is already defined, and you already have ALTER access!
You are ready to start using pyRACF!
Please ensure other users of pyRACF also have at least read access.
Review our documentation at https://ambitus.github.io/pyracf/ as well!
```