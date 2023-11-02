---
layout: default
grand_parent: General Resource Admin
parent: Subfunctions
---

# Custom Field

Resource Administration functions for Custom Field Administration
{: .fs-6 .fw-300 }

&nbsp;

{: .note }
> _This may not be the only step to manage a **Custom Field** in your environment._
> _You may also have to refresh the **CFIELD** class to enact these changes._
> _Please consult RACF documentation and manuals for an understanding of the **CFIELD** class._

## `ResourceAdmin.add_custom_field()`

```python
  def add_custom_field(
        self, custom_field_name: str, custom_field_type: str, traits: dict = {}
  ) -> Union[dict, bytes]:
```

#### 📄 Description

&nbsp;

{: .experimental }
> _Only a subset of available **Segments** and **Traits** are considered **Stable**. See [Segments](../../base/segments_traits_operators#segments) and [Traits](../../base/segments_traits_operators#traits) for more details._

&nbsp;

Define a new **Custom Field** profile in the **CFIELD** class.

#### 📥 Parameters
* `class_name`<br>
  The name of the **Custom Field** profile being defined to the **CFIELD** class.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource on creation. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AddOperationError`<br>
  Raises `AddOperationError` when the **general resource profile** cannot be added because it already exists.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.add_custom_field("TVSHOW","user")
{'securityResult': {'resource': {'name': 'USER.CSDATA.TVSHOW', 'class': 'CFIELD', 'operation': 'set', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDEFINE CFIELD             (USER.CSDATA.TVSHOW) '}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"USER.CSDATA.TVSHOW",
      "class":"CFIELD",
      "operation":"set",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDEFINE CFIELD             (USER.CSDATA.TVSHOW) "
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.alter_custom_field()`

```python
  def alter_custom_field(
        self, custom_field_name: str, custom_field_type: str, traits: dict = {}
  ) -> Union[dict, bytes]:
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

Alter an existing **Custom Field** profile in the **CFIELD** class.

#### 📥 Parameters
* `class_name`<br>
  The name of the **Custom Field** profile being defined to the **CFIELD** class.

* `traits`<br>
  A dictionary of **traits/attributes** that should be given to the resource on creation. See [Traits](../../base/segments_traits_operators#traits) to see what all of the valid **Resource Traits** are.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.
* `AlterOperationError`<br>
  Raises `AlterOperationError` when the **z/OS userid** supplied cannot be altered because it does **NOT** exist.
* `SegmentTraitError`<br>
  Raises `SegmentTraitError` when the dictionary of **traits/attributes** provided contains one or more **unknown** traits.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
cf_traits = {
  "cfdef:help_text":"Favorite TV Show",
  "cfdef:valid_first_characters":"ALPHA",
  "cfdef:valid_other_characters":"ALPHA"
}
resource_admin.alter_custom_field("TVSHOW","user",traits=cf_traits)
{'securityResult': {'resource': {'name': 'USER.CSDATA.TVSHOW', 'class': 'CFIELD', 'operation': 'set', 'requestId': 'ResourceRequest', 'info': ['Definition exists. Add command skipped due  to precheck option'], 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': "RALTER  CFIELD             (USER.CSDATA.TVSHOW)  CFDEF    (HELP        ('Favorite TV Show') FIRST       (ALPHA) OTHER       (ALPHA))", 'messages': ['IRR52216I An error was detected in the definition of custom field USER.CSDATA.TVSHOW. MAXLENGTH is missing or incorrect for a field with TYPE(CHAR).']}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"USER.CSDATA.TVSHOW",
      "class":"CFIELD",
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
          "image":"RALTER  CFIELD             (USER.CSDATA.TVSHOW)  CFDEF    (HELP        ('Favorite TV Show') FIRST       (ALPHA) OTHER       (ALPHA))",
          "messages":[
            "IRR52216I An error was detected in the definition of custom field USER.CSDATA.TVSHOW. MAXLENGTH is missing or incorrect for a field with TYPE(CHAR)."
          ]
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```

## `ResourceAdmin.extract_custom_field()`

```python
  def extract_custom_field(
        self, custom_field_name: str, custom_field_type: str
  ) -> Union[dict, bytes]:
```

#### 📄 Description

Extract an existing **Custom Field** profile in the **CFIELD** class.

#### 📥 Parameters
* `class_name`<br>
  The name of the **Custom Field** profile being defined to the **CFIELD** class.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Trait dictionary** of the values of the traits extracted from the **CFDEF** segment of the Resource Profile or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.extract_custom_field("SHELCITY")
{"customFieldDataType": "char", "maxlength": None, "maxNumericValue": None, "minNumericValue": None, "validFirstCharacters": "alpha", "validOtherCharacters": "alpha", "mixedCaseAllowed": None, "helpText": ["favorite", "tv", "show"]}
```

###### Trait Dictionary as JSON
```json
{
  "customFieldDataType": "char",
  "maxlength": None,
  "maxNumericValue": None,
  "minNumericValue": None,
  "validFirstCharacters": "alpha",
  "validOtherCharacters": "alpha",
  "mixedCaseAllowed": None,
  "helpText": ["favorite", "tv", "show"],
}
```

## `ResourceAdmin.delete_custom_field()`

```python
  def delete_custom_field(
        self, custom_field_name: str, custom_field_type: str
  ) -> Union[dict, bytes]:
```

#### 📄 Description

Delete an existing **Custom Field** profile in the **CFIELD** class.

#### 📥 Parameters
* `class_name`<br>
  The name of the **Custom Field** profile being defined to the **CFIELD** class.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result dictionary** or **Security Request XML bytes** if the `ResourceAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
from pyracf import ResourceAdmin
resource_admin = ResourceAdmin()
resource_admin.delete_custom_field("TVSHOW","user")
{'securityResult': {'resource': {'name': 'USER.CSDATA.TVSHOW', 'class': 'CFIELD', 'operation': 'del', 'requestId': 'ResourceRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'RDELETE CFIELD             (USER.CSDATA.TVSHOW) '}]}, 'returnCode': 0, 'reasonCode': 0}}
```

###### Security Result Dictionary as JSON
```json
{
  "securityResult":{
    "resource":{
      "name":"USER.CSDATA.TVSHOW",
      "class":"CFIELD",
      "operation":"del",
      "requestId":"ResourceRequest",
      "commands":[
        {
          "safReturnCode":0,
          "returnCode":0,
          "reasonCode":0,
          "image":"RDELETE CFIELD             (USER.CSDATA.TVSHOW) "
        }
      ]
    },
    "returnCode":0,
    "reasonCode":0
  }
}
```