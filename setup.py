#!/usr/bin/env python
from setuptools import setup, find_packages


DESCRIPTION = "Unified API for loading, converting, and interacting with in-memory molecular " \
              "dynamics trajectory formats."


setup(name='mdharmony',
      version='0.1.0',
      description=DESCRIPTION,
      author='Connor Brinton',
      author_email='connorb3@stanford.edu',
      url='https://github.com/connorbrinton/mdharmony',
      license='GPLv2 or later',
      packages=find_packages())
