#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

test_requirements = ['pytest>=3', ]

setup(
    author="Arushi Gautam Saranath",
    author_email='arushisaranath@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="This works with specific details of animal behavior measurement tools",
    entry_points={
        'console_scripts': [
            'animal_behavior_technicals=animal_behavior_technicals.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='animal_behavior_technicals',
    name='animal_behavior_technicals',
    packages=find_packages(include=['animal_behavior_technicals', 'animal_behavior_technicals.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/arushisaranath/animal_behavior_technicals',
    version='1.2.1',
    zip_safe=False,
)
