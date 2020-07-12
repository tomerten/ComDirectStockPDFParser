project := ComDirectStockPDFParser
pytest := pipenv run pytest
test_args :=--cov --cov-report term-missing

.PHONY: docs requirements tests clean
.DEFAULT_GOAL : help

help:
	@echo "requirements - run piptools compile to generate requirement files"
	@echo "docs - generate Shinx HTML documentation and open it"
	@echo "tests - run pipenv tests and coverage"

requirements:
	@if [[ ! -f requirements.txt ]]; then \
		touch requirements.txt; \
	fi
	python3 -m piptools compile --output-file requirements.tmp requirements.in  && \
		cat requirements.tmp > requirements.txt

	@if [[ ! -f dev-requirements.txt ]]; then \
		touch dev-requirements.txt; \
	fi
	python3 -m piptools compile --output-file dev-requirements.tmp dev-requirements.in  && \
		cat dev-requirements.tmp > dev-requirements.txt
	pipenv install -r requirements.txt
	pipenv install -r dev-requirements.txt --dev
	git init
	pipenv run pre-commit install -t pre-commit
	pipenv run pre-commit install -t pre-push

tests:
	$(pytest) $(test_args)

docs:
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	xdg-open docs/build/html/index.html

clean: clean-test clean-pyc

clean-test:
	rm -f .coverage

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

install-dev:
	pip install -e .

install:
	pip install .