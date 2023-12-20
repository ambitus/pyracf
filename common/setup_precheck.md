---
layout: default
parent: Common
---

# Setup Precheck

How to set up and check IRRSMO00 precheck configuration.
{: .fs-6 .fw-300 }

&nbsp;

In order to use `set` or `alter` functions in pyRACF, users must have `READ` authority to the `IRR.IRRSMO00.PRECHECK` resource as outlined in [our dependencies note](../../index).

&nbsp;

A function called `setup_precheck` is included with pyRACF to help streamline this process. You can use this function to verify your level of access, or define the `IRR.IRRSMO00.PRECHECK` profile with no universal access.`

## Example

###### Python Script
```python
from pyracf import setup_precheck

setup_precheck()
```

###### Console Output
```
'IRR.IRRSMO00.PRECHECK' is already defined, and you already have 'ALTER' access!
You are ready to start using pyRACF!
Please ensure other users of pyRACF also have at least 'READ' access.
Review our documentation at https://ambitus.github.io/pyracf/ as well!
```