---
layout: page
nav_exclude: true
---

![pyRACF Logo](/assets/images/logo.png)

&nbsp;

Python interface into the RACF management application programming interface.
{: .fs-6 .fw-300 }

&nbsp;

{: .development_status }
> _**pyRACF** is currently in **Beta**, meaning that a subset of functionality is available and considered more or less **Stable** and ready for production, but there is still functionality that is **Experimental** or still needs to be implemented. Please see the annotation below on **Experimental** features._

&nbsp;

{: .experimental }
> _Functionality that is considered **Experimental** will be accompanied by this annotation. This means that the functionality is not tested and or is subject to major changes including even being removed entirely._

&nbsp;

{: .warning }
> _The following **dependencies** are required in order to use pyRACF:_
> * _z/OS **2.4** and higher._
> * _**R_SecMgtOper (IRRSMO00)**: Security Management Operations._
> * _The appropriate RACF authorizations. Details can be found [here](https://www.ibm.com/docs/en/zos/2.3.0?topic=operations-racf-authorization)._

### Install

&nbsp;

{: .note}
 > _pyRACF will eventually be made available on [pypi.org](https://pypi.org/), but currently python wheel distributions for pyRACF are only available for manual download and installation via GitHub._

 &nbsp;

{: .warning}
> _If you get the following error when trying to install pyRACF from GitHub using the provided commands, ensure that you have a `.curlrc` in your **Home Directory** that is configured to point to a **Trusted CA Certificate Bundle**._
>
> ###### CA Certificate Verification Failure
> ```console
>   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
>                                  Dload  Upload   Total   Spent    Left  Speed
>   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
> curl: (60) SSL certificate problem: unable to get local issuer certificate
> More details here: https://curl.haxx.se/docs/sslcerts.html
> 
> curl failed to verify the legitimacy of the server and therefore could not
> establish a secure connection to it. To learn more about this situation and
> how to fix it, please visit the web page mentioned above.
> ```
>
> ###### .curlrc
> ```properties
> capath=/path/to/my/trusted/ca/
> cacert=/path/to/my/trusted/ca/ca.pem
> ```

&nbsp;

[Download & Install From GitHub](https://github.com/ambitus/pyracf/releases)

### Use

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_omvs_uid("squidwrd")
2424
>>> user_admin.set_omvs_uid("squidwrd", 1919)
>>> user_admin.get_omvs_uid("squidwrd")
1919
```

### Mission Statement

As automation becomes more and more prevalent, the need to manage the security environment programmaticaly increases. On z/OS that means managing a security product like the IBM **Resource Access Control Facility** _(RACF)_. RACF is the primary facility for managing identity, authority, and access control for z/OS. There are more than 50 callable services with assembler interfaces that are part of the RACF API. The complete set of interfaces can be found [here](http://publibz.boulder.ibm.com/epubs/pdf/ich2d112.pdf).

&nbsp;

While there are a number of languages that can be used to manage RACF, _(from low level lnaguages like Assembler to higher level languages like REXX)_, the need to have it in a language that is used to manage other platforms is paramount. The pyRACF project is focused on making the RACF management tasks available to Python programmers. This will make it easier to manage RACF from management tools like Ansible and Tekton.

&nbsp;

{: .warning }
> * _pyRACF encodes the data it passes to RACF in Code Page `IBM-1047`._
> * _If you are entering information with special or national characters, users viewing or altering this information from terminals using differnt or international codepages may see unexpected data._
> * _Please consult a list of invariant characters to use for such information if this applies to you._


### Architecture

&nbsp;

<pre class="mermaid">
  graph LR
    subgraph Python
        access[Access Admin] --> parent
        dataset[DataSet Admin] --> parent
        resource[Resource Admin] --> parent
        group[Group Admin] --> parent
        groupconnect[Group Connection Admin] --> parent
        setropts[Setropts Admin] --> parent
        user[User Admin] --> parent
    end
    subgraph C
        parent[Security Admin] --> IRRSMO00
    end
    subgraph System
        IRRSMO00 --> RACF
    end
</pre>
