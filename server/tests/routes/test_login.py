import mongomock
from pytest import fixture
from unittest.mock import patch
from sanic_testing import TestManager

from lostinp.services.authentication import MockedAuthService

from tests.routes.mocks.login import (
    INCOMPLETE_REQUEST,
    INVALID_USER_REQUEST,
    VALID_REQUEST,
)


@mongomock.patch(servers=(("mongo", 27017),))
@fixture
def mocked_app():
    from sanic import Sanic
    from lostinp.routes.login import bp as login_blueprint

    app = Sanic("test_login_route")
    app.blueprint(login_blueprint)

    test = TestManager(app)
    client = test.test_client
    return client


@patch("lostinp.routes.login.CetysAuthentication", MockedAuthService)
def test_create_token_succesfully(mocked_app):
    _, response = mocked_app.post("/login", json=VALID_REQUEST)
    assert response.status == 201


@patch("lostinp.routes.login.CetysAuthentication", MockedAuthService)
def test_handler_bad_request(mocked_app):
    _, response = mocked_app.post("/login", json=INCOMPLETE_REQUEST)
    assert response.status == 400


@patch("lostinp.routes.login.CetysAuthentication", MockedAuthService)
def test_handler_unauthorized(mocked_app):
    _, response = mocked_app.post("/login", json=INVALID_USER_REQUEST)
    assert response.status == 401


@patch("lostinp.routes.login.CetysAuthentication", MockedAuthService)
def test_handler_internal_server_error(mocked_app):
    _, response = mocked_app.post("/login")
    assert response.status == 500
