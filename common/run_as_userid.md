---
layout: default
parent: Common
---

# Run as UserID

Run pyRACF commands as another UserID.
{: .fs-6 .fw-300 }

&nbsp;

{: .experimental }
> _This functionality is **Experimental** and is subject to major changes and even being removed entirely._

&nbsp;

{: .note}
> _Changes made using the functionality described here are scoped to the target "Admin" object instance._

&nbsp;

pyRACF can now leverage a feature of IRRSMO00 where commands can be run under a specified userid. In order to take advantage of this feature, the caller must have `UPDATE` access to the `userid.IRRSMO00` resource in the `SURROGAT` class, where userid represents the specific userid you wish to execute commands as. Further information can be found outlined in [our dependencies note](../../index).

## Example

###### Python Script
```python 
from pyracf import UserAdmin

user_admin = UserAdmin(run_as_userid="squidwrd")
# Any future commands would be run under squidwrd's authority
```

## `SecurityAdmin.set_running_userid()`

```python
def set_running_userid(
    self, new_userid: Union[str, None]
) -> None:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _This functionality is **Experimental** and is subject to major changes and even being removed entirely._

&nbsp;

Set the **z/OS userid** this Admin object will use to run pyRACF commands.

#### 📥 Parameters
* `new_userid`<br>
  The **z/OS userid** this Admin object will use to run pyRACF commands. If you pass in `None`, this will clear any userid previously set for this Admin object.

#### ❌ Raises
* `ImproperUserIdError`<br>
  Raises `ImproperUserIdError` when the **z/OS userid** passed is not a valid string from 1 to 8 characters in length (or `None`).

#### 💻 Example

###### Python REPL
```python 
from pyracf import UserAdmin

user_admin = UserAdmin()
user_admin.set_running_userid("squidwrd")
# Any future commands would be run under squidwrd's authority
```

## `SecurityAdmin.clear_running_userid()`

```python
def clear_running_userid(self) -> None:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _This functionality is **Experimental** and is subject to major changes and even being removed entirely._

&nbsp;

Clear the **z/OS userid** this Admin object will use to run pyRACF commands.

#### 💻 Example

###### Python REPL
```python 
from pyracf import UserAdmin

user_admin = UserAdmin(run_as_userid="squidwrd")
# Any commands run here would be run under squidwrd's authority
user_admin.clear_running_userid()
# Any future commands would be run under the calling user's authority
```

## `SecurityAdmin.get_running_userid()`

```python
def get_running_userid(self) -> None:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _This functionality is **Experimental** and is subject to major changes and even being removed entirely._

&nbsp;

Obtain the **z/OS userid** this Admin object will use to run pyRACF commands.

#### 💻 Example

###### Python REPL
```python 
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(run_as_userid="squidwrd")
>>> user_admin.get_running_userid()
SQUIDWRD
```