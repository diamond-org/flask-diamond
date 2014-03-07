# Ian Dennis Miller
# http://www.iandennismiller.com

SHELL=/bin/bash
PROJECT_NAME=flask-diamond
MOD_NAME=FlaskDiamond
WWWROOT=/var/www/$(PROJECT_NAME)
TEST_CMD=SETTINGS=$$PWD/etc/testing.conf nosetests -c tests/nose/test.cfg
TEST_SINGLE=SETTINGS=$$PWD/etc/testing.conf nosetests -c tests/nose/test-single.cfg

clean:
	rm -rf build dist *.egg-info
	rm -rf docs/source/auto docs/build
	-rm `find . -name "*.pyc"`

install:
	python setup.py install
	rsync -a $(MOD_NAME)/Views/static $(WWWROOT)

server:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py runserver

shell:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py shell

watch:
	watchmedo shell-command -R -p "*.py" -c 'echo \\n\\n\\n\\nSTART; date; $(TEST_SINGLE); date' .

test:
	$(TEST_CMD)

single:
	$(TEST_SINGLE)

db:
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py init_db
	SETTINGS=$$PWD/etc/dev.conf bin/manage.py populate_db

dep:
	mkdir -p lib
	cd lib && git clone https://github.com/mrjoes/flask-admin.git
	cd lib/flask-admin && python setup.py install

doc:
	rm -rf docs/source/auto
	mkdir -p docs/source/auto/$(MOD_NAME)
	sphinx-apidoc -o docs/source/auto/$(MOD_NAME) $(MOD_NAME)
	SETTINGS=$$PWD/etc/dev.conf sphinx-build -b html docs/source docs/build
	open docs/build/index.html

notebook:
	SETTINGS=$$PWD/etc/dev.conf cd var/ipython && ipython notebook

.PHONY: clean install test server watch notebook db dep single doc shell
