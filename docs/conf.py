# Configuration file for the Sphinx documentation builder.
#
# Full list of options can be found in the Sphinx documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import sys
from typing import Any, Dict

project = "SVRP"
copyright = "2023 • Vir0z4 Network IT"
author = "VAIO Library"

# -- General configuration ---------------------------------------------------
#

extensions = [
    # Sphinx's own extensions
    "sphinx.ext.autodoc",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx.ext.todo",
    "sphinx.ext.viewcode",
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
    "sphinx_inline_tabs",
]
templates_path = ["_templates"]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]
myst_heading_anchors = 3

# -- Options for HTML output -------------------------------------------------
#

html_theme = "furo"
html_title = "Sony VAIO Recovery Patcher - Documentation"
language = "en"

html_static_path = ["_static"]
html_css_files = ["pied-piper-admonition.css"]


#if "READTHEDOCS" in os.environ:
#    html_theme_options["announcement"] = (
#        "This is an "
#        "announcement."
#    )


html_js_files = []
html_context: Dict[str, Any] = {}
# html_show_sphinx = False
# html_show_copyright = False
# html_last_updated_fmt = ""

RTD_TESTING = False
if RTD_TESTING or "FURO_RTD_TESTING" in os.environ:
    del html_theme_options["footer_icons"]

    html_css_files += [
        "https://assets.readthedocs.org/static/css/readthedocs-doc-embed.css",
        "https://assets.readthedocs.org/static/css/badge_only.css",
    ]
    html_js_files += [
        "readthedocs-dummy.js",
        "https://assets.readthedocs.org/static/javascript/readthedocs-doc-embed.js",
    ]
    html_context["READTHEDOCS"] = True
    html_context["current_version"] = "latest"
    html_context["conf_py_path"] = "/docs/"
    html_context["display_github"] = True
    html_context["github_user"] = "Vir0z4"
    html_context["github_repo"] = "svrp"
    html_context["github_version"] = "main"
    html_context["slug"] = "svrp"

FONT_AWESOME_TESTING = False
if FONT_AWESOME_TESTING:
    html_css_files += [
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/fontawesome.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/solid.min.css",
        "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/brands.min.css",
    ]

    html_theme_options["footer_icons"] = [
        {
            "name": "GitHub",
            "url": "https://github.com/Vir0z4/svrp",
            "html": "",
            "class": "fa-solid fa-github fa-2x",
        },
    ]
