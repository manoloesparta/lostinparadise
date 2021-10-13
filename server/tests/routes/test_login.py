import json
from sys import prefix
import mongomock
from pytest import fixture
from flask import Flask

from tests.routes.mocks.login import VALID_REQUEST, HEADERS
from tests.helpers.jwt import get_claim_from_jwt

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
    assert parsed.get("statusCode") == 201

    token = parsed.get("message", {}).get("X-Jwt-Key")
    username = get_claim_from_jwt(token, "username")
    assert username == VALID_REQUEST["username"]


def test_handler_bad_request(mocked_login_route):
    pass


def test_handler_unauthorized(mocked_login_route):
    pass


def test_handler_internal_server_error(mocked_login_route):
    pass
