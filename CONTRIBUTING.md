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
To ensure that **code formatters _(isort and black)_** and **linters _(flake8 and pylint)_** are always run against your code on **every commit** set up the **pre-commit hooks**.

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

There are two different ways to support the testing effort. You can perform a number of tests, or provide test cases. Test cases should be placed in the /tests directory along side test scripts. The test case should describe:

* A Test case ID that allows people to track the test case. It should contain the type in the ID name:
  * The component involved in the test case (or general if it hits multiple)
  * The Type of test case (Functionality, Security, Usability)
  * A unique ordinal integer
  * Examples: UserFunctionality001 or GeneralUsability005
* A Description of the test - This should define what is being tested and why
* Assumptions and preconditions - What needs to be in place for the test to be made (for example - "User must be logged on in problem program state")
* Any test data that is required for the test to complete
* The steps of the test.
* Passing Result - What consititutes success
* Failing Result - what consititutes failure
* If Automated, the script that is being used to perform the test

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
