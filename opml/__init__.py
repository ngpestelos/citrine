# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Nestor G Pestelos Jr
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from opml import *

try:
    __version__ = __import__('pkg_resources').get_distribution('OPML_Parser').version
except:
    __version__ = '?'
