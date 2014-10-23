#!/usr/bin/python

from setuptools import setup

setup(name='dbs-builder',
      version='0.0.1',
      description='Builder for the dbs project',
      author='Tomas Tomecek',
      author_email='ttomecek@redhat.com',
      url='https://github.com/sYnfo/dbs',
      packages=['dbs_builder', 'dbs_worker'],
)
