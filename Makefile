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
	bin/test-skel.sh

docs:
	rm -rf var/sphinx/build
	SETTINGS=$$PWD/etc/conf/dev.conf sphinx-build -b html docs var/sphinx/build

release:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: install requirements clean test docs release
