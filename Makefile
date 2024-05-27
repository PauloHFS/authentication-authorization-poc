activate:
	source .venv/bin/activate

install: activate
	pip install -r requirements.txt

dev:
	fastapi dev src/main.py

test:
	ENV=TEST alembic downgrade base
	ENV=TEST alembic upgrade head
	ENV=TEST pytest

reset-db:
	alembic downgrade base
	alembic upgrade head