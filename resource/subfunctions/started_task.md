---
layout: default
grand_parent: General Resource Admin
parent: Subfunctions
---

# Started task

Resource Administration subfunctions for Started Task Administration.
{: .fs-6 .fw-300 }

&nbsp;

{: .note }
> _This may not be the only step to manage a **Started Task** in your environment._
> _You may also have to refresh the **STARTED** class to enact these changes._
> _Please consult RACF documentation and manuals for an understanding of the **STARTED** class._

## `ResourceAdmin.add_started_task()`

```python
def add_started_task(self, started_task_name: str, traits: dict = {}) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../../base/segments_traits_operators#segments) and [Traits](../../base/segments_traits_operators#traits) for more details._

&nbsp;

Define a new **Started Task** profile in the **STARTED** class.

#### 📥 Parameters
* `started_task_name`<br>
  The name of the **Started Task** profile being defined to the **STARTED** class.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource on creation. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AddOperationError`<br>
  Raises `AddOperationError` when the **general resource profile** cannot be added because it already exists.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.add_started_task("TSTTSKEL")
{'securityResult': {'resource': {'name': 'TSTTSKEL', 'class': 'STARTED', 'operation': 'set', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDEFINE STARTED             (TSTTSKEL) ', 'messages': ['ICH10006I RACLISTED PROFILES FOR STARTED WILL NOT REFLECT THE ADDITION(S) UNTIL A SETROPTS REFRESH IS ISSUED.']}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TSTTSKEL",
      "class":"STARTED",
      "operation":"set",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDEFINE STARTED             (TSTTSKEL) ",
          "messages":[
            "ICH10006I RACLISTED PROFILES FOR STARTED WILL NOT REFLECT THE ADDITION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.alter_started_task()`

```python
def alter_started_task(self, started_task_name: str, traits: dict = {}) -> Union[dict, bytes]:
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

Alter an existing **Started Task** profile in the **STARTED** class.

#### 📥 Parameters
* `started_task_name`<br>
  The name of the **Started Task** profile being defined to the **STARTED** class.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does **NOT** exist.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.alter_started_task("TSTTSKEL",traits={"stdata:trusted": True})
{'securityResult': {'resource': {'name': 'TSTTSKEL', 'class': 'STARTED', 'operation': 'set', 'requestId': 'ResourceRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RALTER  STARTED             (TSTTSKEL)  STDATA   (TRUSTED     (YES))', 'messages': ['IRR52148I Warning: A value for USER should be specified in STDATA.', 'IRR52149I Warning: STARTED profiles should have (or match) names with two qualifiers.', 'ICH11009I RACLISTED PROFILES FOR STARTED WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED.']}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TSTTSKEL",
      "class":"STARTED",
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
          "image":"RALTER  STARTED             (TSTTSKEL)  STDATA   (TRUSTED     (YES))",
          "messages":[
            "IRR52148I Warning: A value for USER should be specified in STDATA.",
            "IRR52149I Warning: STARTED profiles should have (or match) names with two qualifiers.",
            "ICH11009I RACLISTED PROFILES FOR STARTED WILL NOT REFLECT THE UPDATE(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.extract_started_task()`

```python
def extract_started_task(self, started_task_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Extract an existing **Started Task** profile in the **STARTED** class.

#### 📥 Parameters
* `started_task_name`<br>
  The name of the **Started Task** profile being defined to the **STARTED** class.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Trait dictionary** of the values of the traits extracted from the **STDATA** segment of the Resource Profile or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.extract_started_task("TSTTSKEL")
{'user': None, 'group': None, 'trusted': 'yes', 'privileged': None, 'trace': None}
```

###### Trait Dictionary as JSON
```json
{
  "user": null,
  "group": null,
  "trusted": "yes",
  "privileged": null,
  "trace": null
}
```

## `ResourceAdmin.delete_started_task()`

```python
def delete_started_task(self, started_task_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Delete an existing **Started Task** profile in the **STARTED** class.

#### 📥 Parameters
* `started_task_name`<br>
  The name of the **Started Task** profile being defined to the **STARTED** class.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **SAF Return Code** of a **Security Result** is equal to `4`.
* `DownstreamFatalError`<br>
  Raises `DownstreamFatalError` when the **SAF Return Code** of a **Security Result** is greater than `4`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.delete_started_task("TSTTSKEL")
{'securityResult': {'resource': {'name': 'TSTTSKEL', 'class': 'STARTED', 'operation': 'del', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDELETE STARTED             (TSTTSKEL) ', 'messages': ['ICH12002I RACLISTED PROFILES FOR STARTED WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED.']}]}, 'returnCode': 0, 'reasonCode': 0, 'runningUserid': 'testuser'}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"TSTTSKEL",
      "class":"STARTED",
      "operation":"del",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDELETE STARTED             (TSTTSKEL) ",
          "messages":[
            "ICH12002I RACLISTED PROFILES FOR STARTED WILL NOT REFLECT THE DELETION(S) UNTIL A SETROPTS REFRESH IS ISSUED."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```