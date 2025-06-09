#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'PyQt5',
    'lxml',
]

test_requirements = [
    'qt',
    'qt4',
    'libxml2'
]

setup(
    name='roLabelImg',
    version='1.3.3',
    description="roLabelImg is a graphical image annotation tool for labeling ROTATED rectangle regions, rewritten from 'labelImg' and supporting rotated bounding boxes.",
    long_description=readme + '\n\n' + history,
    author="TzuTa Lin",
    author_email='tzu.ta.lin@gmail.com',
    url='https://github.com/cgvict/roLabelImg',
    packages=[
        'roLabelImg', 'roLabelImg.libs'
    ],
    package_dir={'roLabelImg': '.'},
    py_modules=['resources'],
    data_files=[('', ['resources.qrc'])],
    entry_points={
        'console_scripts': [
            'roLabelImg=roLabelImg:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='roLabelImg, labelImg, annotation, rotated box',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
