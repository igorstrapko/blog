#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
from typogrify.filters import typogrify

#AUTHORS = ['Good Praxist Igor', 'Maciej Baron']
SITENAME = 'My Blog'
SITEURL = 'https://igorstrapko.github.io/blog'

PATH = 'content'

TIMEZONE = 'Europe/London'

TYPOGRIFY = True
TYPOGRIFY_IGNORE_TAGS = []

DEFAULT_LANG = 'en'
# DISPLAY_PAGES_ON_MENU = False
# DISPLAY_CATEGORIES_ON_MENU = False

## THEMES
#THEME = 'theme/basic'
#THEME = 'theme/sober'
#THEME = 'theme/#svbtle'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True