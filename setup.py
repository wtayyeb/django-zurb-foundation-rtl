# /usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import os

ROOT_DIR = os.path.dirname(__file__)
SOURCE_DIR = os.path.join(ROOT_DIR)

setup(
    name="static-foundation",
    version="6.3.1.0",
    description="Django Zurb Foundation package",
    author="w.tayyeb",
    author_email="w.tayyeb@gmail.com",
    url="https://github.com/wtayyeb/static-foundation",
    license='BSD License',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 3',
        'Topic :: Utilities',
    ],
)
