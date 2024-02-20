"""Python setup.py for package_name package"""
import io
from pathlib import Path
from setuptools import find_packages, setup


def read(*paths, **kwargs):
    """Read the contents of a text file safely.
    >>> read("package_name", "VERSION")
    >>> read("README.md")
    ...
    """

    current_dir = Path(__file__).resolve().parent
    file_path = current_dir.joinpath(*paths)
    with io.open(
            file_path,
            encoding=kwargs.get("encoding", "utf8"),
    ) as open_file:
        content = open_file.read().strip()

    return content


def read_requirements(path):
    return [
        line.strip()
        for line in read(path).split("\n")
        if not line.startswith(('"', "#", "-", "git+"))
    ]

setup(
    name="package_name",
    version=read("src/package_name", "VERSION"),
    description="project_description",
    url="https://github.com/author_name/project_urlname/",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",
    author="author_name",
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=read_requirements("requirements.txt"),
    extras_require={"test": read_requirements("requirements-dev.txt")}
)
