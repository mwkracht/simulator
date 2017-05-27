#!/usr/bin/env python

from distutils.core import setup


# Dynamically calculate version from source package
version = __import__('trafficsim').get_version()


setup(
    name='Traffic Simulator',
    version=version,
    url='https://github.com/mwkracht/simulator',
    author='Matthew Kracht',
    author_email='mwkracht@gmail.com',
    description=('A simple traffic simulation utility.'),
    license='MIT',
    packages=['trafficsim', 'trafficsim.display'],
)
