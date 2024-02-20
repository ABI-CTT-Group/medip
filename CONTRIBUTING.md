# How to develop on this project

{PROJECT_NAME} welcomes contributions from the community.

**You need PYTHON 3!**

These instructions are for linux base systems.

## Setting up your own fork of this repo.

1. On GitHub interface click on `Fork` button.
2. Clone your fork of this repo. `git clone git@github.com:YOUR_GITHUB_USERNAME/PROJECT_NAME.git`. This will become your default origin repo.
3. Enter the directory `cd PROJECT_NAME`
4. Add upstream repo `git remote add upstream https://github.com/AUTHOR_NAME/PROJECT_NAME`

## Working on virtual environment

1. Create a virtual environment using `venv`

   ```bash
   python -m venv VIRTUAL_ENVIRONMENT_NAME
   ```
   We recommend naming your virtual environment with your Python version. e.g. venv39 can refer to python version 3.9. 
   so that you can also have multiple virtual environments in different Python versions.
   
   Managing your system python installations is beyond the scope of this documentation. 
   You can point to your preferred python interpreter or use pyven to manage your python versions.  

2. Activate the virtual environment.

   ```bash
   source .VIRTUAL_ENVIRONMENT_NAME/bin/activate
   ```

3. You can later deactivate by:

   ```bash
   deactivate
   ```

## Create a new branch to work on your contribution

Run `git checkout -b MY_BRANCH_NAME`

## Make your changes

Edit the files using your preferred editor. (With  Python project, we recommend Pycharm)


## Build the docs locally with Sphinx

TODO

## Commit your changes

This project uses [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0/).

Example: `fix(package): update setup.py arguments 🎉` (emojis are fine too)

## Push your changes to your fork

Run `git push origin BRANCH`

## Submit a pull request

On GitHub interface, click on `Pull Request` button.

Wait CI to run and one of the developers will review your PR.

## Makefile utilities

This project comes with a `Makefile` that contains a number of useful utility.


## Making a new release

This project uses [semantic versioning](https://semver.org/) and tags releases with `X.Y.Z`
Every time a new tag is created and pushed to the remote repo, GitHub actions will
automatically create a new release on GitHub and trigger a release on PyPI.

For this to work you need to set up a secret called `PIPY_API_TOKEN` on the project `Settings > Secrets and variables > Actinos`, 
this token can be generated on [pypi.org](https://pypi.org/account/).

To trigger a new release all you need to do is:

1. If you have changes to add to the repo
    * Make your changes following the steps described above.
    * Commit your changes following the [conventional git commit messages](https://www.conventionalcommits.org/en/v1.0.0/).
2. Run the tests to ensure everything is working.
4. Run `make release` to create a new tag and push it to the remote repo.

the `make release` will ask you the version number to create the tag, ex: type `0.1.1` when you are asked.

> **CAUTION**:  The make release will change local changelog files and commit all the unstaged changes you have.
