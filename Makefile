VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3

run: install
	$(PYTHON) src/bot.py

install: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	
clean:
	rm -rf src/__pycache__
	rm -rf $(VENV)
