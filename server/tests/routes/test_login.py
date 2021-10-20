import mongomock
from unittest.mock import patch
from pytest import fixture

import json
from flask import Flask

from tests.helpers.jwt import get_claim_from_jwt
from tests.routes.mocks.login import (
    VALID_REQUEST,
    HEADERS,
    INVALID_USER_REQUEST,
    INCOMPLETE_REQUEST,
)

app = Flask(__name__)


@mongomock.patch(servers=(("mongo", 27017),))
@fixture
def mocked_login_route():
    from lostinp.routes.login import mod as login_module

    app.register_blueprint(login_module)

    yield app.test_client()


def test_create_token_succesfully(mocked_login_route):
    payload = json.dumps(VALID_REQUEST)
    response = mocked_login_route.post("/login", data=payload, headers=HEADERS)
    parsed = json.loads(response.data)
    assert parsed.get("status") == 201

    token = parsed.get("data", {}).get("X-Jwt-Key")
    username = get_claim_from_jwt(token, "username")
    assert username == VALID_REQUEST["username"]


def test_handler_bad_request(mocked_login_route):
    payload = json.dumps(INCOMPLETE_REQUEST)
    response = mocked_login_route.post("/login", data=payload, headers=HEADERS)
    parsed = json.loads(response.data)
    assert parsed.get("status") == 400


def test_handler_unauthorized(mocked_login_route):
    payload = json.dumps(INVALID_USER_REQUEST)
    response = mocked_login_route.post("/login", data=payload, headers=HEADERS)
    parsed = json.loads(response.data)
    assert parsed.get("status") == 401


@patch("lostinp.routes.login.LoginController.do_it", side_effect=Exception("Test"))
def test_handler_internal_server_error(do_it_mock, mocked_login_route):
    payload = json.dumps(VALID_REQUEST)
    response = mocked_login_route.post("/login", data=payload, headers=HEADERS)
    parsed = json.loads(response.data)
    assert parsed.get("status") == 500
