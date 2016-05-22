# Flask-Diamond (c) Ian Dennis Miller

SHELL=/bin/bash
MOD_NAME=flask_diamond

install:
	python setup.py install

requirements:
	pip install -r requirements.txt

clean:
	rm -rf build dist *.egg-info
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete

test:
	# create folder
	rm -rf build/test-app
	mkdir -p build/test-app

	# scaffold the app
	mrbob --config skels/test-app/.mrbob.ini -O build/test-app skels/flask-diamond-app
	cd build/test-app && make install test

	# views
	mrbob --config skels/test-app/.mrbob.ini -O build/test-app skels/example-views
	cd build/test-app && make install test

	# models
	mrbob --config skels/test-app/.mrbob.ini -O build/test-app skels/example-models
	cd build/test-app && make install test

docs:
	rm -rf build/sphinx
	SETTINGS=$$PWD/etc/conf/testing.conf sphinx-build -b html docs build/sphinx

release:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: install requirements clean test docs release
