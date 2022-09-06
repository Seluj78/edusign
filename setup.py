#!/usr/bin/env python
"""
Sentry-Python - Sentry SDK for Python
=====================================
**Sentry-Python is an SDK for Sentry.** Check out `GitHub
<https://github.com/getsentry/sentry-python>`_ to find out more.
"""
import os

from setuptools import find_packages
from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def get_file_text(file_name):
    with open(os.path.join(here, file_name)) as in_file:
        return in_file.read()


setup(
    name="edusign",
    version="0.0.3",
    author="Jules Lasne",
    author_email="jules.lasne@gmail.com",
    url="https://github.com/seluj78/edusign",
    project_urls={
        # TODO: Add documentation link
        # "Documentation": "https://edusign.readthedocs.io/en/stable/index.html",
        # TODO: Change this to an real changelog
        "Changelog": "https://github.com/Seluj78/edusign/commits/main",
    },
    description="Python client for Edusign (https://edusign.fr)",
    long_description=get_file_text("README.md"),
    long_description_content_type="text/markdown",
    packages=find_packages(exclude=("tests", "tests.*")),
    zip_safe=False,
    license="GNU GPL 3",
    install_requires=[
        "requests",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
