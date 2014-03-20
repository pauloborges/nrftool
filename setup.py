#!/usr/bin/env python
# coding: utf-8

import os
import sys

from setuptools import setup, find_packages
import nrftool

def clean():
	os.system("rm -rf dist *.egg-info")

def publish():
	os.system("python setup.py sdist upload")

if "publish" in sys.argv:
	clean()
	publish()
	sys.exit()

elif "clean" in sys.argv:
	clean()
	sys.exit()

setup(
	name=nrftool.NAME,
	version=nrftool.VERSION,

	description=nrftool.SHORT_DESCRIPTION,
	license=nrftool.LICENSE,
	author=nrftool.AUTHOR,
	author_email=nrftool.AUTHOR_EMAIL,
	url=nrftool.URL,

	packages=find_packages(),
	package_data={ "nrftool": ["script/*.jlink"] },
	entry_points={ "console_scripts": ["nrftool = nrftool.cmdline:main"] },

	classifiers=[
		"Development Status :: 3 - Alpha",
		"Environment :: Console",
		"License :: OSI Approved :: MIT License",
		"Natural Language :: English",
		"Operating System :: POSIX :: Linux",
		"Programming Language :: Python :: 2",
	],
)
