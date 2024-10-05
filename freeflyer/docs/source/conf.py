# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'FreeFlyer'
copyright = '2024, Brandi McPherson'
author = 'Brandi McPherson'
release = 'n/a'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autosectionlabel', 'rst2pdf.pdfbuilder' ]



templates_path = ['_templates']
exclude_patterns = []

language = 'n/a'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
html_logo = "../freeflyer.png"
html_theme_options = {
    'logo_only': True,
    'display_version': False,
}
html_css_files = [
    'custom.css',
]

# pdf_documents = [('index', u'rst2pdf', u'Sample rst2pdf doc', u'Your Name'),]