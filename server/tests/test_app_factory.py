from pytest import fixture
from unittest.mock import patch

from lostinp import app_factory


@fixture
def mocked_flask():
    with patch("lostinp.Flask.run") as mock:
        yield mock


@fixture
def mocked_wsgi():
    with patch("lostinp.WSGIServer") as mock:
        mock.side_effect = None
        yield mock


def test_app_factory_in_development(mocked_flask):
    app = app_factory("dev")
    print("whaterver")
    app()
    mocked_flask.assert_called_once()


def test_app_factory_in_production(mocked_wsgi):
    app = app_factory("prod")
    app()
    mocked_wsgi.assert_called_once()
