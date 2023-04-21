# pyRACF

Python interface into the RACF management application programming interface.

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_uid("squidwrd")
2424
>>> user_admin.set_uid("squidwrd", 1919)
>>> user_admin.get_uid("squidwrd")
1919
```

[![Build Status](https://v3.travis.ibm.com/z-innersource/pyRACF.svg?token=9v6Apmv6YSouXWPYsx7p&branch=main)](https://v3.travis.ibm.com/z-innersource/pyRACF)

## Description

As automation becomes more and more prevalent, the need to manage the security environment programmaticaly increases. On z/OS that means managing a security product like the IBM Resource Access Control Facility(RACF). RACF is the primary facility for managing identity, authority, and access control for z/OS. There are more than 50 callable services with assembler interfaces that are part of the RACF API. The complete set of interfaces can be found at:

<http://publibz.boulder.ibm.com/epubs/pdf/ich2d112.pdf>

 While there are a number of languages that can be used to manage RACF, (from low level lnaguages like Assembler to higher level languages like REXX), the need to have it in a language that is used to manage other platforms is paramount. The pyRACF project is focused on making the RACF management tasks available to Python programmers. This will make it easier to manage RACF from management tools like Ansible and Tekton.

## Getting Started

### Dependencies

* z/OS 2.4 and higher.
* R_SecMgtOper (IRRSMO00): Security Management Operations.
* The appropriate RACF authorizations. Detail can be found at: <https://www.ibm.com/docs/en/zos/2.3.0?topic=operations-racf-authorization>

### Installation

```shell
python3 -m pip install git+ssh://git@github.ibm.com/z-innersource/pyRACF@<tag version/branch name>
```

### Usage

In the samples directory you will find examples of user, group, and resource profile management. Additionally there is more information in the [index.md](./docs/index.md) file.

## Help

Questions, comments, and bugs can be discussed on the __[#pyracf](https://ibm-systems-z.slack.com/archives/C0455P33BS4)__ __Slack channel__ in the __IBMZ Slack organization__.

## Authors

* Leonard Carcaramo: lcarcaramo@ibm.com
* Elijah Swift: Elijah.Swift@ibm.com
* Joseph Bostian: jbostian@us.ibm.com
* Melissa Chodziutko: mchodziutko@ibm.com

## Version History

* 0.9 Initial release with IRRSmo00
