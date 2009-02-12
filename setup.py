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
  name = 'OPML Parser',
  version = '0.1',
  description = 'Python library for parsing OPML file',
  long_description = """Parses an OPML file and creates a list.""",
  author = 'Nestor G Pestelos Jr',
  author_email = 'ngpestelos@gmail.com',
  license = 'BSD',
  url = '',
  zip_safe = True,
  classifiers = [
      'Development Status :: 3 - Alpha'],
  packages = ['opml'],
  test_suite = '',
  install_requires = []
)
