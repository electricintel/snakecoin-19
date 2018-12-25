# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import sys
import re
import io
from shutil import rmtree

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))


NAME = 'snakecoin'
DESCRIPTION = 'A blockchain for a simple cryptocurrency.'
URL = 'https://github.com/vpaliy/snakecoin'
EMAIL = 'vpaliy97@gmail.com'
AUTHOR = 'Vasyl Paliy'
REQUIRES_PYTHON = '>=3.0'
VERSION = None

with io.open(os.path.join(here, 'snakecoin', '__init__.py'), encoding='utf-8') as fp:
  VERSION = re.compile(r".*__version__ = '(.*?)'", re.S).match(fp.read()).group(1)

try:
  with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()
except FileNotFoundError:
    long_description = str()

try:
  with io.open(os.path.join(here, 'requirements.txt'), encoding='utf-8') as fp:
    requires = [r.strip() for r in fp.readlines()]
except FileNotFoundError:
    requires = [
      'requests',
      'six',
      'future-strings'
    ]

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    long_description=long_description,
    long_description_content_type='text/markdown',
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    license='MIT',
    python_requires=REQUIRES_PYTHON,
    packages=find_packages(exclude=('tests',)),
    install_requires=requires,
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ]
)
