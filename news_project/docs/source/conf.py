import os
import sys
import django

# --------------------------------------------------
# Path setup
# --------------------------------------------------

# Add project root to Python path
sys.path.insert(0, os.path.abspath('../..'))

# Tell Sphinx where Django settings are
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'news_project.settings')

# Start Django
django.setup()

# --------------------------------------------------
# Project information
# --------------------------------------------------

project = 'news_project'
copyright = '2026, Matthew Baloyi'
author = 'Matthew Baloyi'
release = '1.0'

# --------------------------------------------------
# General configuration
# --------------------------------------------------

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']

exclude_patterns = []

# --------------------------------------------------
# HTML output
# --------------------------------------------------

html_theme = 'alabaster'

html_static_path = ['_static']