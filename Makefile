# Flask-Diamond (c) Ian Dennis Miller

SHELL=/bin/bash
MOD_NAME=flask_diamond
WATCHMEDO_PATH=$$(which watchmedo)
NOSETESTS_PATH=$$(which nosetests)
TEST_CMD=SETTINGS=$$PWD/etc/conf/testing.conf $(NOSETESTS_PATH) $(MOD_NAME)

install:
	python setup.py install

requirements:
	pip install -r requirements.txt

clean:
	rm -rf build dist *.egg-info
	find . -name '*.pyc' -delete
	find . -name __pycache__ -delete

test: test-all test-scaffold
	@echo "OK"

test-all:
	$(TEST_CMD) -c etc/nose/test-all.cfg

single:
	$(TEST_CMD) -c etc/nose/test-single.cfg 2>&1

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
	SETTINGS=$$PWD/etc/conf/testing.conf sphinx-build -b html docs build/sphinx

release:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: install requirements clean test docs release
