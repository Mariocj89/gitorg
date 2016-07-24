#!/usr/bin/env python
from setuptools import setup

setup(
    name='gitorg',
    packages=['gitorg'],
    version='0.0.1',
    description='Use git for organizations!',
    author='Mario Corchero',
    author_email='mariocj89@gmail.com',
    url='https://github.com/Mariocj89/gitorg',
    keywords=['github', 'sync', 'workspace'],
    test_suite='nose.collector',
    use_2to3=True,
    install_requires=['six', 'PyGithub', 'GitPython'],
    entry_points={
        'console_scripts': [
            'gitorg=gitorg.__main__:main'
        ]
    }
)
