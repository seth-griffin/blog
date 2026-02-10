Overview
=====================
A simple blogging application built with Python and Flask using MySQL/Maria as a backend

Quick Start
=====================

```
touch .env
vim .env
```

Add the following settings to .env

```
PYTHONDONTWRITEBYTECODE=1
DB_URN='mysql+mysqlconnector://{}:{}@{}/{}'
DB_USER=dev
DB_PASS=
DB_IP=localhost
DB_NAME=blog
```

Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies

```
python3 -m pip install
```

Note:

When finished deactivate your venv with:

```
deactivate
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
