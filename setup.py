#!/usr/bin/env python3

from setuptools import setup


setup(
    name='semo',
    version='0.1.0a0',
    description='sevenmosquito',
    author='sevenmosquito',
    author_email='yinshaowen241@gmail.com',
    packages=['semo'],
    package_data={
        '': []
        },
    url='https://github.com/cosven/sevenmosquito',
    keywords=['blog', 'homepage', 'site'],
    classifiers=(
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3 :: Only',
        ),
    install_requires=[
        'django==1.10.5',
        'markdown2==2.3.3',
        'PyMySQL==0.7.9',
        'qiniu',
        'djangorestframework',
        'feedgen',
        'mistune',
        ],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
    entry_points={
        'console_scripts': []
        },
    )
