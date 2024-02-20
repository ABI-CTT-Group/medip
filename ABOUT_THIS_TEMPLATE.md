# About this template

This template was modified from https://GitHub.com/rochacbruno/python-project-template

## HOW TO USE THIS TEMPLATE

1. Clink **Use this template** > **Create a new repository**
2. Set the project name and visibility. then click **Create repository**
3. Clone the new repository to your local drive.
4. Update the README file accordingly. Checklist
   - [ ] Project name
   - [ ] Project descript
   - [ ] badges
   - [ ] Links
5. Making and pushing your first commit

## What is included on the template:
- A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your project.  
- A Makefile with the most useful commands to install, test, lint, format and release your project.
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- Documentation structure using [Sphinx](https://www.sphinx-doc.org)
- [HISTORY.md](HISTORY.md) to store change logs by release using [gitchangelog](https://pypi.org/project/gitchangelog/)
- Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- GitHub repository metadata

## Structure

Repository structure:

```text
├── .GitHub                  # GitHub metadata for repository
│   ├── ISSUE_TEMPLATE            # issue templates
│   └── PULL_REQUEST_TEMPLATE.md  # The CI pipeline for GitHub Actions
├── docs                     # Documentation structure based on Sphinx
    └── source               
        └── conf.py          # The configuration file for your Sphinx docuemntation project
        └── index.rst        # The index page for the docs site
├── scripts                  # scripts using the pacakge 
├── src                      # this template uses the [Python "src" layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/#src-layout-vs-flat-layout). this directory contins the source code for your package.
    ├── package_name             # The main python package for the project
    │         ├── __init__.py          # This tells Python that this is a package
    │         └── VERSION              # The version for the project is kept in a static file
└── tests                    # Unit tests for the project (add mote tests files here)
├── tutorials
├── .gitignore               # A list of files to ignore when pushing to GitHub
├── .readthedocs.yaml        # Read the Docs configuration file
├── ABOUT_THIS_TEMPLATE      # Template information  
├── Containerfile            # A configuration file that automates the steps of creating a container image  
├── CODE_OF_CONDUCT          # code of the conduct 
├── CONTRIBUTING.md          # Onboarding instructions for new contributors
├── HISTORY.md               # Auto generated list of changes to the project
├── LICENSE                  # APACHE 2 
├── Makefile                 # A collection of utilities to manage the project
├── MANIFEST.in              # A list of files to include in a package
├── README.md                # The main readme for the project
├── requirements.txt         # An empty file to hold the requirements for the project
├── requirements-dev.txt     # List of requirements for testing and devlopment
├── setup.py                 # The setup.py file for installing and packaging the project
```

## FAQ

Frequently asked questions.

### Why this template is not using [Poetry](https://python-poetry.org/) ?

I really like Poetry and I think it is a great tool to manage your python projects,
if you want to switch to poetry, you can run `make switch-to-poetry`.

But for this template I wanted to keep it simple.

Setuptools is the simplest and well-supported way of packaging a Python project,
it doesn't require extra dependencies and is the easiest way to install the project.

Also, poetry doesn't have a good support for installing projects in development mode yet.

### Why the `requirements.txt` is empty ?

This template is a low dependency project, so it doesn't have any extra dependencies.
You can add new dependencies as you will, or you can use the `make init` command to
generate a `requirements.txt` file based on the template you choose `flask, fastapi, click etc`.

### Why there is a `requirements-test.txt` file ?

This file lists all the requirements for testing and development,
I think the development environment and testing environment should be as similar as possible.

Except those tools that are up to the developer choice (like ipython, ipdb etc.).

### Why the template doesn't have a `pyproject.toml` file ?

It is possible to run `pip install https://GitHub.com/name/repo/tarball/main` and
have pip to download the package directly from Git repo.

For that to work you need to have a `setup.py` file, and `pyproject.toml` is not
supported for that kind of installation.

I think it is easier for example you want to install specific branch or tag you can
do `pip install https://GitHub.com/name/repo/tarball/{TAG|REVISON|COMMIT}`

People automating CI for your project will be grateful for having a setup.py file

### Why isn't this template made as a cookiecutter template?

I really like [cookiecutter,](https://GitHub.com/cookiecutter/cookiecutter) and it is a great way to create new projects,
but for this template I wanted to use the GitHub `Use this template` button,
to use this template doesn't require to install extra tooling such as cookiecutter.

Just click on [Use this template](https://GitHub.com/rochacbruno/python-project-template/generate) and you are good to go.

The substitutions are done using GitHub actions and a simple sed script.

### Why `VERSION` is kept in a static plain text file?

I used to have my version inside my main module in a `__version__` variable, then
I had to do some tricks to read that version variable inside the setuptools 
`setup.py` file because that would be available only after the installation.

I decided to keep the version in a static file because it is easier to read from
wherever I want without the need to install the package.

e.g: `cat project_name/VERSION` will get the project version without harming
with module imports or anything else, it is useful for CI, logs and debugging.

### Why to include `tests`, `history` and `Containerfile` as part of the release?

The `MANIFEST.in` file is used to include the files in the release, once the 
project is released to PyPI all the files listed on MANIFEST.in will be included
even if the files are static or not related to Python.

Some build systems such as RPM, DEB, AUR for some Linux distributions, and also
internal repackaging systems tends to run the tests before the packaging is performed.

The Containerfile can be useful to provide a safer execution environment for 
the project when running on a testing environment.

I added those files to make it easier for packaging in different formats.

### Why conftest includes a go_to_tmpdir fixture?

When your project deals with file system operations, it is a good idea to use
a fixture to create a temporary directory and then remove it after the test.

Before executing each test pytest will create a temporary directory and will
change the working directory to that path and run the test.

So the test can create temporary artifacts isolated from other tests.

After the execution Pytest will remove the temporary directory.

### Why this template is not using [pre-commit](https://pre-commit.com/) ?

pre-commit is an excellent tool to automate checks and formatting on your code.

However, I figured out that pre-commit adds extra dependency and it an entry barrier
for new contributors.

Having the linting, checks and formatting as simple commands on the [Makefile](Makefile)
makes it easier to understand and change.

Once the project is bigger and complex, having pre-commit as a dependency can be a good idea.

### Why the CLI is not using click?

I wanted to provide a simple template for a CLI application on the project main entry point
click and typer are great alternatives but are external dependencies and this template
doesn't add dependencies besides those used for development.

### Why this doesn't provide a full example of application using Flask or Django?

as I said before, I want it to be simple and multipurpose, so I decided to not include
external dependencies and programming design decisions.

It is up to you to decide if you want to use Flask or Django and to create your application
the way you think is best.

This template provides utilities in the Makefile to make it easier to you can run:

```bash
$ make init 
Which template do you want to apply? [flask, fastapi, click, typer]? > flask
Generating a new project with Flask ...
```

Then the above will download the Flask template and apply it to the project.

## The Makefile

All the utilities for the template and project are on the Makefile

```bash
❯ make
Usage: make <target>

Targets:
help:             ## Show the help.
install:          ## Install the project in dev mode.
fmt:              ## Format code using black & isort.
lint:             ## Run pep8, black, mypy linters.
test: lint        ## Run tests and generate coverage report.
watch:            ## Run tests on every change.
clean:            ## Clean unused files.
virtualenv:       ## Create a virtual environment.
release:          ## Create a new tag for release.
docs:             ## Build the documentation.
switch-to-poetry: ## Switch to poetry package manager.
init:             ## Initialize the project based on an application template.
```
