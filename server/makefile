PYTHON = venv/bin/python
PIP = venv/bin/pip

.PHONY: setup 
setup:
	virtualenv -p $(env) venv
	$(PIP) install --upgrade pip
	$(PIP) install -r requirements.txt

.PHONY: build
build:
	docker-compose build

.PHONY: dev
dev:
	docker-compose up

.PHONY: prod
prod:
	docker-compose --env-file ./prod.env up mongo server

.PHONY: load
load:
	docker-compose up -d mongo 
	$(PYTHON) scripts/load_data.py

.PHONY: wipe
wipe:
	docker-compose down
	sudo rm -rf database

.PHONY: tests 
tests:
	$(PYTHON) -m coverage run -m pytest tests --disable-pytest-warnings
	$(PYTHON) -m coverage report -i

.PHONY: format 
format:
	$(PYTHON) -m black . --exclude "(database|venv)"

.PHONY: clean 
clean:
	find . -name __pycache__ | xargs rm -rf
