#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'https://otso-andersen.github.io/website-template-pelican'
RELATIVE_URLS = False

FEED_ALL_ATOM = 'feeds/all.atom.xml'
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
#GOOGLE_ANALYTICS = ""

###############################################################################
# Special Theme settings:

THEME_HEADERPICTURE = SITEURL + '/images/header_photo.jpg'

THEME_CATEGORIES = {
    'category_1': {
        'description': 'Description for category 1',
        'logo': SITEURL + '/category_1/logo.png',
        'thumbnail': 'https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e002152/GSFC_20171208_Archive_e002152~orig.jpg',
    },
    'category_2': {
        'description': 'Description for category 2'
    }
}



THEME_AUTHORS = {
    'Jean Dupont': {
        'description': """
            Description of the author Jean Dupont
        """,
        'cover': 'https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e002152/GSFC_20171208_Archive_e002152~orig.jpg',
        'image': SITEURL + '/images/jean.jpg',
        'links': (('github', 'https://github.com/otso-andersen'),),
    },
    'Alice Dubois': {
        'description': """
            Description of the author Alice Dubois
        """,
        'cover': 'https://images-assets.nasa.gov/image/GSFC_20171208_Archive_e002152/GSFC_20171208_Archive_e002152~orig.jpg',
        'image': SITEURL + '/images/alice.jpg',
        'links': (('github', 'https://github.com/otso-andersen'),),
    }
}
