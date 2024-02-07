---
layout: default
grand_parent: Common
parent: Misc
---

# Dump Processing

How pyRACF creates and processes IRRSMO00 Raw Security Result Dumps
{: .fs-6 .fw-300 }

&nbsp;

{: .warning}
> _**IRRSMO00 Raw Security Result XML Dump Files** are **NOT** post-processed. This means that **pyRACF** secrets redaction is not applied. However, IRRSMO00's built-in secrets redaction is always applied, which always redacts known sensitive information such as **Passwords** and **Passphrases**._

&nbsp;

An **IRRSMO00 Raw Security Result XML Dump** can be created in the following scenarios:
* The **Security Result XML** returned by IRRSMO00 is unable be be parsed as XML.
* [Dump Mode](../../class_attributes/dump_mode) is enabled meaning that an **IRRSMO00 Raw Security Result XML Dump** will be triggered on every request *(Both successes and failures)*.

&nbsp;

**IRRSMO00 Raw Security Result XML Dump Files** are created at `~/.pyracf/dump` with the naming convention `pyracf.<timestamp>.<md5>.dump`.

&nbsp;

Both the `.pyracf` directory and the `dump` directory are created with `700` permissions to ensure **ONLY** the running/owning user can access them. If `umask` or the running/owning user creates these directories or otherwise modifies these directories to have permissions other than `700`, pyRACF will automatically change the permissions to `700`. The **IRRSMO00 Raw Security Result XML Dump File** is created with `600` permissions to ensure that **ONLY** the running/owning user can access it. pyRACF will **NOT** attempt to fix the permissions on previously created dump files if the user changes the permissions after the dump file is created.

&nbsp;

{: .warning}
> _If a the **Security Result XML** returned by IRRSMO00 cannot be parsed as XML, a dump is created, and `xml.etree.ElementTree.ParseError` is raised, you should open an issue [here](https://github.com/ambitus/pyracf/issues) if the problem was not the result of user error or a system configuration problem._

&nbsp;

When a dump is created due to the **Security Result XML** not being able to be parsed as XML, pyRACF log print the following messages to the console. After creating the dump, the original `xml.etree.ElementTree.ParseError` will be raised.

###### Console Output
```console
[ FATAL ] Unable to parse result XML returned by IRRSMO00.
[ INFO ] Raw security result XML has been written to '/u/testuser/.pyracf/dump/pyracf.<timestamp>.<md5>.dump'.
```

When a dump is created as a result of [Dump Mode](../../class_attributes/dump_mode) being enabled, pyRACF will print the following message to the console. Normal processing continues after creating the dump.

###### Console Output
```console
[ INFO ] Raw security result XML has been written to '/u/testuser/.pyracf/dump/pyracf.<timestamp>.<md5>.dump'.
```

The **IRRSMO00 Raw Security Result XML Dump File** can be interpreted using a hex dump utility like `xxd` or `od`.

###### Shell
```shell
xxd ~/.pyracf/dump/pyracf.<timestamp>.<md5>.dump
```

###### Shell
```shell
od -t x1 -c ~/.pyracf/dump/pyracf.<timestamp>.<md5>.dump
```