# coding: utf-8

"""
Copyright (c) 2014 Paulo Sérgio Borges de Oliveira Filho

Check LICENSE for details.
"""

class Command(object):
	def __init__(self, verbose=False, jlinkexe='JLinkExe', **kwargs):
		self.verbose = verbose
		self.jlinkexe = jlinkexe
