# authentication-authorization-poc

Proof of concept to test how to work with Authentication and Authorizantion on a Web Server

Things to learn:

- RBAC (Role Based Access Control)
- ABAC (Attribute Based Access Control)

## Technologies

- Python
- FastAPI
- SQLAlchemy
- Alembic
- SQLite

[Follow this guidelines](https://github.com/zhanymkanov/fastapi-best-practices)

## Checkpoints

- [ ] create a authentication flow
  - [ ] sign-up endpoint
  - [ ] sign-in endpoint
  - [ ] implements a JWT token
  - [ ] implements a refresh token
  - [ ] handle the sessions on the server
  - [ ] set the cookies on the client
  - [ ] use redis to store the refresh tokens
- [ ] create a authorization flow
  - [ ] create a middleware to check if the user is authorized
  - [ ] create a autorization flow (roles and permissions)

## How to run

### Requirements

- virtualenv
- python3
- pip3

### Steps

1. Clone the repository
2. Create a virtualenv
3. Install the requirements
4. Run the server

### Alembic Commands

- Display the current revision for a database: `alembic current`.
- View migrations history: `alembic history --verbose`.
- Create a new migration: `alembic revision --autogenerate -m "migration name"`.
- Revert all migrations: `alembic downgrade base`.
- Revert migrations one by one: `alembic downgrade -1`.
- Apply all migrations: `alembic upgrade head`.
- Apply migrations one by one: `alembic upgrade +1`.
- Display all raw SQL: `alembic upgrade head --sql`.
- Reset the database: `alembic downgrade base && alembic upgrade head`.
