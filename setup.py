# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

setup(
    name='geohash',
    version='0.1.0',
    description='Sample AWS Serverless API project',
    long_description=readme,
    author='Gustavo Maia',
    author_email='gustavo.maia@enkel.com.br',
    url='https://github.com/enkelbr/enkel-sample-api',
    packages=find_packages(exclude=('tests', 'docs'))
)
