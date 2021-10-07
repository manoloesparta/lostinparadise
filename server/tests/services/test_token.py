from pytest import fixture, raises
from unittest.mock import patch

from lostinp.services.token import JwtService
from lostinp.utils.exceptions import InvalidToken, ClaimNotFound
from tests.services.mocks.token import (
    SECRET,
    USERNAME,
    TOKEN_WITHOUT_USERNAME,
    EXPIRED_TOKEN,
)


@fixture
def jwt_service():
    yield JwtService(SECRET)


def test_create_user_token(jwt_service):
    token = jwt_service.create_user_token(USERNAME)
    username = jwt_service.get_username_claim(token)
    assert username == USERNAME


def test_get_username_claim_expired(jwt_service):
    with raises(InvalidToken):
        jwt_service.get_username_claim(EXPIRED_TOKEN)


def test_get_username_wiht_no_claim(jwt_service):
    with raises(ClaimNotFound):
        jwt_service.get_username_claim(TOKEN_WITHOUT_USERNAME)
