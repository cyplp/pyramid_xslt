# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

version = '0.0'

setup(name='pyramid_xslt',
      version=version,
      description="Xslt renderer for pyramid",
      long_description="""\
      """,
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='pyramid xslt renderer',
      author='Cyprien Le Pannérer',
      author_email='cyplp@free.fr',
      url='',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'lxml',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
