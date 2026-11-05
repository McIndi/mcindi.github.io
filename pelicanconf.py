AUTHOR = 'Cliff'
SITENAME = 'McIndi Solutions LLC'
SITESUBTITLE = 'Gateway, PKI and Agent Security Engineering'
SITEDESCRIPTION = (
    'Hands-on engineering for IBM DataPower and API Connect estates: certificate '
    'inventory and rotation, post-quantum readiness, and identity for AI agents, '
    'for banks, insurers, and healthcare organizations.'
)
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = "theme/mcindi"
DIRECT_TEMPLATES = ["index", "blog", "archives", "categories", "authors", "tags", "sitemap"]
SITEMAP_SAVE_AS = "sitemap.xml"
BLOG_SAVE_AS = "blog/index.html"
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Custom menu items (the main site sections)
MENUITEMS = (
    ('Engagements', '/#offers'),
    ('Proof', '/#case-studies'),
    ('Team', '/#about'),
)

# Ensure custom domain and Pages metadata get copied into output
STATIC_PATHS = ["static", "extra/CNAME", "extra/.nojekyll", "extra/robots.txt"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/.nojekyll": {"path": ".nojekyll"},
    "extra/robots.txt": {"path": "robots.txt"},
}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
