# Makefile for ML project tasks

run:
	python train.py

lint:
	ruff check .

test:
	pytest tests/

clean:
	find . -type f -name "*.pyc" -delete
	rm -rf __pycache__ models/* outputs/* logs/*

venv:
	python -m venv .venv && source .venv/bin/activate && pip install -r requirements.txt

freeze:
	pip freeze > requirements.txt

pipreqs:
	pipreqs ./ --force