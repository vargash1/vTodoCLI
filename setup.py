#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Hector Vargas
# @Date:   2016-04-05 6:12:10 am
# @Email:  vargash1@wit.edu
# @Name :  Vargas, Hector
# @Last modified by:   vargash1
# @Last modified time: Friday, April 15th 2016, 5:40:37 am
import os
from setuptools import setup

# Utility function to read the README file.
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "vTodoCLI",
    version = "0.0.0",
    author = "Hector Vargas",
    author_email = "vargash1@wit.edu",
    description = ("vTodoCLI"),
    license = "MIT",
    url = "https://github.com/vargash1/vTodoCLI",
    packages = ['vtodocli'],
    package_dir = {'vtodocli':'vtodocli'},
    package_data = {'vtodocli':['.env']},
    long_description = read('README.md'),
    entry_points = {
        'console_scripts':[
            'vTodoCLI=vtodocli.vTodoCLI:main',
        ],
    }
)
