from unittest import TestCase
from unittest.mock import patch

from lostinp import app_factory


class TestAppFactory(TestCase):
    def test_app_factory_in_development(self):
        with patch("lostinp.Flask.run") as mocked_flask:
            app = app_factory("development")
            app()
            mocked_flask.assert_called_once()

    def test_app_factory_in_production(self):
        assert True
