#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
sys.dont_write_bytecode = True

import os
sys.path.insert(1, os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), 'utils', 'resbuilder'))
import script

from subprocess import check_call

def repo():
	return os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

def convert(folder, file, ver = 3):
	#converts xml model to binary
	full = os.path.join(folder, file)
	try:
		print(os.path.splitext(file)[0])
		check_call(['python', '-B', os.path.join('binpy', 'modelxmltobin.py'), '-' + str(ver), full])
	except Exception:
		print('Failed ' + full)
		sys.exit(1)
	script.run(['pack_file', full + '.bin'])

def convert_folder(folder, skip = [], ver3 = []):
	#converts xml files in the folder to binary
	for item in os.listdir(folder):
		if os.path.splitext(item)[1] == '.xml':
			if item not in skip:
				convert(folder, item, 3 if item in ver3 else 4)

def merge_models(folder):
	try:
		print('Merging models in ', folder)
		check_call(['python', '-B', os.path.join('binpy', 'merge_models_xml.py'), folder])
	except Exception:
		print('Failed ' + folder)
		sys.exit(1)

def run_items():
	# список устаревших предметов
	old = ['axe.xml', \
		'BookNormal.xml', 'brush_mm.xml', \
		'CoffeeCup.xml', \
		'golf_klugka.xml', 'grably.xml', 'guitar_mm.xml', \
		'Item_Bagor.xml', 'Item_BirdCage.xml', 'Item_CardBox.xml', \
		'kiy.xml', \
		'Lantern.xml', 'letter.xml', \
		'metla.xml', \
		'palka.xml', 'paper.xml', 'pen.xml', \
		'scissors.xml', 'shovel.xml', 'spray.xml', 'super_grably.xml', 'swing.xml', \
		'tabletpc.xml', 'trubka.xml', 'kost.xml', 'leyka.xml']
	convert_folder(os.path.join(repo(), 'base_mm', 'models', 'Items'), [], old)

def run_amelia_items():
	convert_folder(os.path.join(repo(), 'base_mm', 'models', 'Items', 'AmeliaItems'), ['amelia_items_book.sit.xml', 'amelia_items_book.stay.xml'])
	merge_models(os.path.join(repo(), 'base_mm', 'models', 'Items', 'AmeliaItems', 'amelia_items_book'))

def run_common_items():
	merge_models(os.path.join(repo(), 'base_mm', 'models', 'Items', 'CommonItems', 'rockingchair_01'))
	merge_models(os.path.join(repo(), 'base_mm', 'models', 'Items', 'CommonItems', 'rockingchair_02'))
	merge_models(os.path.join(repo(), 'base_mm', 'models', 'Items', 'CommonItems', 'rockingchair_03'))

def run_karl_items():
	convert_folder(os.path.join(repo(), 'base_mm', 'models', 'Items', 'KarlItems'), [])
	merge_models(os.path.join(repo(), 'base_mm', 'models', 'Items', 'KarlItems', 'lantern2', 'karl_item_lantern2'))


def run_amelia():
	convert(os.path.join(repo(), 'base_mm', 'models', 'Amelia'), 'amelia_body.xml')
	merge_models(os.path.join(repo(), 'base_mm', 'models', 'Amelia', 'amelia_skeleton'))

def run_karl():
	convert(os.path.join(repo(), 'base_mm', 'models', 'Karl'), 'karl_body.xml')
	convert(os.path.join(repo(), 'base_mm', 'models', 'Karl'), 'karl_body_pyjama.xml')
	merge_models(os.path.join(repo(), 'base_mm', 'models', 'Karl', 'karl_skeleton'))

def run_cat():
	merge_models(os.path.join(repo(), 'base_mm', 'models', 'Cat', 'cat_04'))

def run_horse():
	convert(os.path.join(repo(), 'base_mm', 'models', 'Horse'), 'horse_body.xml')
	merge_models(os.path.join(repo(), 'base_mm', 'models', 'Horse', 'Horse_skeleton'))

#def run_car():
#	convert_folder(os.path.join(repo(), 'base_mm', 'models', 'car'))

def run_ship():
	convert_splitted(os.path.join(repo(), 'models', 'ship'), os.path.join(repo(), 'base_mm', 'models', 'ship', 'ship.bin'))

def run_father():
	convert_folder(os.path.join(repo(), 'base_mm', 'models', 'Father'))

def run_match3():
	convert_folder(os.path.join(repo(), 'base_mm', 'models', 'Match3'))

# def run_dog():
# 	exclude_convert(os.path.join(repo(), 'base_mm', 'models'), 'dog_04.xml')

# def run_ostin():
# 	convert_splitted(os.path.join(repo(), 'models', 'Ostin'), os.path.join(repo(), 'base_mm', 'models', 'Ostin', 'Ostin.bin'))

# def run_ostin_items():
# 	container = os.path.join(repo(), 'models', 'Ostin')
# 	for item in os.listdir(container):
# 		path = os.path.join(container, item)
# 		if os.path.isdir(path):
# 			convert_splitted(path, os.path.join(repo(), 'base_mm', 'models', 'Ostin', item + '.bin'))

def main(group):
	if not group or group == 'items':
		run_items()

	if not group or group == 'amelia_items':
		run_amelia_items()

	if not group or group == 'common_items':
		run_common_items()

	if not group or group == 'karl_items':
	 	run_karl_items()

	if not group or group == 'amelia':
		run_amelia()	

	if not group or group == 'karl':
		run_karl()

	if not group or group == 'cat':
		run_cat()

	if not group or group == 'horse':
		run_horse()
		
	# if not group or group == 'dog':
	# 	run_dog()

	# if not group or group == 'car':
	# 	run_car()

	if not group or group == 'ship':
		run_ship()

	if not group or group == 'father':
		run_father()

	if not group or group == 'match3':
		run_match3()

	# if not group or group == 'ostin':
	# 	run_ostin()

	# if not group or group == 'ostin_items':
	# 	run_ostin_items()

def pause():
	script.pause()

if __name__ == "__main__":
	main(sys.argv[1] if len(sys.argv) > 1 else '')
