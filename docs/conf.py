import os
import sys
sys.path.insert(0, os.path.abspath('../sw'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
project = 'py_pidx'
copyright = '2025, Mehrab Mahdian'
author = 'Mehrab Mahdian'

# -- General configuration ---------------------------------------------------
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # for Google-style or NumPy docstrings
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------
html_theme = "furo"

html_context = {
    "display_github": True,              # Show GitHub link in the docs
    "github_user": "mehrabmahdian",     # Your GitHub username
    "github_repo": "py_pidx",             # Your GitHub repo name
    "github_version": "main",             # Branch name
    "conf_py_path": "/",                  # Path in the repo to your docs root
}

# html_static_path = ['_static']
