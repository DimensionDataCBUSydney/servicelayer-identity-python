from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='servicelayer-identity',
      version=version,
      description="Identity Client for the Service Layer",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Anthony Shaw',
      author_email='anthony.shaw@dimensiondata.com',
      url='',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
