# miniverse

Used to test dataverse GeoConnect functions.

This purpose is proof-of-concept testing for building a connection between the Dataverse and WorldMap.

Includes a "Map It" button that sends a fake token associated with a particular file,

### Requirements

* Django 1.6
* python 2.6+ (tested with 2.7, but not 3.x)

### Run on dev server with [GeoConnect](https://github.com/IQSS/geoconnect)

Run on Port 8090

	python manage.py runserver 8090
	
### Simple function

Admin file upload and single page for linking to "GeoConnect" or viewing the type of metadata that a token can access.
	
![Miniverse screenshot](miniverse/miniverse/static/images/miniverse_screenshot.png?raw=true "File Listing")
