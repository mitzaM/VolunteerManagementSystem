#!/usr/bin/env python
# -*- encoding: utf-8 -*-
import os
from glob import glob
from os.path import basename
from os.path import splitext

from setuptools import find_packages
from setuptools import setup

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='VolunteerManagementSystem',
    version='0.1',
    description='Volunteer Management System',
    long_description=README,
    author='Mihai Man',
    author_email='mitaman89@gmail.com',
    url='https://www.tiff.ro/',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    include_package_data=True,
    zip_safe=False,

    install_requires=[
        'Django>=1.10',
        'pytz==2017.2',
        'requests==2.8.1',
        'psycopg2==2.6.1',
        'django-debug-toolbar==1.5',
    ],

    license='GNU GENERAL PUBLIC License',

    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.9.5',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU GENERAL PUBLIC License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
