#!/usr/bin/env python
import os
from setuptools import setup, find_packages

README_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)),
                           'README.md')

dependencies = [
    'nltk',
    'beautifulsoup4',
    'lxml',
    'cssutils'
]

setup(
    name='pycaption',
    version='0.1',
    description='Multi-language caption reader/writer',
    author='Joe Norton',
    author_email='joey@nortoncrew.com',
    url='https://github.com/pbs/pycaption',
    install_requires = dependencies,
    packages = find_packages(),
    include_package_data=True,
)
