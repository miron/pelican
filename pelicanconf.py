AUTHOR = 'streetyogi'
AUTHORS = 'streetyogi'
SITENAME = 'street.yoga'
# SITEURL = 'https://street.yoga'

PATH = 'content'

TIMEZONE = 'Europe/Vienna'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Python', 'https://python.org'),)

# Social widget
SOCIAL = (('linkedin', 'https://www.linkedin.com/in/streetyogi/'),
          ('instagram', 'https://www.instagram.com/street.yogi/'),
          ('github', 'https://github.com/miron/'),)


# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
PLUGINS = [
        'pelican_gist'
] 

# DIRECT_TEMPLATES = ('index', 'blog']
# PAGINATED_DIRECT_TEMPLATES = ('assets','categories', 'archives', 'blog') # For backdrop theme
# PAGINATED_TEMPLATES = {'assets': None, 'categories': None, 'archives': None, 'blog': None, 'author': None, 'articles': None}
DEFAULT_PAGINATION = True # necessary for basic theme



