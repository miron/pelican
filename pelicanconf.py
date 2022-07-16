from datetime import datetime

AUTHOR = "baby"
SITEURL = "https://beata.street.yoga"
# SITEURL = "http://127.0.0.1:8000"
SITENAME = "beata.street.yoga"
SITETITLE = "beata"
SITESUBTITLE = "Cupcakes & Yoga"
SITEDESCRIPTION = """Treat your body with Cupcakes and Yoga"""
SITELOGO = '/images/logo_quadrat.png'
FAVICON = '/images/favicon.ico'
BROWSER_COLOR = "#333333"
PYGMENTS_STYLE = "monokai"
THEME_COLOR = 'dark'

ROBOTS = "index, follow"

THEME = "Flex"
PATH = "content"
OUTPUT_PATH = "blog/"
TIMEZONE = "Europe/Vienna"

DISABLE_URL_HASH = True

# PLUGIN_PATHS = ['pelican-plugins']

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
LINKS = ()

SOCIAL = (
    ("envelope", 'mailto:beata@street.yoga'),
    ("instagram", "https://instagram.com/baby_pole"),
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
DEFAULT_PAGINATION = 10

DISQUS_SITENAME = "flex-pelican"
ADD_THIS_ID = "ra-62d18ff205e38df4"

STATIC_PATHS = ["images"]

THEME_COLOR_AUTO_DETECT_BROWSER_PREFERENCE = True
THEME_COLOR_ENABLE_USER_OVERRIDE = True

USE_LESS = True
