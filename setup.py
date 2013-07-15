# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='pyramid_xslt',
      version=version,
      description="Xslt renderer for pyramid",
      long_description= open('README.rst').read(),
      classifiers=['Framework :: Pyramid',
                   'License :: OSI Approved :: MIT License',
                   'Topic :: Text Processing :: Markup :: XML'],
      keywords='pyramid xslt renderer',
      author='Cyprien Le Pannérer',
      author_email='cyplp@free.fr',
      url='https://github.com/cyplp/pyramid_xslt',
      license='MIT',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'lxml',
          'zope.component',
          'zope.interface',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
