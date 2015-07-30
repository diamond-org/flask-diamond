# Flask-Diamond (c) Ian Dennis Miller

SHELL=/bin/bash
PROJECT_NAME=Flask-Diamond
MOD_NAME=flask_diamond
TEST_CMD=SETTINGS=$$PWD/etc/conf/testing.conf nosetests -w $(MOD_NAME)

install:
	pip install -r requirements.txt
	python setup.py install

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`

server:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py runserver

shell:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py shell

watch:
	watchmedo shell-command -R -p "*.py" -c 'echo \\n\\n\\n\\nSTART; date; $(TEST_CMD) -c etc/nose/test-single.cfg; date' .

test:
	$(TEST_CMD) -c etc/nose/test.cfg

single:
	$(TEST_CMD) -c etc/nose/test-single.cfg

db:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py init_db
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py populate_db

upgradedb:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py db upgrade

migratedb:
	SETTINGS=$$PWD/etc/conf/dev.conf bin/manage.py db migrate

docs:
	rm -rf var/sphinx/build
	SETTINGS=$$PWD/etc/conf/dev.conf sphinx-build -b html etc/sphinx var/sphinx/build

notebook:
	SETTINGS=$$PWD/etc/conf/dev.conf cd var/ipython && ipython notebook

release:
	python setup.py sdist upload -r https://pypi.python.org/pypi

.PHONY: clean install test server watch notebook db single docs shell upgradedb migratedb release
