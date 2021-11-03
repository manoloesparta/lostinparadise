from pytest import fixture, raises

from lostinp.utils.jwt_helper import JwtHelper
from lostinp.utils.exceptions import InvalidToken, ClaimNotFound
from tests.services.mocks.token import (
    SECRET,
    USERNAME,
    TOKEN_WITHOUT_USERNAME,
    EXPIRED_TOKEN,
)


@fixture
def jwt_service():
    yield JwtHelper(SECRET)


def test_create_user_token(jwt_service):
    token = jwt_service.create_user_token(USERNAME)
    username = jwt_service.get_claim(token, "username")
    assert username == USERNAME


def test_get_username_claim_expired(jwt_service):
    with raises(InvalidToken):
        jwt_service.get_claim(EXPIRED_TOKEN, "username")


def test_get_username_wiht_no_claim(jwt_service):
    with raises(ClaimNotFound):
        jwt_service.get_claim(TOKEN_WITHOUT_USERNAME, "username")
