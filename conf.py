# Configuration file for the Sphinx documentation builder.

import os
import sys

# -- Path setup --------------------------------------------------------------

# Add any paths to sys.path here (if you have external modules to document)
# Example: sys.path.insert(0, os.path.abspath('../src'))

# -- Project information -----------------------------------------------------

project = 'Brother Printer Driver Guide'
copyright = '2025, Brother Printer Driver Guide'
author = 'Brother Printer Driver Team'

# The full version, including alpha/beta/rc tags
release = '1.0.0'

# -- HTML output settings ----------------------------------------------------

# Title shown in the browser tab and top of HTML pages
html_title = "How to Choose the Right Brother Driver for Your Printer"

# Optional short title (e.g., for nav bar)
html_short_title = "Brother Driver Selection Guide"

# Favicon (place favicon.ico in the root or _static folder)
html_favicon = 'favicon.ico'

# Choose a theme (you can uncomment one of these if you have it installed)
# html_theme = 'sphinx_rtd_theme'
# html_theme = 'alabaster'

# Hide "View page source"
html_show_sourcelink = False

# Allow raw HTML blocks in .rst files
html_allow_unsafe = True

# Enable raw directives (for raw:: html)
raw_enabled = True

# Theme customization options
html_theme_options = {
    'show_powered_by': False,
}

# Paths to templates and static files
templates_path = ['_templates']
# html_static_path = ['_static']  # Uncomment if you include CSS/JS/images

# Patterns to ignore when looking for source files
# exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']
