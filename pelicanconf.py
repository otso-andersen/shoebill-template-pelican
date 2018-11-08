#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

from datetime import date
CURRENTYEAR = date.today().year



AUTHOR = u'Shoebill Pelican'
SITENAME = u'shoebill'
SITEURL = 'http://localhost:8000'


# By default, new articles will be drafts. To publish them, add [Status: published] to its .md
# (comment the line to have Status: published by default)
#DEFAULT_METADATA = {
#    'status': 'draft',
#}

PATH = 'content'
STATIC_PATHS = ['static']
ARTICLE_URL = '{category}/{slug}.html'
ARTICLE_SAVE_AS = '{category}/{slug}.html'
ARTICLE_LANG_SAVE_AS = '{category}/{slug}-{lang}.html'
ARTICLE_LANG_URL = '{category}/{slug}-{lang}.html'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'
DEFAULT_DATE = 'fs'

# location of the folder containing the theme 
THEME = 'themes/shoebill'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['section_number', 'summary', 'clean_summary', 'photos', 'neighbors', 'pin_to_top', 'render_math','pelican-toc', 'share_post']

# Max Length of summary in List View:
SUMMARY_MAX_LENGTH = 200 

# Best if DEFAULT_PAGINATION % 3 == 0
DEFAULT_PAGINATION = 9



# Use typogrify 
# (particularly important for not breaking templates when using summary|truncate):
TYPOGRIFY = True


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

#############################################################################
# Plugins settings
#############################################################################

# Photos:
PHOTO_LIBRARY = "content/pictures"
PHOTO_GALLERY = (1080, 1080, 75)
PHOTO_ARTICLE = (800, 800, 75)
PHOTO_THUMB = (350, 350, 75)
# N.B: "The image quality, on a scale from 1 (worst) to 95 (best). The default is 75. 
# Values above 95 should be avoided; 100 disables portions of the JPEG compression algorithm, 
# and results in large files with hardly any gain in image quality." (from the PILLOW doc)

# Toc
TOC = {
    'TOC_HEADERS'       : '^h[1-6]', # What headers should be included in
                                     # the generated toc
                                     # Expected format is a regular expression

    'TOC_RUN'           : 'true',    # Default value for toc generation,
                                     # if it does not evaluate
                                     # to 'true' no toc will be generated

    'TOC_INCLUDE_TITLE': 'false',     # If 'true' include title in toc
}

###############################################################################
# Special Theme settings:
#############################################################################

# Display author names (on the thumbnails of posts and at the end of each article)
DISPLAY_AUTHORS = True

# location of the folder containing your images for the theme 
# (BANNER, SITELOGO, CATEGORIES[logo], AUTHOR[cover], AUTHOR[image])
# [!!!IMPORTANT!!! path to the *generated* folder relative to output]:
STATIC_IMAGES_FOLDER = 'static/images'

# Logo for the website (appears on the navigation bar on mobile and as a favicon):
SITELOGO = 'watermark.png'

# Picture to display as a banner on the homepage (comment out to not display):
# (N.B: a HOME_BANNER will supersede an article.banner)
HOME_BANNER = "header_photo.jpg"

# Additional information for your categories (description is a text, logo an image):
CATEGORIES = {
    'category 1': {
        'description': 'A good category, if you ask me.',
        'logo':  'logo.png',
    },
    'category 2': {
        'description': 'This one is a list.',
        'list_template': True,
    }
}

# additional information for the authors: 
    # description: quick bio appearing at the end of each article
    # image: small profile picture appearing beside the name at the end of each article
    # cover: banner image appearing on the author page
    # links: must be a list of tuples (name of the icon, URL of the link). Font Awesome is used for the link icons. First element must contain the name of the icon without fa prefix (see the names on fontawesome.com).
AUTHORS = {
    'Shoebill Pelican': {
        'description': """
            People say I have a bill the shape of a shoe. When I feel angsty, I go and steal some kid's crocs.   
        """,
        'cover': 'profile_cover.jpg',
        'image': 'shoebill_image.jpg',
        'links': (('github', 'https://github.com/otso-andersen'),),
    },
    'Alice Dubois': {
        'description': """
               I like white rabbits and couchsurfing.
        """,
        'cover': 'profile_cover.jpg',
        'image': 'alice_image.jpg',
        'links': (('github', 'https://github.com/otso-andersen'),),
    },
    'Jean Dupont': {
        'description': """
            I like cheese and being French. Follow me on Instagram #winephotos.  
        """,
        'cover': 'profile_cover.jpg',
        'image': 'jean_image.jpg',
        'links': (('github', 'https://github.com/otso-andersen'),),
    }
}

# List of metadata recognized by this theme:
    # Title
    # Status: draft / published
    # SubTitle
    # Tags: tag 1, tag 2
    # Image: picture for the thumbnail and the cover
    # Summary
    # Authors: Author 1, Author 2, Author 3
    # Lang: fr (language of the article, default to english)
    # Date: yyyy-mm-dd (date of creation)
    # Modified: yyyy-mm-dd (date of modification)
    # Gallery: {photo}folder (add the gallery with the photos inside folder)
    # Pin: true (pin the article on the homepage -- multiple pinned articles possible)
    # Cooking_time: 50 min (indicate the time for a cooking recipe)
    # Banner: true (make this the first big article on the homepage -- only one possible)
    # Toc_hidden: true (hide the table of content)
    # Cover: true (use the picture in the metadata Image as a cover on the article page)


