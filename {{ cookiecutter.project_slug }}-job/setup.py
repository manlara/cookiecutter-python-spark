import os
import sys
from setuptools import setup

setup(
  name = '{{ cookiecutter.project_slug }}',
  packages = ['{{ cookiecutter.project_slug }}'], # this must be the same as the name above
  include_package_data=True,
  version = '{{ cookiecutter.version }}',
  description = '{{ cookiecutter.project_short_description }}',
  long_description = open('README.md').read(),
  long_description_content_type = 'text/markdown',
  author = '{{ cookiecutter.author_name }}',
  author_email = '{{ cookiecutter.author_email }}',
  url = '', # use the URL to the github repo
  keywords = [], # arbitrary keywords
  classifiers = ['Development Status :: 4 - Beta'],
) 