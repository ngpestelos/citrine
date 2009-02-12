#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Nestor G Pestelos Jr
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
  name = 'Citrine',
  version = '0.1',
  description = 'Python library for parsing OPML files',
  long_description = """Parses an OPML file and creates a list. Currently used for feed lists.""",
  author = 'Nestor G Pestelos Jr',
  author_email = 'ngpestelos@gmail.com',
  license = 'BSD',
  url = '',
  zip_safe = True,
  classifiers = [
      'Development Status :: 3 - Alpha'],
  packages = ['citrine'],
  test_suite = '',
  install_requires = []
)
