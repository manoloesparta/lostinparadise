from pytest import fixture
from unittest.mock import patch

from lostinp import app_factory


@fixture
def mocked_flask():
    with patch("lostinp.Flask.run") as mock:
        yield mock


@fixture
def mocked_run():
    with patch("lostinp.run_simple") as mock:
        mock.side_effect = None
        yield mock


def test_app_factory_in_development(mocked_flask):
    app = app_factory("development")
    app()
    mocked_flask.assert_called_once()


def test_app_factory_in_production(mocked_run):
    app = app_factory("production")
    app()
    mocked_run.assert_called_once()
