import pytest
from app import create_app

from app.extensions import db
from app.blueprints import data


def test_cmd_create_db_exists(runner):
    result = runner.invoke(args=["data", "--help"])
    assert "create-db" in result.output


def test_cmd_clean_exists(runner):
    result = runner.invoke(args=["data", "--help"])
    assert "clean" in result.output


def test_cmd_import_posts(runner):
    result = runner.invoke(args=["data", "--help"])
    assert "import-posts" in result.output
