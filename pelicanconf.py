AUTHOR = 'Cliff'
SITENAME = 'McIndi Solutions LLC'
SITESUBTITLE = 'Senior Technology Leadership for Regulated, Mission-Critical Environments'
SITEDESCRIPTION = (
    'Enterprise security gateways (IBM DataPower/APIC), governed Dev/Ops and automation '
    '(Ansible/Python), and cloud/container modernization (OpenShift/AWS/Azure/GCP). '
    'Predictable outcomes with quantifiable ROI.'
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
    ('Services', '/#services'),
    ('Expertise', '/#pillars'),
    ('Case Studies', '/#case-studies'),
    ('Software', '/#software'),
    ('Our Process', '/#process'),
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
