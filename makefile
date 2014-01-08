.PHONY: python-setup

setup: python-setup

python-setup: python/_virtualenv
	python/_virtualenv/bin/pip install -r python/requirements.txt

python/_virtualenv:
	virtualenv python/_virtualenv
	python/_virtualenv/bin/pip install --upgrade setuptools
	python/_virtualenv/bin/pip install --upgrade pip
