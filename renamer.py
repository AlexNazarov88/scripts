#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
sys.dont_write_bytecode = True

import os
import os.path
import argparse

def main(dirName): 
	preset = 'timing.txt'
	print "Dir name: " + dirName

	for dirpath, dirnames, filenames in os.walk(dirName):
		for filename in [f for f in filenames if f.endswith(".txt")]:
			if filename == preset:
				pass
			else:
				print "Dir: " + dirpath
				print "Found: " + filename
				os.rename(dirpath + "/" + filename, dirpath + "/" + preset)
				if not filename.endswith( '.txt' ):
					filename += '.txt'

if __name__ == '__main__': 
    
    print "TXT timings file renamer script - v0.1"
    parser = argparse.ArgumentParser()
    parser.add_argument("dirName", help = "dir name to look for timings")
    args = parser.parse_args()

    main(args.dirName) 
    print "Renamed!"
