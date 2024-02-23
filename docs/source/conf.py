# Configuration file for the Sphinx documentation builder.

# -- Project information

project = 'Syncify Documentation'
copyright = '2024, Syncify AB'
author = 'Syncify AB'

release = '0.1'
version = '0.1.0'

# -- General configuration

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.doctest',
    'sphinx.ext.autodoc',
    'sphinx.ext.autosummary',
    'sphinx.ext.intersphinx',
    'myst_parser',
]

intersphinx_mapping = {
    'python': ('https://docs.python.org/3/', None),
    'sphinx': ('https://www.sphinx-doc.org/en/master/', None),
}
intersphinx_disabled_domains = ['std']

templates_path = ['_templates']

# -- Options for HTML output

html_theme = 'sphinx_material'

html_static_path = ['_static']

html_css_files = [
    'custom1.css',
]
html_title = "Documentation"

html_favicon = '_static/favicon.png'
html_logo = '_static/favicon.png'
html_show_sourcelink = False

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}
html_theme_options = {
    'globaltoc_collapse': False,
    'globaltoc_includehidden': False,
    'globaltoc_depth': 3,
    'color_accent': 'light-blue',
}

# -- Options for EPUB output
epub_show_urls = 'footnote'