# Internet Archive Collection Downloader
# Version 0.1
# By Mike Dank, adapted from code by Robin Camille Davis
# Usage: python ia-collection-dl.py $collectionName
# Where $collectionName is in http://archive.org/details/$collectionName

import sys
import internetarchive as ia

## Make sure the arguments are set
if len(sys.argv) < 2:
	print>>sys.stderr, "USAGE: " + sys.argv[0] + " $collectionName"
	sys.exit(1)

## Set/Print our collection name and search for it
collection_name = 'collection:'+sys.argv[1]
print "Attempting to download collection: " + sys.argv[1]
collection = ia.Search(collection_name)

## Really dirty total item count
## Cant use len() on Search object
current_item = 1
total_item = 0
for entry in collection:
	total_item = total_item + 1

## Go through all items of the collection and download
for entry in collection:
	item_id = entry['identifier']
	print 'Downloading ' + str(current_item) + "/" + str(total_item) + '\t' + item_id

	item = ia.Item(item_id)
	status = item.download()
	print '\t\t Download successful'
	current_item = current_item + 1
