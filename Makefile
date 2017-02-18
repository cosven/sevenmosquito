.PHONY: docs

all: lint

clean:
	find . -name "*.pyc" -exec rm -f {} \;

lint:
	flake8 --ignore=E501 semo blog

test:
	./manage.py test blog

docs:
	cd docs && make html
