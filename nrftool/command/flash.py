# coding: utf-8

"""
Copyright (c) 2014 Paulo Sérgio Borges de Oliveira Filho

Check LICENSE for details.
"""

import os

from .jlink import ExecJLinkScriptCommand

class Flash(ExecJLinkScriptCommand):
	SCRIPT = "flash.jlink"

	def __init__(self, firmware, address, **kwargs):
		super(Flash, self).__init__(**kwargs)
		self.firmware = self.format_firmware(firmware)
		self.address = self.format_address(address)

	def execute(self):
		return super(Flash, self).execute(self.SCRIPT,
			firmware=self.firmware,
			address=self.address
		)

	def format_firmware(self, firmware):
		return os.path.abspath(firmware)

	def format_address(self, address):
		try:
			return hex(int(address))
		except ValueError:
			return address
