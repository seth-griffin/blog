Overview
=====================
A simple blogging application built with Python and Flask using MySQL/Maria as a backend

Quick Start
=====================
touch .env and then edit adding:

```
touch .env
vim .env
PYTHONDONTWRITEBYTECODE=1
DB_URN='mysql+mysqlconnector://{}:{}@{}/{}'
DB_USER=dev
DB_PASS=
DB_IP=localhost
DB_NAME=blog
```

```
source .venv/bin/activate
flask data create-db
flask data import-posts
flask run --debug --port 5001
```

Before checking in code run black formatter:

```
black .
```

If making database changes drop and recreate the database tables:

```
flask data clean
flask data create-db
flask data import-posts
```
