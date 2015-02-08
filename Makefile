# Flask-Diamond (c) Ian Dennis Miller

SHELL=/bin/bash
PROJECT_NAME=Flask-Diamond
MOD_NAME=flask_diamond
TEST_CMD=SETTINGS=$$PWD/etc/testing.conf nosetests -w $(MOD_NAME)

install:
	python setup.py install

clean:
	rm -rf build dist *.egg-info
	-rm `find . -name "*.pyc"`

server:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py runserver

shell:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py shell

watch:
	watchmedo shell-command -R -p "*.py" -c 'echo \\n\\n\\n\\nSTART; date; $(TEST_CMD) -c etc/nose/test-single.cfg; date' .

test:
	$(TEST_CMD) -c etc/nose/test.cfg

single:
	$(TEST_CMD) -c etc/nose/test-single.cfg

db:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py init_db
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py populate_db

upgradedb:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py db upgrade

migratedb:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py db migrate

docs:
	rm -rf docs/api etc/sphinx/api var/sphinx/api
	mkdir -p var/sphinx/api/$(MOD_NAME)
	sphinx-apidoc -o var/sphinx/api/$(MOD_NAME) $(MOD_NAME)
	ln -s $$PWD/var/sphinx/api etc/sphinx/api
	SETTINGS=$$PWD/etc/dev.conf sphinx-build -b html etc/sphinx var/sphinx/build
	mv var/sphinx/build docs/api
	rm -rf etc/sphinx/api var/sphinx/api

notebook:
	SETTINGS=$$PWD/etc/dev.conf cd var/ipython && ipython notebook

gh-pages: docs
	rm -rf /tmp/gh-pages
	git clone -b gh-pages git@github.com:iandennismiller/flask-diamond.git /tmp/gh-pages
	cp -r docs/api /tmp/gh-pages
	cd /tmp/gh-pages
	git add -A
	git commit -am "autosync documentation"
	git push -u origin gh-pages

.PHONY: clean install test server watch notebook db single docs shell upgradedb migratedb gh-pages
