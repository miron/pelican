AUTHOR = 'streetyogi'
SITENAME = 'street.yoga'
SITEURL = 'https://street.yoga'

PATH = 'content'

TIMEZONE = 'Europe/Vienna'

DEFAULT_LANG = 'English'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('github', 'https://github.com/miron/'))

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/streetyogi/'),
          ('instagram', 'https://www.instagram.com/street.yogi/'))

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGINS = [
        'pelican_gist'
]
