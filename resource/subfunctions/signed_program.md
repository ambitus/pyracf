---
layout: default
grand_parent: General Resource Admin
parent: Subfunctions
---

# Signed Program

Resource Administration subfunctions for Signed Program Administration.
{: .fs-6 .fw-300 }

&nbsp;

{: .note }
> _This may not be the only step to manage a **Signed Program** in your environment._
> _You may also have to refresh the **PROGRAM** class to enact these changes._
> _Please consult RACF documentation and manuals for an understanding of the **PROGRAM** class._

## `ResourceAdmin.add_signed_program()`

```python
def add_signed_program(self, signed_program_name: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../../base/segments_traits_operators#segments) and [Traits](../../base/segments_traits_operators#traits) for more details._

&nbsp;

Define a new **Signed Program** profile in the **PROGRAM** class.

#### 📥 Parameters
* `signed_program_name`<br>
  The name of the **Signed Program** profile being defined to the **PROGRAM** class.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource on creation. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.
* `AddOperationError`<br>
  Raises `AddOperationError` when the **general resource profile** cannot be added because it already exists.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.add_signed_program("TESTPRGM")
{'securityResult': {'resource': {'name': 'TESTPRGM', 'class': 'PROGRAM', 'operation': 'set', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDEFINE PROGRAM             (TESTPRGM) '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TESTPRGM",
      "class":"PROGRAM",
      "operation":"set",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDEFINE PROGRAM             (TESTPRGM) "
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.alter_signed_program()`

```python
def alter_signed_program(self, signed_program_name: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../../base/segments_traits_operators#segments) and [Traits](../../base/segments_traits_operators#traits) for more details._

&nbsp;

{: .warning }
> _Alter operations in pyracf require READ access to `IRR.IRRSMO00.PRECHECK` in the `XFACILIT` class_
> _This function will not produce output unless the user running the command has this access._

&nbsp;

Alter an existing **Signed Program** profile in the **PROGRAM** class.

#### 📥 Parameters
* `signed_program_name`<br>
  The name of the **Signed Program** profile being defined to the **PROGRAM** class.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does **NOT** exist.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.alter_signed_program("TESTPRGM", traits={"sigver:log_signature_verification_events": "SUCCESS"})
{'securityResult': {'resource': {'name': 'TESTPRGM', 'class': 'PROGRAM', 'operation': 'set', 'requestId': 'ResourceRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RALTER  PROGRAM             (TESTPRGM)  SIGVER   (SIGAUDIT    (SUCCESS))'}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TESTPRGM",
      "class":"PROGRAM",
      "operation":"set",
      "requestId":"ResourceRequest",
      "info":[
        "Definition exists. Add command skipped due  to precheck option"
      ],
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RALTER  PROGRAM             (TESTPRGM)  SIGVER   (SIGAUDIT    (SUCCESS))"
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.extract_signed_program()`

```python
def extract_signed_program(self, signed_program_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Extract an existing **Signed Program** profile in the **PROGRAM** class.

#### 📥 Parameters
* `signed_program_name`<br>
  The name of the **Signed Program** profile being defined to the **PROGRAM** class.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Trait dictionary** of the values of the traits extracted from the **SIGVER** segment of the Resource Profile or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.extract_signed_program("TESTPRGM")
{'signatureRequired': None, 'failProgramLoadCondition': 'never', 'logSignatureVerificationEvents': 'success', 'library': None}
```

###### Trait Dictionary as JSON
```json
{
  "signatureRequired": null,
  "failProgramLoadCondition": "never",
  "logSignatureVerificationEvents": "success",
  "library": null
}
```

## `ResourceAdmin.delete_signed_program()`

```python
def delete_signed_program(self, signed_program_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Delete an existing **Signed Program** profile in the **PROGRAM** class.

#### 📥 Parameters
* `signed_program_name`<br>
  The name of the **Signed Program** profile being defined to the **PROGRAM** class.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is greater than `4`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.delete_signed_program("TESTPRGM")
{'securityResult': {'resource': {'name': 'TESTPRGM', 'class': 'PROGRAM', 'operation': 'del', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDELETE PROGRAM             (TESTPRGM) '}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TESTPRGM",
      "class":"PROGRAM",
      "operation":"del",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDELETE PROGRAM             (TESTPRGM) "
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```