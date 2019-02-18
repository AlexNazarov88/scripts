#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Author: Oleksandr Nazarov - aleksandr.nazarov@vokigames.com

# Script that parses xml and does operations on material tags.
# This includes complete removal of tag and replacement 
# of absolute texture to specified one.


# *material strip script + png texture script
# в принципе можно обьединить в один скрипт - парсер
# 	- как парсеру знать правилен ли материал?
# 		возможно аутпут использованной в материале текстуры (следующий тег) и запрос инпута Y/N
# 		если да - заменяет путь нужной текстурой, которая была передана в аргументах
# 		нет - удаляет тег
		
# py -2 matstrip.py (+path)export_06-02-2019_0904.xml -t --tex.png 
# 											 -d (deletes all material tags)


import sys
sys.dont_write_bytecode = True

import os.path
import argparse
import re

if __name__ == "__main__":
    parser = argparse.ArgumentParser()




    

# 	parser.add_argument("filePath", help = "path to text file")
# 	args = parser.parse_args()