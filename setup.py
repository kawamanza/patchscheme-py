# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def get_version():
    return '0.0.1'


setup(
    name='patchscheme',
    version=get_version(),
    description=(
        'A lightweight library for handling patch '
        'actions to the dict objects.'
    ),
    long_description='',
    author='Marcelo Manzan',
    author_email='manzan@gmail.com',
    url='https://github.com/kawamanza/patchscheme-py',
    packages=find_packages(),
)
