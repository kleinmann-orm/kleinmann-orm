checkfiles = kleinmann/ examples/ tests/ conftest.py
py_warn = PYTHONDEVMODE=1
pytest_opts = -n auto --cov=kleinmann --cov-append --tb=native -q

help:
	@echo  "Kleinmann ORM development makefile"
	@echo
	@echo  "usage: make <target>"
	@echo  "Targets:"
	@echo  "    up      Updates dev/test dependencies"
	@echo  "    deps    Ensure dev/test dependencies are installed"
	@echo  "    check	Checks that build is sane"
	@echo  "    test	Runs all tests"
	@echo  "    docs 	Builds the documentation"
	@echo  "    style   Auto-formats the code"

up:
	@poetry update

deps:
	@poetry install -E asyncpg -E accel -E psycopg

check: deps build
ifneq ($(shell which black),)
	black --check $(checkfiles) || (echo "Please run 'make style' to auto-fix style issues" && false)
endif
	ruff check $(checkfiles)
	mypy $(checkfiles)
	#pylint -d C,W,R $(checkfiles)
	#bandit -r $(checkfiles)make
	twine check dist/*

lint: deps build
ifneq ($(shell which black),)
	black --check $(checkfiles) || (echo "Please run 'make style' to auto-fix style issues" && false)
endif
	ruff check $(checkfiles)
	mypy $(checkfiles)
	#pylint $(checkfiles)
	bandit -c pyproject.toml -r $(checkfiles)
	twine check dist/*

test: deps
	$(py_warn) KLEINMANN_TEST_DB=sqlite://:memory: pytest $(pytest_opts)

test_sqlite:
	$(py_warn) KLEINMANN_TEST_DB=sqlite://:memory: pytest --cov-report= $(pytest_opts)

test_postgres_asyncpg:
	python -V | grep PyPy || $(py_warn) KLEINMANN_TEST_DB="asyncpg://postgres:$(KLEINMANN_POSTGRES_PASS)@127.0.0.1:5432/test_\{\}" pytest $(pytest_opts) --cov-append --cov-report=

test_postgres_psycopg:
	python -V | grep PyPy || $(py_warn) KLEINMANN_TEST_DB="psycopg://postgres:$(KLEINMANN_POSTGRES_PASS)@127.0.0.1:5432/test_\{\}" pytest $(pytest_opts) --cov-append --cov-report=

_testall: test_sqlite test_postgres_asyncpg test_postgres_psycopg
	coverage report

testall: deps _testall

ci: check _testall

docs: deps
	rm -fR ./build
	sphinx-build -M html docs build

style: deps
	isort -src $(checkfiles)
	black $(checkfiles)

build: deps
	rm -fR dist/
	poetry build

publish: deps build
	twine upload dist/*

loc:
	@for path in "kleinmann" "examples" "tests"; do \
		find $$path -name "*.py" -print0 | xargs -0 wc -l | tail -n 1 | cut -d " " -f 2 | xargs echo $$path; \
	done
