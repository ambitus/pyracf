---
layout: page
nav_exclude: true
---

# pyRACF

Python interface into the RACF management application programming interface.
{: .fs-6 .fw-300 }

&nbsp;

{: .warning }
> _The following **dependencies** are required in order to use pyRACF:_
> * _z/OS **2.4** and higher._
> * _**R_SecMgtOper (IRRSMO00)**: Security Management Operations._
> * _The appropriate RACF authorizations. Details can be found [here](https://www.ibm.com/docs/en/zos/2.3.0?topic=operations-racf-authorization)._

#### Install

```shell
python3 -m pip install pyRACF
```

#### Use

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_uid("squidwrd")
2424
>>> user_admin.set_uid("squidwrd", 1919)
>>> user_admin.get_uid("squidwrd")
1919
```

As automation becomes more and more prevalent, the need to manage the security environment programmaticaly increases. On z/OS that means managing a security product like the IBM Resource Access Control Facility(RACF). RACF is the primary facility for managing identity, authority, and access control for z/OS. There are more than 50 callable services with assembler interfaces that are part of the RACF API. The complete set of interfaces can be found [here](http://publibz.boulder.ibm.com/epubs/pdf/ich2d112.pdf).

&nbsp;

While there are a number of languages that can be used to manage RACF, (from low level lnaguages like Assembler to higher level languages like REXX), the need to have it in a language that is used to manage other platforms is paramount. The pyRACF project is focused on making the RACF management tasks available to Python programmers. This will make it easier to manage RACF from management tools like Ansible and Tekton.

&nbsp;

<pre class="mermaid">
  graph LR
    subgraph Python
    AccessAdmin --> SecurityAdmin
    DataSetAdmin --> SecurityAdmin
    ResourceAdmin --> SecurityAdmin
    GroupAdmin --> SecurityAdmin
    SetroptsAdmin --> SecurityAdmin
    UserAdmin --> SecurityAdmin
    end
    subgraph C
    SecurityAdmin --> IRRSMO00
    end
    subgraph System
    IRRSMO00 --> RACF
    end
</pre>
