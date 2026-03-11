AUTHOR = 'Cliff'
SITENAME = 'McIndi Solutions LLC'
SITESUBTITLE = 'Hands-On Engineering for Critical Infrastructure'
SITEDESCRIPTION = (
    'We design, build, and operate enterprise security gateways, automation pipelines, '
    'and cloud platforms for healthcare, financial services, and high-security environments. '
    '20+ years of hands-on delivery — from architecture through production.'
)
SITEURL = ""

PATH = "content"

TIMEZONE = 'America/New_York'

DEFAULT_LANG = 'en'

THEME = "theme/mcindi"
DIRECT_TEMPLATES = ["index", "blog", "archives", "categories", "authors", "tags"]
BLOG_SAVE_AS = "blog/index.html"
DISPLAY_PAGES_ON_MENU = True
DISPLAY_CATEGORIES_ON_MENU = False

# Custom menu items (the main site sections)
MENUITEMS = (
    ('What We Build', '/#services'),
    ('Outcomes', '/#pillars'),
    ('Case Studies', '/#case-studies'),
    ('Software', '/#software'),
    ('How We Ship', '/#process'),
    ('About', '/#about'),
    ('Contact', '/#contact'),
    ('Blog', '/blog/'),
)

# Ensure custom domain and Pages metadata get copied into output
STATIC_PATHS = ["static", "extra/CNAME", "extra/.nojekyll"]
EXTRA_PATH_METADATA = {
    "extra/CNAME": {"path": "CNAME"},
    "extra/.nojekyll": {"path": ".nojekyll"},
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
