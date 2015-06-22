#!/usr/bin/env python
# -*- coding: utf-8 -*-


try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

requirements = [
]

test_requirements = [
]

__version__ = "0.1.3"
description = (
    """web.sh is a cross-platform script (web) and API for launching a browser"""
    """(with x-www-browser (Linux, Unix), open (OSX), start (Windows),"""
    """or python -m webbrowser)""")

setup(
    name='web.sh',
    version=__version__,
    description=description,
    long_description=readme + '\n\n' + history,
    author="Wes Turner",
    author_email='wes@wrd.nu',
    url='https://github.com/westurner/web.sh',
    packages=[
        'websh',
    ],
    package_dir={'websh':
                 'websh'},
    include_package_data=True,
    install_requires=requirements,
    entry_points="""
    [console_scripts]
    web = websh.websh:main
    x-www-browser- = websh.websh:main
    """,
    license="BSD",
    zip_safe=False,
    keywords='websh browser webbrowser x-www-browser',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
