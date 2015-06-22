
.. :changelog:

========
History
========

0.1.1 (2015-06-21)
---------------------

* DOC: README.rst: links, Features, Usage, API
* BLD: setup.py console_script entrypoint ``web = websh.web:main``
* BLD: setup.py console_script entrypoint ``x-www-browser- = websh.web:main``
* BUG,REF: websh.py: logging, logging config [07f9a0f]
* BUG,CLN,DOC,REF,TST: websh.py: match_domain, :PymodeLintAuto, argv, logging config [4b33395]
* ENH: websh.py: https://github.com/westurner/dotfiles/blob/master/scripts/web [29c0ca7]
* BLD,RLS: \*, setup.py, __init__.py: ``cookiecutter gh:audreyr/cookiecutter-pypackage`` [e288536]

0.1.2 (2015-06-21)
-------------------
* DOC: README.rst: API docs
* RLS: setup.py, __init__.py: ``__version__ = 0.1.2``
* First release on PyPI

0.1.3 (2015-06-21)
-------------------
* DOC: README.rst, HISTORY.rst: formatting, links, release notes

0.1.4 (2015-06-21)
-------------------
* RLS: setup.py, __init__.py: __version = '0.1.4' [8e33773]
* BUG: websh.py: py26, py34 compat [a6ed31a]
* BLD: tox.ini, .travis.yml: commands = python websh/websh.py -v -t [295abab]
* DOC: websh.py, README.rst: usage docstrings [d054b43]
* DOC: README.rst: links [bc1d06c]
