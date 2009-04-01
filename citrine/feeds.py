# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Nestor G Pestelos Jr
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

from couchdb import Server
import parser
from datetime import datetime

def load_from_file(filename, dbname):
    "Load feeds from OPML to a CouchDB database"
    outlines = parser.get_outlines(filename)
    db = Server()[dbname]
    for outline in outlines:
        load_outline(db, outline)

def load_outline(db, outline):
    xmlUrl  = outline.get('xmlUrl', '')
    title   = outline.get('title', '')
    htmlUrl = outline.get('htmlUrl', '')
    children = outline.get('outlines', [])
    row = { 'title' : outline.get('title', ''), \
      'feedtype': outline.get('type', ''), \
      'htmlUrl': outline.get('htmlUrl', ''), \
      'type': 'feed',
      'posted': datetime.today().ctime()}

    if xmlUrl and xmlUrl != '':
        print "Creating a new record for %s" % xmlUrl
        try:
            db[xmlUrl] = row
        except:
            print "Oops: " + xmlUrl, "with length:", len(xmlUrl)

    for child in children:
        load_outline(db, child)
