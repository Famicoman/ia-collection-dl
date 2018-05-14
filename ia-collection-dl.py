# Internet Archive Collection Downloader
# Version 0.1
# By Mike Dank, adapted from code by Robin Camille Davis
# Usage: python ia-collection-dl.py $collectionName
# Where $collectionName is in http://archive.org/details/$collectionName

import sys
import os
import internetarchive as ia

from internetarchive import ArchiveSession

def get_name():
	'''Get the name of the mirror to make from argv'''
	if len(sys.argv) < 2:
		sys.stderr.write("USAGE: " + sys.argv[0] + " <collectionName>\n")
		sys.exit(1)
	## Set/Print our collection name and search for it
	return sys.argv[1]

def mkcd(target):
	'''If target mirror doesn't exist, mkdir and change into it.'''
	if os.path.exists(os.path.join(os.getcwd(), target)):
		print("Path: "+os.path.join(os.getcwd(), target)+" exists, EXITING!")
	else:
		os.makedirs(os.path.join(os.getcwd(), target))
		os.chdir(os.path.join(os.getcwd(), target))

def mk_mirror(target):
	'''Make the mirror'''
	session = ArchiveSession()
	target = 'collection:' + target
	print("Attempting to download collection: " + target)
	search = ia.Search(session, target)

	## Because the internetarchive module won't return us a list
	## we'll have to make our own.
	current_item = 1
	total_item = 0
	collection = []
	for entry in search:
		collection.append(entry)
		total_item += 1

	## Go through all items of the collection and download
	for entry in collection:
		item_id = entry['identifier']
		print('Downloading ' + str(current_item) + '/' + str(total_item) + '\t'\
			+ item_id)

		item = ia.Item(session, item_id)
		status = item.download()
		print('\t\t Download successful')
		current_item += 1


def main():
	# Get mirror name
	name = get_name()
	# change into this directiory
	mkcd(name)
	# make the mirror
	mk_mirror(name)

if __name__ == '__main__':
	main()