#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True
import run

main_list = [
    'items', \
    'amelia_items', \
    'common_items', \
    'karl_items', \
    'amelia', \
    'karl', \
    'cat', \
    'match3']

def run_function(models = []):
    for i in models:
        run.main(i)
    
if __name__ == "__main__":
    run_function(main_list)
    run.pause()