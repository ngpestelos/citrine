# -*- coding: utf-8 -*-
#
# Copyright (C) 2009 Nestor G Pestelos Jr
# All rights reserved.
#
# This software is licensed as described in the file COPYING, which
# you should have received as part of this distribution.

"""Parse an OPML file and return a reading list.

    Outlines can be nested (currently used for outlines two levels deep)

>>>> import opml.parser
>>>> outlines = parser.get_outlines('google-reader-subscriptions.xml')
"""

from xml.dom import minidom

def process_outline(element):
    outline = {}
    keys = element.attributes.keys()
    if 'text' in keys:
        outline['text'] = element.attributes['text'].value
    if 'title' in keys:
        outline['title'] = element.attributes['title'].value
    if 'type' in keys:
        outline['type'] = element.attributes['type'].value
    if 'xmlUrl' in keys:
        outline['xmlUrl'] = element.attributes['xmlUrl'].value
    if 'htmlUrl' in keys:
        outline['htmlUrl'] = element.attributes['htmlUrl'].value

    sub_level = [node for node in element.childNodes if is_outline(node)]
    sub_outlines = [process_outline(node) for node in sub_level]
    if sub_outlines:
        outline['outlines'] = sub_outlines
    return outline

def is_outline(node):
    if node.nodeType == node.ELEMENT_NODE and node.nodeName == 'outline':
        return True
    else: return False

def get_outlines(filename='google-reader-subscriptions.xml'):
    doc = minidom.parse(filename)
    body = doc.getElementsByTagName('body')[0]
    toplevel = [node for node in body.childNodes if is_outline(node)]
    return [process_outline(node) for node in toplevel]

def find_outline(outlines, title):
    return [outline for outline in outlines if outline['title'] == title]
