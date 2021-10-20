import mongomock
from pytest import fixture

from tests.utils.mocks.decorators import (
    USERS_REGISTERED,
    VALID_HEADERS,
    NOT_REGISTERED_HEADERS,
    INVALID_TOKEN_HEADERS,
)


@mongomock.patch(servers=(("mongo", 27017),))
@fixture
def decorator_mocked():
    from lostinp.utils.db_handler import MongoHandler
    from lostinp.repos.users import UsersRepo
    from lostinp.models.user import User
    from lostinp.utils.decorators import user_must_be_registered

    handler = MongoHandler()
    repo = UsersRepo(handler)
    [repo.register_user(User(user)) for user in USERS_REGISTERED]

    yield user_must_be_registered


def test_valid_request(decorator_mocked):
    @decorator_mocked(VALID_HEADERS)
    def inner():
        return True

    response = inner()
    assert response == True


def test_non_registered_user(decorator_mocked):
    @decorator_mocked(NOT_REGISTERED_HEADERS)
    def decorated():
        return True

    response = decorated()
    assert response.get("status") == 400


def test_invalid_token(decorator_mocked):
    @decorator_mocked(INVALID_TOKEN_HEADERS)
    def decorated():
        return True

    response = decorated()
    assert response.get("status") == 400
