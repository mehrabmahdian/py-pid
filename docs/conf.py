import os
import sys
sys.path.insert(0, os.path.abspath('../sw'))

# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'py-pid'
copyright = '2025, Mehrab Mahdian'
author = 'Mehrab Mahdian'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # for Google-style or NumPy docstrings
]
templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_rtd_theme"

html_context = {
    "display_github": True,
    "github_user": "mehrabmahdian",
    "github_repo": "py-pid",
    "github_version": "main",
    "conf_py_path": "/",
}



html_static_path = ['_static']
