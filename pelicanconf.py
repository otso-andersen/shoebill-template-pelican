#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import date
CURRENTYEAR = date.today().year

AUTHOR = u'Jean Dupont'
SITENAME = u'Pelican Website'
SITESUBTITLE = u'To see a World in a Grain of Sand <br>And a Heaven in a Wild Flower, <br>Hold Infinity in the palm of your hand <br>And Eternity in an hour. <br><br>&mdash; William Blake'
SITEURL = 'https://otso-andersen.github.io/website-template-pelican'


PATH = 'content'
STATIC_PATHS = ['images', 'category_1','category_2']
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{category}/{slug}-{lang}.html'
ARTICLE_LANG_URL = '{category}/{slug}-{lang}.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

THEME = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


# Blogroll
LINKS = (('my GitHub','https://github.com/otso-andersen/website'),)


PLUGINS = ['encrypt_content']

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

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
