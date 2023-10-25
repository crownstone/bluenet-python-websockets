#!/usr/bin/env python

from setuptools import setup, find_packages


print(find_packages(exclude=["examples", "experiment", "tests", "techDocs"]))

setup(
    name='BluenetWebSocket',
    version='0.0.1',
    packages=find_packages(exclude=["examples", "DevParser", "tests", "techDocs"]),
    install_requires=[
        'autobahn==17.9.3',
        'Twisted==23.8.0',
    ],
 )