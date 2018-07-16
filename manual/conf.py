# -*- coding: utf-8 -*-
#
# PyX documentation build configuration file, created by
# sphinx-quickstart on Thu May 19 17:32:57 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os
sys.path.insert(0, '../pyx')
sys.path.insert(0, '..')
import pyx.version

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.mathjax', 'sphinx.ext.todo', 'sphinx.ext.autodoc']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'manual'

# General information about the project.
project = 'PyX'
copyright = pyx.version.date.split('/')[0] + ', Jörg Lehmann, Michael Schindler, André Wobst'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '.'.join(pyx.version.version.split('.')[:1])
# The full version, including alpha/beta/rc tags.
release = pyx.version.version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
today = pyx.version.date
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'pyx'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {'sidebarwidth': 200}

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = ['theme']

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = 'PyX %s Manual' % release

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}
html_sidebars = {
   '**': ['localtoc.html', 'sourcelink.html', 'searchbox.html']
}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'PyXdoc'

todo_include_todos = True


# -- Options for LaTeX output --------------------------------------------------

# The paper size ('letter' or 'a4').
latex_paper_size = 'a4'

# The font size ('10pt', '11pt' or '12pt').
#latex_font_size = '10pt'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('manual', 'manual.tex', 'PyX Manual',
   'Jörg Lehmann, Michael Schindler, André Wobst', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Additional stuff for the LaTeX preamble.
latex_preamble = r'''
  \hypersetup{pdftitle={PyX Manual},
              pdfauthor={Joerg Lehmann <joerg@pyx-project.org>, Michael Schindler <m-schindler@users.sourceforge.net>, Andre Wobst <wobsta@pyx-project.org>},
              pdfsubject={PyX Manual},
              pdfkeywords={PyX, graphics, manual}}
'''

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('manual', 'pyx', 'PyX Manual',
     ['Jörg Lehmann, Michael Schindler, André Wobst'], 1)
]

# -- Other options  ------------------------------------------------------------

mathjax_path = 'http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=default'
todo_include_todos = True
autoclass_content = 'both'
autodoc_member_order = 'bysource'


# -- unprocessed function signature extractor ----------------------------------
# This feature is not robust. It does not parse the code properly, removes
# comments and whitespace doubtfully, requires '):' without space for
# termination, etc.

import inspect

def function_signature_lines(lines):
    # extract the lines of the function definition removing comments
    # and stripping spaces
    for line in lines:
        code = line.split("#", 1)[0].strip()
        yield code
        if code.endswith("):"):
            break

def unprocessed_function_signature(app, what, name, obj, options, sig, retann):
    # extract the unprocessed signature from the source
    if what not in ["class", "method", "staticmethod", "function"]:
        return
    if what == "class":
        # get the constructor (code copied from autodoc)
        obj = getattr(obj, "__init__", None)
        if obj is None or obj is object.__init__ or not \
           (inspect.ismethod(obj) or inspect.isfunction(obj)):
            return
    elif hasattr(obj, '__wrapped__'):
        obj = obj.__wrapped__
    src, line = inspect.findsource(obj)
    code = " ".join(function_signature_lines(src[line:])).split("(", 1)[1][:-2]
    if code.startswith("self, "):
        code = code[6:]
    elif code == "self":
        code = ""
    return "({})".format(code), retann

def remove_default_constructor_docstring(app, what, name, obj, options, lines):
    # remove default constructor docstring, i.e. when no own constructor is defined
    for i, line in enumerate(lines):
        lines[i] = line.replace("x.__init__(...) initializes x; see help(type(x)) for signature", "")

def setup(app):
    app.connect('autodoc-process-signature', unprocessed_function_signature)
    app.connect('autodoc-process-docstring', remove_default_constructor_docstring)
