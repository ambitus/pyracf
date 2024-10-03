![pyRACF Logo](https://raw.githubusercontent.com/ambitus/pyracf/refs/heads/main/logo.png)

[![tests](https://github.com/ambitus/pyracf/actions/workflows/unittest.yml/badge.svg)](https://github.com/ambitus/pyracf/actions/workflows/unittest.yml)
[![coverage](https://github.com/ambitus/pyracf/actions/workflows/coverage.yml/badge.svg)](https://github.com/ambitus/pyracf/actions/workflows/coverage.yml)
[![pylint](https://github.com/ambitus/pyracf/actions/workflows/pylint.yml/badge.svg)](https://github.com/ambitus/pyracf/actions/workflows/pylint.yml)
[![flake8](https://github.com/ambitus/pyracf/actions/workflows/flake8.yml/badge.svg)](https://github.com/ambitus/pyracf/actions/workflows/flake8.yml)
[![Beta Version](https://img.shields.io/pypi/v/pyracf?label=beta)](https://pypi.org/project/pyracf/#history)
[![Python Versions](https://img.shields.io/pypi/pyversions/pyracf)](https://pypi.org/project/pyracf/)
[![Download Stats](https://img.shields.io/pypi/dm/pyracf)](https://pypistats.org/packages/pyracf)

> ⚠️ _If this is not what you are looking for, it is likely because you are looking for a different package that used to be distributed under the `pyracf` name. You may instead be looking for the [`mfpandas`](https://pypi.org/project/mfpandas/) package, which was distributed under the `pyracf` name prior to October 2024._

Python interface into the RACF management application programming interface.

```python
>>> from pyracf import UserAdmin
>>> user_admin = UserAdmin()
>>> user_admin.get_omvs_uid("squidwrd")
2424
>>> user_admin.set_omvs_uid("squidwrd", 1919)
>>> user_admin.get_omvs_uid("squidwrd")
1919
```

## Description

As automation becomes more and more prevalent, the need to manage the security environment programmatically increases. On z/OS that means managing a security product like the IBM Resource Access Control Facility (RACF). RACF is the primary facility for managing identity, authority, and access control for z/OS. There are more than 50 callable services with assembler interfaces that are part of the RACF API.

[RACF callable services interfaces](http://publibz.boulder.ibm.com/epubs/pdf/ich2d112.pdf)

 While there are a number of languages that can be used to manage RACF, (from low level languages like Assembler to higher level languages like REXX), the need to have it in a language that is used to manage other platforms is paramount. The pyRACF project is focused on making the RACF management tasks available to Python programmers. This will make it easier to manage RACF from management tools like Ansible and Tekton.

## Getting Started

### Dependencies

* z/OS 2.4 and higher.
* R_SecMgtOper (IRRSMO00): Security Management Operations.
* [The appropriate RACF authorizations](https://www.ibm.com/docs/en/zos/2.5.0?topic=operations-racf-authorization)

### Installation

```shell
pip install pyracf
```

> 💡 _You may also optionally [Download & Install pyRACF From GitHub](https://github.com/ambitus/pyracf/releases)._

### Usage

* [pyRACF Documentation](https://ambitus.github.io/pyracf/)

## Help

* [Github Discussions](https://github.com/ambitus/pyracf/discussions)

## Authors

* Joe Bostian: jbostian@ibm.com
* Frank De Gilio: degilio@us.ibm.com
* Leonard Carcaramo: lcarcaramo@ibm.com
* Elijah Swift: Elijah.Swift@ibm.com
