PYTHON = venv/bin/python
PIP = venv/bin/pip

.PHONY: setup 
setup:
	virtualenv -p $(env) venv
	$(PIP) install -r requirements.txt

.PHONY:
start:
	$(PYTHON) start.py

.PHONY: tests 
tests:
	$(PYTHON) -m coverage run -m pytest tests
	$(PYTHON) -m coverage report -m

.PHONY: format 
format:
	$(PYTHON) -m black . --exclude "(data|venv)"

.PHONY: clean 
clean:
	find . -name __pycache__ | xargs rm -rf
