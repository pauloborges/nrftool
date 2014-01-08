# coding: utf-8

"""
Copyright (c) 2014 Paulo Sérgio Borges de Oliveira Filho

Check LICENSE for details.
"""

import subprocess
import tempfile
import os

from .base import Command

__all__ = ["ExecJLinkScriptCommand"]

JLINK		= "JLinkExe"
SCRIPT_DIR	= os.path.join(os.path.dirname(os.path.realpath(__file__)),
						"../script")

JLINK_ERRORS = {
	"Can not connect to J-Link via USB.": "Can not find the device.",
	"ERROR: Could not open file.": "Can not find the specified firmware."
}

class JLinkError(Exception):
	def __init__(self, text, linenumber):
		self.text = text
		self.linenumber = linenumber

class ExecJLinkScriptCommand(Command):
	def execute(self, script, **kwargs):
		if len(kwargs) > 0:
			script = create_tmp_script(script, **kwargs)
		else:
			script = generate_abs_path(script)

		try:
			output = subprocess.check_output([JLINK, script],
				universal_newlines=True,
				stderr=subprocess.STDOUT
			)
		except subprocess.CalledProcessError as exception:
			output = exception.output

		return process_output(output, self.verbose)

def create_tmp_script(script, **kwargs):
	content = open(generate_abs_path(script), "r").read().decode("utf-8")
	stream = content.format(**kwargs).encode("utf-8")

	with tempfile.NamedTemporaryFile(delete=False) as f:
		name = f.name
		f.write(stream)

	return name

def generate_abs_path(script):
	return os.path.join(SCRIPT_DIR, script)

def process_output(output, verbose):
	lines = output.split("\n")

	try:
		for i, line in enumerate(lines):
			if line in JLINK_ERRORS:
				raise JLinkError(line, i)
	except JLinkError as error:
		if verbose:
			lines[i] = colorize(error.text)
			print("\n".join(lines))
		else:
			print(colorize(JLINK_ERRORS[error.text]))
		return 1

	if verbose:
		print(output)
	
	return 0

def colorize(s):
	return "\033[01;31m" + s + "\033[00m"
