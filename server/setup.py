#!/usr/bin/env python3
"""Setup script to build the back-end server as a package."""
from setuptools import find_packages
from setuptools import setup


NAME = 'back-end-server'
VERSION = '0.1'
URL = 'https://github.com:lekha/banana-bread'
DESCRIPTION = 'A back-end server for a banana-bread bake-off competition.'
LONG_DESCRIPTION = DESCRIPTION


SETUP_DEPS = ()
INSTALL_DEPS = (
    'Flask',
    'flask-login',
    'pymysql',
    'requests-oauthlib',
)
EXTRA_DEPS = {}
TEST_DEPS = ()


if __name__ == '__main__':
    setup(
        name = NAME,
        version = VERSION,
        description = DESCRIPTION,
        long_description = LONG_DESCRIPTION,
        url = URL,
        setup_requires = SETUP_DEPS,
        install_requires = INSTALL_DEPS,
        extras_require = EXTRA_DEPS,
        tests_require = TEST_DEPS,
        packages = find_packages(exclude = ['tests', 'tests.*']),
        include_package_data = True,
    )
