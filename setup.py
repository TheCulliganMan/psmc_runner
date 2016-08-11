#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='psmc_runner',
    version='0.0.1',
    description='psmc_runner package for Python-Guide.org',
    long_description=readme,
    author='Ryan Culligan',
    author_email='rrculligan@gmail.com',
    url='https://github.com/TheCulliganMan/psmc_runner',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
