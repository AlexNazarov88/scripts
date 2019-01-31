#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com

Script to walk dirs and subdirs recursively and rename certain files with to a certain pattern
v0.2

to do:
	*make it universal. pass as arguments regex and dst name (what about extensions?)

	*change extension? pass new extension as argument

"""

import sys
sys.dont_write_bytecode = True

import os
import os.path
import argparse
from shutil import move


def main(dirName): 
	preset = 'timing.txt'
	# print "Dir name: " + dirName

	for dirpath, dirnames, filenames in os.walk(dirName):
		for filename in [f for f in filenames if f.endswith(".txt")]:
			print "Dir: " + dirpath
			print "Found: " + filename
			move(dirpath + "/" + filename, dirpath + "/" + preset)
			if not filename.endswith( '.txt' ):
				filename += '.txt'


if __name__ == '__main__': 
    
    print "TXT timings file renamer script - v0.2"
    parser = argparse.ArgumentParser()
    parser.add_argument("dirName", help = "dir name to look for timings")
    args = parser.parse_args()

    main(args.dirName) 
    print "Renamed!"
