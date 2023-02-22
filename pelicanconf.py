from datetime import datetime

AUTHOR = "streetyogi"
SITEURL = "https://street.yoga"
# SITEURL = "http://127.0.0.1:8000"
SITENAME = "street.yoga"
SITETITLE = "street.yoga"
SITESUBTITLE = "Yoga & Machines"
SITEDESCRIPTION = """Learn about yoga, or just spinal movements, so much needed for people living a sedentary lifestyle
Lerne Yoga oder natürliche Wirbelsäulenbewegungen, die unverzichtbar sind als ausgleich zu unserer sitzenden Lebensweise
"""
SITELOGO = '/images/logo_quadrat.png'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
THEME_COLOR = 'dark'

ROBOTS = "index, follow"

THEME = "../"
PATH = "content"
OUTPUT_PATH = "blog/"
TIMEZONE = "Europe/Vienna"

DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['pelican-plugins']

PLUGINS = ['pelican_gist']

# JINJA_ENVIRONMENT = {'extensions': ['jinja2.ext.i18n']}

I18N_TEMPLATES_LANG = "en"
DEFAULT_LANG = "en"
OG_LOCALE = "en_US"
LOCALE = "en_US"

DATE_FORMATS = {
    "en": "%B %d, %Y",
}

FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

USE_FOLDER_AS_CATEGORY = False
MAIN_MENU = True
HOME_HIDE_TAGS = True
LINKS = (
        ('streetyoga.capital', 'https://streetyoga.github.io/atapi/'),
        ('imprint', 'https://firmen.wko.at/streetyoga-eu/wien/?firmaid=59c376c3-30b3-495c-a0ee-e48267328364'),
        ('vegan cooking', 'https://hive.blog/@street.yoga')
)

SOCIAL = (
    ("envelope", 'mailto:miron@street.yoga'),
    ("github", "https://github.com/miron"),
    ("instagram", "https://instagram.com/street.yogi"),
    ("linkedin", "https://www.linkedin.com/in/streetyogi")
)

MENUITEMS = (
    ("Archives", "/archives.html"),
    ("Categories", "/categories.html"),
    ("Tags", "/tags.html")
)

CC_LICENSE = {
    "name": "Creative Commons Attribution-ShareAlike 4.0 International License",
    "version": "4.0",
    "slug": "by-sa",
    "icon": True,
    "language": "en_US"
}

COPYRIGHT_YEAR = datetime.now().year
DEFAULT_PAGINATION = 3

DISQUS_SITENAME = "street-yoga"
ADD_THIS_ID = "ra-62d18ff205e38df4"

STATIC_PATHS = ["images", ".well-known"]

EXTRA_PATH_METADATA = {
    '.well-known/nostr.json': {'path': '.well-known/nostr.json'},
}


THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
