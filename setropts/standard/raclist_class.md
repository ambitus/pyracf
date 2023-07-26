---
layout: default
grand_parent: Setropts Admin
parent: Standard
---

# Raclist Class

Setropts administration functions for modifying if a class has the Raclist attribute. 
{: .fs-6 .fw-300 }

## `SetroptsAdmin.add_raclist_class()`

```python
def add_raclist_class(self, class_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Add a class to the list of classes that RACF has **Raclisted**.

#### 📥 Parameters
* `class_name`<br>
  The name of the **class** to add the raclist attribute to.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ConnectionAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.add_raclist_class("ELIJTEST")
{'step1': {'securityResult': {'systemSettings': {'operation': 'set', 'requestId': 'SetroptsRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'SETROPTS      RACLIST    (ELIJTEST)'}]}, 'returnCode': 0, 'reasonCode': 0}}}
```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1":{
    "securityResult":{
      "systemSettings":{
        "operation":"set",
        "requestId":"SetroptsRequest",
        "commands":[
          {
            "safReturnCode":0,
            "returnCode":0,
            "reasonCode":0,
            "image":"SETROPTS      RACLIST    (ELIJTEST)"
          }
        ]
      },
      "returnCode":0,
      "reasonCode":0
    }
  }
}
```


## `SetroptsAdmin.remove_raclist_class()`
remove_raclist_class
```python
def remove_raclist_class(self, class_name: str) -> Union[dict, bytes]:
```

#### 📄 Description

Remove a class from the list of classes that RACF has **Raclisted**.

#### 📥 Parameters
* `class_name`<br>
  The name of the **class** to remove the raclist attribute from.

#### 📤 Returns
* `Union[dict, bytes]`<br>
  Returns a **Security Result Steps dictionary** or **Concatenated Security Request XML bytes** if the `ConnectionAdmin.generate_requests_only` class attribute is set to `True`.

#### ❌ Raises
* `SecurityRequestError`<br>
  Raises `SecurityRequestError` when the **Return Code** of a **Security Result** returned by IRRSMO00 is **NOT** equal to `0`.

#### 💻 Example

###### Python REPL
```python
>>> from pyracf import SetroptsAdmin
>>> setropts_admin = SetroptsAdmin()
>>> setropts_admin.remove_raclist_class("ELIJTEST")
{'step1': {'securityResult': {'systemSettings': {'operation': 'set', 'requestId': 'SetroptsRequest', 'commands': [{'safReturnCode': 0, 'returnCode': 0, 'reasonCode': 0, 'image': 'SETROPTS    NORACLIST    (ELIJTEST)'}]}, 'returnCode': 0, 'reasonCode': 0}}}

```

###### Security Result Steps Dictionary as JSON
```json
{
  "step1":{
    "securityResult":{
      "systemSettings":{
        "operation":"set",
        "requestId":"SetroptsRequest",
        "commands":[
          {
            "safReturnCode":0,
            "returnCode":0,
            "reasonCode":0,
            "image":"SETROPTS    NORACLIST    (ELIJTEST)"
          }
        ]
      },
      "returnCode":0,
      "reasonCode":0
    }
  }
}
```