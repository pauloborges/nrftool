# coding: utf-8

"""
Copyright (c) 2014 Paulo Sérgio Borges de Oliveira Filho

Check LICENSE for details.
"""

import argparse
import sys

import nrftool
from nrftool.command import Flash, Erase

USAGE_FLASH = """
\t%(prog)s flash FIRMWARE ADDRESS [--verbose]\
"""

USAGE_ERASE = """
\t%(prog)s erase [--verbose]\
"""

USAGE = USAGE_FLASH + USAGE_ERASE

EPILOG = """
supported nRF devices:
\tnRF51822 (PCA10001)
"""

def build_parser():
	parser = argparse.ArgumentParser(
		prog=nrftool.NAME,
		description=nrftool.SHORT_DESCRIPTION,
		usage=USAGE,
		epilog=EPILOG,
		formatter_class=argparse.RawDescriptionHelpFormatter
	)

	parser.add_argument("-v", "--version",
		action="version",
		version="%(prog)s {v}".format(v=nrftool.VERSION),
		help="print the program version and exit"
	)

	parser.add_argument("--verbose",
		action="store_true",
		help="print the output from JLinkExe"
	)

	subparsers = parser.add_subparsers()

	flash_cmd = subparsers.add_parser("flash",
		help="flash a firmware at the specified address"
	)
	flash_cmd.set_defaults(command="flash")

	flash_cmd.add_argument("firmware")
	flash_cmd.add_argument("address",
		nargs="?",
		default="0x0"
	)

	erase_cmd = subparsers.add_parser("erase",
		help="erase the memory of the target device"
	)
	erase_cmd.set_defaults(command="erase")

	return parser

def build_command(args):
	if args.command == "flash":
		return Flash(args.firmware, args.address, verbose=args.verbose)
	elif args.command == "erase":
		return Erase(verbose=args.verbose)

def main():
	parser = build_parser()
	args = parser.parse_args()

	command = build_command(args)
	sys.exit(command.execute())

if __name__ == "__main__":
	main()
