from __future__ import with_statement

import sys
from setuptools import setup


def get_version():
    with open('itunesiap/version.txt') as f:
        return f.read().strip()


def get_readme():
    try:
        with open('README.rst') as f:
            return f.read().strip()
    except IOError:
        return ''


install_requires = [
    'requests[security]', 'prettyexc>=0.6.0',
    'six', 'pytz', 'python-dateutil',
]
tests_require = [
    'pytest>=3.0.0', 'pytest-cov', 'tox', 'mock', 'patch',
]

if sys.version_info[:2] >= (3, 4):
    install_requires.extend([
        'aiohttp', 'aiodns',
    ])
    tests_require.extend([
        'pytest-asyncio==0.5.0'
    ])

setup(
    name='itunes-iap',
    version=get_version(),
    description='Apple iTunes In-app purchase verification api.',
    long_description=get_readme(),
    author='Jeong YunWon',
    author_email='itunesiap@youknowone.org',
    url='https://github.com/youknowone/itunes-iap',
    packages=(
        'itunesiap',
    ),
    package_data={
        'itunesiap': ['version.txt']
    },
    install_requires=install_requires,
    tests_require=tests_require,
    extras_require={
        'tests': tests_require,
        'doc': ['sphinx'],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
