#!/usr/bin/env python

from setuptools import setup

setup(name='blaz',
      version='0.0.1',
      description='Composable tasks inside docker containers',
      author='Alberto Miorin',
      author_email='alberto.miorin@gmail.com',
      url='https://albertomiorin.com',
      license='MIT',
      py_modules=['blaz'],
      install_requires=['ansicolors'],
      )