activate:
	source .venv/bin/activate

install: activate
	pip install -r requirements.txt

dev:
	fastapi dev src/main.py

test:
	rm -rv test.db
	pytest