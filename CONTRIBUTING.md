# Contributing to pyRACF

Thank you for taking the time to contribute to pyRACF!
The following are a set of guidelines to help you contribute.

**Table Of Contents**

* [Before Getting Started](#before-getting-started)

* [Ways to Contribute](#ways-to-contribute)

  * [Coding](#coding)

  * [pre-commit Hooks](#pre-commit-hooks)

  * [Adding New Functionality](#adding-new-functionality)

  * [Testing](#testing)

  * [Fixing Bugs](#fixing-bugs)

  * [Adding or Fixing Documentation](#adding-or-fixing-documentation)

  * [Branch Naming Conventions](#branch-naming-conventions)

* [Style Guidelines](#style-guidelines)

* [Contribution checklist](#contribution-checklist)

* [Found a bug?](#found-a-bug)

## Before Getting Started

> :warning: _All code contributed must be made under an Apache 2 license._
>
> :warning: _All contributions must be accompanied by a [Developer Certification of Origin (DCO) signoff](https://github.com/openmainframeproject/tsc/blob/master/process/contribution_guidelines.md#developer-certificate-of-origin)._

pyRACF is focused on making it easy for people to managed z/OS security definitions. It is not focused on providing in the moment RACF decisions.

Contributions should be focused not only in creating functionality but also creating something that provides abstraction from the underlying interface.

The ultimate goal is provide something that is intuitive to a security professional without forcing a deep understanding of z/OS and RACF infrastructure.

At the same time the code should provide a map to someone who is interested in the underlying infrastructure. As such the code becomes more than a functional tool, it becomes an educational tool for those interested in exploring it.

## Ways to Contribute

There are many ways to contribute to the project. You can write code, work on the documentation, provide tests, report bugs or provide suggestions for improvement.

### Coding

If you want to write code, a good way to get started is by looking at the issues section of the repository. Look for the **Good First Issue** tag. Good First Issues are great as a first contribution.

### pre-commit Hooks
To ensure that **code formatters _(isort and black)_**, **linters _(flake8 and pylint)_**, and **unit tests** are always run against your code on **every commit** set up the **pre-commit hooks**.

> :warning: _pyRACF uses Poetry as it's **build backend** and for **dependency management**. After installing Poetry, ensure that the install location of Poetry is added to the `$PATH` **environment variable** if it is not already._
* [Install Poetry](https://python-poetry.org/docs/#installation)

* Install dependencies
  ```shell
  poetry install --no-root
  ```
* Setup pre-commit hooks
  ```shell
  poetry run pre-commit install -f
  ```

### Adding New Functionality

If you have a new functionality that can be added to the package, open a GitHub pull request against the `dev` branch with your changes. In the PR, make sure to clearly document the new functionality including why it is valuable.

### Testing

The main way to test pyRACF is to write **unit tests** in the [`tests`](tests) folder which **mock** the real **IRRSMO00 API** to enable **XML generation** and **XML parsing** logic to be validated in a **fast** and **automated** way. The unit test suite can be run by just executing [`test_runner.py`](tests/test_runner.py). It is also recommended to do manual tests on a **z/OS system** for **new functionality** and **bug fixes** to test the real calls to **IRRSMO00**.

Since pyRACF uses Poetry as it's **build backend** and for **dependency management**, the pyRACF unit test suite should be executed as follows:

```shell
poetry run coverage run tests/test_runner.py
```

* **Unit Tests:**

  > :bulb: _See the Python [`unittest`](https://docs.python.org/3/library/unittest.html) and [`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html) documentation for more details on writing test cases._

  > :white_check_mark: _Mocks are mainly used to mock real **API calls** to **IRRSMO00**. This means that the unit testing infrastructure for pyRACF can be run on virtually **any platform** that suports Python since the IRRSMO00 interface portion of pyRACF is the only component of pyRACF that depends on **z/OS APIs**. The IRRSMO00 interface portion of pyRACF is a very small portion of pyRACF that only serves as a mechanism for getting data to the IRRSMO00 C code that invokes the IRRSMO00 callable service and getting results from the IRRSMO00 C code after the IRRSMO00 callable service is done processing. This means that the majority of pyRACF can be tested virtually anywhere Python is supporetd for **fast iteration** using IDEs and **high test coverage**._

  * Unit tests should be placed in the **subfolder** corresponding to the **class** you are creating a test for. Secondly, note that you should place your test case in the **unit test class** that corresponds to the type of functionality you are trying to validate. In general, each **class** you are testing should have **test classes** for **XML generation**, **XML parsing**, **setter functions**, **getter functions**, and **debug logging**. Lastly, there should also be **folders** conatining **XML request samples**, **XML/dictionary result samples**, and **log samples** in the same folder as the **unit tests classes**, and these samples should be loaded in a corresponding **constants module** in that same folder for use in unit test cases. 

    > _**Example:** A test case for verifying that the `UserAdmin.get_uid()` **User Administration** function can extract an **OMVS UID** from **profile extract XML** that contains an **OMVS segment** should be placed in the [`test_user_getters.py`](tests/user/test_user_getters.py) unit test class within the [`users`](tests/user) subfolder. A **profile extract XML** sample that contains an **OMVS Segment** should be created in the [`user_result_samples`](tests/user/user_result_samples) folder that resides within the same folder as the corresponding **unit test classes** if one does not exist already. The **profile extract XML** sample should be loaded in [`test_user_constants.py`](tests/user/test_user_constants.py) and then used to **mock** the **IRRSMO00 response** so that the `UserAdmin.get_uid()` logic can be tested without making a **real API call**._

### Fixing Bugs

If you fix a bug, open a GitHub pull request against the `dev` branch with the fix. In the PR, make sure to clearly describe the problem and the solution approach.

### Adding or Fixing Documentation

If any updates need to be made to the pyRACF documentation, open a GitHub pull request against the `gh-pages-dev` branch with your changes. This may include updates to document new functionality or updates to correct errors or mistakes in the existing documentation.

### Branch Naming Conventions

Code branches should use the following naming conventions:

* `wip/name` *(Work in progress branch that likely won't be finished soon)*
* `feat/name` *(Branch where new functionality or enhancements are being developed)*
* `bug/name` *(Branch where one or more bugs are being fixed)*
* `junk/name` *(Throwaway branch created for experimentation)*

## Style Guidelines

:bulb: _These steps can be done automatically using the [pre-commit Hooks](#pre-commit-hooks)._

* When adding code to pyRACF, follow the PEP8 style guide for Python
* The use of `pylint`, `flake8`, `black`, and `isort` is required.
* We expect all contributions to pass `flake8` and to have a `pylint` score of **10**.

## Contribution checklist

When contributing to pyRACF, think about the following:

* Make any necessary updates to `pyproject.toml`.
* Make any necessary updates to `README.md`.
* Make any necessary updates to the gitHub pages documentation in the `gh-pages` branch _(Pull requests should be opened against the `gh-pages-dev` branch)_.
* Add any available test cases to `/tests`.
* Verify `__init__.py` files are updated properly.
* Ensure that you have __pre-commit Hooks__ setup to ensure that **isort**, **black**, **flake8**, and **pylint** are run against the code for every commit you make.
* Run unit test suite by executing `poetry run coverage run tests/test_runner.py`.
* Install pyRACF on a z/OS system and do a smoke test to make sure no regressions have been introduced with the C code that interfaces with IRRSOM00. [`function_test.py`](tests/function_test/function_test.py) can be used for this smoke test.

## Found a bug?

If you find a bug in the code, please open the an issue.
In the issue, clearly state what is the bug, and  any other details that can be helpful.
