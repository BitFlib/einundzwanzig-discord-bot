VENV = .venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip3

run: $(VENV)/bin/activate
	$(PYTHON) src/bot.py

$(VENV)/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt
	
clean:
	rm -rf src/__pycache__
	rm -rf $(VENV)
