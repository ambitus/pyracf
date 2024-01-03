---
layout: default
parent: Common
---

# Run as Userid

Make security requests as another user.
{: .fs-6 .fw-300 }

&nbsp;

{: .note}
> _Changes made using the functionality described here are scoped to the target "Admin" object instance._

&nbsp;

{: .warning}
> _In order to use `run_as_userid`, the caller must have at least `UPDATE` access to the `userid.IRRSMO00` resource in the `SURROGAT` class, where `userid` represents the specific userid you wish to execute commands as. Further information can be found outlined in [our dependencies note](../../index)._

&nbsp;

The **Running Userid** can be set using the `run_as_userid` class attribute on any "Admin" object as shown in the below example. The **Running Userid** can also be set using the `set_running_userid()` function, which is a class function available on all "Admin" objects.

&nbsp;


## Example

###### Python Script
```python 
from pyracf import UserAdmin

user_admin = UserAdmin(run_as_userid="squidwrd")
# All subsequent requests will be made using squidwrd's authority.
```

## `SecurityAdmin.set_running_userid()`

```python
def set_running_userid(
    self, new_userid: Union[str, None]
) -> None:
```

#### 📄 Description

Set the **z/OS userid** who's authority this "Admin" object will use to make security requests.

#### 📥 Parameters
* `new_userid`<br>
  The **z/OS userid** who's authority this "Admin" object will use to make security requests. If you pass in `None`, this will clear any userid previously set for this "Admin" object.

#### ❌ Raises
* `UserIdError`<br>
  Raises `UserIdError` when the **z/OS userid** provided is not a string value between 1 to 8 characters in length.

#### 💻 Example

###### Python REPL
```python 
from pyracf import UserAdmin

user_admin = UserAdmin()
user_admin.set_running_userid("squidwrd")
# All subsequent requests will be made using squidwrd's authority.
```

###### Python REPL
```python 
from pyracf import UserAdmin

user_admin = UserAdmin(run_as_userid="squidwrd")
# All subsequent requests will be made using squidwrd's authority.
user_admin.set_running_userid(None)
# All subsequent requests will be made using the calling user's authority.
```

## `SecurityAdmin.get_running_userid()`

```python
def get_running_userid(self) -> None:
```

#### 📄 Description

Get the **z/OS userid** who's authority this "Admin" object is using to make security requests.

#### 💻 Example

###### Python REPL
```python 
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin(run_as_userid="squidwrd")
>>> user_admin.get_running_userid()
squidwrd
```