# Internet Archive Collection Downloader
# Version 0.1
# By Mike Dank, adapted from code by Robin Camille Davis
# Usage: python ia-collection-dl.py $collectionName
# Where $collectionName is in http://archive.org/details/$collectionName

import sys
import internetarchive as ia


def get_name():
	## Make sure the arguments are set
	if len(sys.argv) < 2:
		sys.stderr.write("USAGE: " + sys.argv[0] + " <collectionName>\n")
		sys.exit(1)
	## Set/Print our collection name and search for it
	return 'collection:'+sys.argv[1]

def other(target):
	print("Attempting to download collection: " + target)
	search = ia.Search(target)

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
		print('Downloading ' + str(current_item) + "/" + str(total_item) + '\t' + item_id)

		item = ia.Item(item_id)
		status = item.download()
		print('\t\t Download successful')
		current_item += 1


def main():
	name = get_name()

if __name__ == '__main__':
	main()