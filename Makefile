# Flask-Diamond (c) Ian Dennis Miller

SHELL=/bin/bash
MOD_NAME=flask_diamond

install:
	python setup.py install

requirements:
ifeq ($(OS),Windows_NT)
	easy_install -U mr.bob==0.1.2
endif
	pip install -r requirements.txt

develop:
	pip install -r .requirements-dev.txt

clean:
	rm -rf build dist *.egg-info
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete

test: test-all test-scaffold
	@echo "OK"

test-all:
	SETTINGS=$$PWD/$(MOD_NAME)/tests/testing.conf nosetests $(MOD_NAME) -c etc/nose/test-all.cfg

single:
	SETTINGS=$$PWD/$(MOD_NAME)/tests/testing.conf nosetests $(MOD_NAME) -c etc/nose/test-single.cfg 2>&1

test-scaffold:
	# create folder
	rm -rf build/test-app
	mkdir -p build/test-app

	# scaffold the app
	mrbob --config flask_diamond/tests/mrbob.ini -O build/test-app flask_diamond/skels/app
	cd build/test-app && make install test

	# planets tutorial
	mrbob --config flask_diamond/tests/mrbob.ini -O build/test-app flask_diamond/skels/tutorial-planets
	cd build/test-app && make install test

docs:
	rm -rf build/sphinx
	SETTINGS=$$PWD/$(MOD_NAME)/tests/testing.conf sphinx-build -b html docs build/sphinx

release:
	python setup.py sdist upload

.PHONY: install requirements clean test docs release develop
