ia-collection-dl
================

Downloads an entire Internet Archive collection

Based off of download-all-items-in-IA-collection.py by Robin Camille Davis

Visit http://programminghistorian.org/lessons/data-mining-the-internet-archive for the original version

**Written in python with the internetarchive module (tested with v 0.6.1)**

Visit https://pypi.python.org/pypi/internetarchive for more information

## Before You Run

Download the internetarchive module

	pip install internetarchive

## Quickstart Example

Find a collection identifier from the collection URL

	https://archive.org/details/omni-magazine

The identifier here is **omni-magazine**

Run ia-collection-downloader with the identifier

	$ python ia-collection-dl.py omni-collection

Your items will download into the current directory
