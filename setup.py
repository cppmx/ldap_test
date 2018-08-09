# -*- coding: utf-8 -*-
import sys
import subprocess
import string
from setuptools import setup, find_packages

sys.path.insert(0, '.')
requirements = ['python-ldap', 'flask-wtf', 'flask-sqlalchemy', 'flask-login']
packages = find_packages(  )

__version__ = '0.0.0.1'
__date__ = '2018/08/09 14:00:00'
__author__ = 'Carlos Colon <espacio.sideral@gmail.com>'
__build__ = subprocess.check_output('git describe --tags --always HEAD'.split()).decode().strip()

with open('web_app/_version.py', 'w+') as f:
    f.write('''\
# I will destroy any changes you make to this file.
# Sincerely,
# setup.py ;)
__version__ = '{}'
__date__ = '{}'
__author__ = '{}'
__build__ = '{}'
'''.format(__version__, __date__, __author__, __build__))

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='ldap_test',
    version=__version__,
    packages=packages,
    install_requires=requirements,
    url='https://github.com/cppmx/ldap_test',
    long_description=long_description,
    long_description_content_type="text/markdown",
    license='BSD',
    author='Carlos Colón',
    author_email='espacio.sideral@gmail.com',
    description='Ldap Test Login',
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: BSD 3-Clause License",
        "Operating System :: OS Independent",
    ),
    options={
        'sdist': {
            'formats': ['gztar', 'zip'],
        },
    }
)
