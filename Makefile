activate:
	source .venv/bin/activate

install: activate
	pip install -r requirements.txt

dev:
	fastapi dev src/main.py

test:
	rm -rvf test.db
	ENV=TEST alembic downgrade base
	ENV=TEST alembic upgrade head
	ENV=TEST pytest

reset-db:
	rm -rvf data.db
	alembic downgrade base
	alembic upgrade head