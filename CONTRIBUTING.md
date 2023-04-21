# Contributing to pyRACF

Thank you for taking the time to contribute to pyRACF!
The following are a set of guidelines to help you contribute.

**Table Of Contents**

* [Before getting started](#before-getting-started)

* [Ways to contribute](#ways-to-contribute)

* [Style Guidelines](#style-guidelines)

* [Contribution checklist](#contribution-checklist)

* [Found a bug?](#found-a-bug)

## Before getting started

pyRACF is focused on making it easy for people to managed z/OS security definitions. It is not focused on providing in the moment RACF decisions.

Contributions should be focused not only in creating functionality but also creating something that provides abstraction from the underlying interface.

The ultimate goal is provide something that is intuitive to a security professional without forcing a deep understanding of z/OS and RACF infrastructure.

At the same time the code should provide a map to someone who is interested in the underlying infrastructure. As such the code becomes more than a functional tool, it becomes an educational tool for those interested in exploring it.

## Ways to contribute

There are many ways to contribute to the project. You can write code, work on the documentation, provide tests, report bugs or provide suggestions for improvement.

### Coding

If you want to write code, a good way to get started is by looking at the issues section of the repository. Look for the **Good First Issue** tag. Good First Issues are great as a first contribution.

### pre-commit Hooks
To ensure that **code formatters _(isort and black)_**, **linters _(flake8 and pylint)_**, and **unit tests** are always run against your code on **every commit** set up the **pre-commit hooks**.

* Install development dependencies
  ```shell
  python3 -m pip install -r requirements-development.txt
  ```
* Setup pre-commit hooks
> :warning: _If your workstation cannot find `pre-commit`, ensure that the **Python package** `bin` directory location is added to the `$PATH` **environment variable**._
  ```shell
  pre-commit install -f
  ```

### Adding new functionality

If you have a new functionality that can be added to the package, open a GitHub pull request with the code. In the PR, make sure to clearly document the new functionality including why it is valuable.

### Testing

There are two different ways to support the testing effort. The first way pyRACF can be tested is by creating sample scripts in the [`samples`](samples) folder which requires that the user logon to a **z/OS system** and run the scripts to **manually validate** a piece of functionality. The other method, is to write **unit tests** in the [`tests`](tests) folder which **mock** the real **IRRSMO00 API** to enable **XML generation** and **XML parsing** logic to be validated in a **fast** and **automated** way. It is recommended to implement **both** since the sample scripts help validate that **real API calls** work and provides examples of how pyRACF can be used, and the automated unit testing helps ensure that the majority of the functionality provided can be validated **quickly** and **easily** by just running the [`test_runner.py`](tests/test_runner.py).

* **Samples:**
  * Sample scripts should be placed in the the **subfolder** corresponding to the **class** you are providing a sample for. 

    > _**Example:** An **Add User** sample should go in the [`user`](samples/user) subfolder._
* **Unit Tests:**

  > :bulb: _See the Python [`unittest`](https://docs.python.org/3/library/unittest.html) and [`unittest.mock`](https://docs.python.org/3/library/unittest.mock.html) documentation for more details on writing test cases._

  > :warning: _Mocks are mainly used to mock real **API calls** to **IRRSMO00**. This means that the unit testing infrastructure for pyRACF can be run on virtually **any platform** that suports Python since the IRRSMO00 interface portion of pyRACF is the only component of pyRACF that depends on **z/OS APIs**._

  * Unit tests should be placed in the **subfolder** corresponding to the **class** you are creating a test for. Secondly, note that you should place your test case in the **unit test class** that corresponds to the type of functionality you are trying to validate. In general, each **class** you are testing should have **test classes** for **XML generation**, **XML parsing**, **Setter functions**, and **Getter functions**. Lastly, there should also be **folders** conatining **XML request samples** and **XML/dictionary result samples** in the same folder as the **unit tests classes**, and these samples should be loaded in a corresponding **constants module** in that same folder for use in unit test cases. 

    > _**Example:** A test case for verifying that the `UserAdmin.get_uid()` **User Administration** function can extract an **OMVS UID** from **profile extract XML** that contains an **OMVS segment** should be placed in the [`test_user_getters.py`](tests/user/test_user_getters.py) unit test class within the [`users`](tests/user) subfolder. A **profile extract XML** sample that contains an **OMVS Segment** should be created in the [`user_result_samples`](tests/user/user_result_samples) folder that resides within the same folder as the corresponding **unit test classes** if one does not exist already. The **profile extract XML** sample should be loaded in [`test_user_constants.py`](tests/user/test_user_constants.py) and then used to **mock** the **IRRSMO00 response** so that the `UserAdmin.get_uid()` logic can be tested without making a **real API call**._

### Fixing bugs

If you fix a bug, open a GitHub pull request with the fix. In the PR, make sure to clearly described the problem and the solution approach.

### Adding or fixing documentation

If you want to improve the current documentation, that includes adding new documentation, fixing grammar, spelling, and format errors open a GitHub pull request with your changes.

## Style Guidelines

* When adding code to pyRACF, follow the PEP8 style guide for Python
* The use of Flake8, Black, and pydocstyle as helpers is recommended
* It is strongly recommended that you perform a pylint check on your code. We expect it to have a pylint score greater than 9

## Contribution checklist

When contributing to pyRACF, think about the following:

* Make any necessary updates to setup file
* Make any necessary updates to README file
* Make any necessary updates to /docs/index.md
  * Add / modify any documentation here
* Make any necessary updates to /docs/about.md
  * Add your name as a contributor, if you are not part of the list
* Add any available test cases to /tests
* Verify **init** files are updated properly
* Ensure that you have __pre-commit Hooks__ setup to ensure that **isort**, **black**, **flake8**, and **pylint** are run against the code for every commit you make.
* Test installation of pyzkiln package after updates are made

## Found a bug?

If you find a bug in the code, please open the an issue.
In the issue, clearly state what is the bug, and  any other details that can be helpful.
