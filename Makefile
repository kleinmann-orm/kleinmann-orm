.PHONY: $(MAKECMDGOALS)
MAKEFLAGS += --no-print-directory
##
##  🚧 Kleinmann ORM developer tools
##
SOURCE=kleinmann tests examples conftest.py
py_warn = PYTHONDEVMODE=1
pytest_opts = -n auto --cov=kleinmann --cov-append --tb=native -q

help:           ## Show this help (default)
	@grep -Fh "##" $(MAKEFILE_LIST) | grep -Fv grep -F | sed -e 's/\\$$//' | sed -e 's/##//'

##

ci: all
all:            ## Run an entire CI pipeline
	make format lint test_all

format:         ## Format with all tools
	make black

lint:           ## Lint with all tools
	make ruff mypy

test:           ## Run tests
	$(py_warn) KLEINMANN_TEST_DB=sqlite://:memory: pytest $(pytest_opts)

test_sqlite:
	$(py_warn) KLEINMANN_TEST_DB=sqlite://:memory: pytest --cov-report= $(pytest_opts)

test_postgres:
	python -V | grep PyPy || $(py_warn) KLEINMANN_TEST_DB="asyncpg://postgres:$(KLEINMANN_POSTGRES_PASS)@127.0.0.1:5432/test_\{\}" pytest $(pytest_opts) --cov-append --cov-report=

test_all:       ## Run tests with all databases
	make test_sqlite test_postgres
	coverage report

##

black:          ## Format with black
	black ${SOURCE}

ruff:           ## Lint with ruff
	ruff check --fix --unsafe-fixes ${SOURCE}

mypy:           ## Lint with mypy
	mypy ${SOURCE}

##

install:        ## Install all dependencies
	poetry install -E accel

update:         ## Update all dependencies
	poetry update

docs:           ## Build the documentation
	make install
	rm -fR ./build
	sphinx-build -M html docs build

build:          ## Build and verify the package
	rm -fR dist/
	poetry build
	twine check dist/*

##

loc:
	@for path in $(SOURCE); do \
		find $$path -name "*.py" -print0 | xargs -0 wc -l | tail -n 1 | cut -d " " -f 2 | xargs echo $$path; \
	done
