# miniverse

Used to test Dataverse GeoConnect functions, specifically the workflow and types of API calls that may be needed.

This project is solely for "proof of concept" and will expand to test how different types of files will interact with GeoConnect.

### Requirements

* Django 1.6
* python 2.6+ (tested with 2.7, but not 3.x)

### Run on dev server with [GeoConnect](https://github.com/IQSS/geoconnect)

Run on Port 8090

	python manage.py runserver 8090
	
### Simple functionality

Djanog admin file upload and a single page for linking to "GeoConnect" or viewing the type of metadata that a token can access.
	
![Miniverse screenshot](/miniverse/static/images/miniverse_screenshot.png?raw=true "File Listing")
