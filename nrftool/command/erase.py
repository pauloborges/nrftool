# coding: utf-8

"""
Copyright (c) 2014 Paulo Sérgio Borges de Oliveira Filho

Check LICENSE for details.
"""

from .jlink import ExecJLinkScriptCommand

class Erase(ExecJLinkScriptCommand):
	SCRIPT = "erase.jlink"

	def execute(self):
		return super(Erase, self).execute(self.SCRIPT)
