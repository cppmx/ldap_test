# LDAP Test Project Make File
# author: Carlos Colón

VIRTUALENV = $(shell which virtualenv)

clean: shutdown
	rm -fr ldap_test.egg-info
	rm -fr venv

venv:
	$(VIRTUALENV) -p /usr/bin/python2.7 venv

install: clean venv
	. venv/bin/activate; python setup.py install
	. venv/bin/activate; python setup.py develop

launch: venv shutdown
	. venv/bin/activate; python run.py

shutdown:
#	ps -ef | grep "run.py" | grep -v grep | awk '{print $$2}' | xargs kill > /dev/null
