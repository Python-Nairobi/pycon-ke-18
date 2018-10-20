#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Python Nairobi'
SITENAME = 'PyCon-KE 2018'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Africa/Nairobi'

DEFAULT_LANG = 'en'

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
SOCIAL = (
    ('github', 'https://github.com/python-nairobi'),
    ('twitter', 'https://twitter.com/pynbo'),
    ('meetup', 'https://www.meetup.com/Python-Nairobi/'),
    ('blog', 'http://blog.pynbo.or.ke/'),
    ('facebook', 'https://www.facebook.com/PythonNairobi/'),
    ('youtube', 'https://www.youtube.com/channel/UCRDIwuaMTjxCvKyMdKqv6uw'),
)

THEME = "pelican-pyconke-18"
NAVITEMS = (
    ('PyConKe 18', '/'),
    #('Registration', '/registration'),
    ('Schedule', '/schedule'),
    #('Call for Proposals', '/call_for_proposals'),
    #('Volunteering', '/call_for_volunteers'),
    ('CoC', '/coc')
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

VOLUNTEER_LINK = "call_for_volunteers"
PROPOSALS_LINK = ""
SPONSOR_LINK = "mailto:sponsorthis@pycon.or.ke"

STATIC_PATHS = [
    'images',
    'js',
    'css',
    'extra/robots.txt',
    'CNAME',
    'README.md',
]

TICKET_CATEGORIES = (
    ('early_bird', '500', 'https://mookh.com/item-details/e856d1c5-7b0a-48e0-8aea-101fda06193e'),
    #('corporate', '1000')
)

DIRECT_TEMPLATES = [
    'index', 'schedule', 'categories', 'authors', 'archives'
]