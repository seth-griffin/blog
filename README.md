Overview
=====================
A simple blogging application built with Python and Flask using MySQL/Maria as a backend

Quick Start
=====================

## Create .env config

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

## Create a virtual environment

```
python3 -m venv .venv
source .venv/bin/activate
```

## Install dependencies

```
python3 -m pip install
```

## Initialize the database backend

```
flask data clean # Optional when making data structure changes or content updates
flask data create-db
flask data import-posts
flask run --debug --port 5001
```

## Run black prior to committing to tidy your code:

```
black .
```

# Deactivate venv

```
deactivate
```
