import mongomock
from pytest import fixture, raises

from lostinp.utils.exceptions import BadRequest, Unauthorized
from tests.helpers.mongo import insert_collection, empty_collection
from tests.controllers.mocks.login import (
    USERS_REGISTERED,
    NON_EXISTING_CRENDENTIALS,
    EXISTING_USER,
    NON_EXISTING_USER,
    QUERY_EXISTING_USER,
    INVALID_REQUEST,
    VALID_REQUEST,
)


@mongomock.patch(servers=(("mongo", 27017),))
@fixture
def mocked_controller():
    from lostinp.utils.db_handler import MongoHandler
    from lostinp.repos.users import UsersRepo
    from lostinp.services.authentication import MockedAuthService
    from lostinp.utils.jwt_helper import JwtHelper
    from lostinp.controllers.login import LoginController

    handler = MongoHandler()
    repo = UsersRepo(handler)
    token = JwtHelper()
    auth = MockedAuthService()

    controller = LoginController(auth, token, repo)

    insert_collection(handler, USERS_REGISTERED)
    yield controller
    empty_collection(handler)


def test_user_does_not_exist(mocked_controller):
    with raises(Unauthorized):
        mocked_controller._verify_user_exists(**NON_EXISTING_CRENDENTIALS)


def test_register_user(mocked_controller):
    mocked_controller._register_or_increment_count(NON_EXISTING_USER.username)
    assert mocked_controller.user_repo.is_user_registered(NON_EXISTING_USER)


def test_increment_count_user(mocked_controller):
    pre = mocked_controller.user_repo.db_handler.get_document(QUERY_EXISTING_USER)
    mocked_controller._register_or_increment_count(EXISTING_USER.username)
    pos = mocked_controller.user_repo.db_handler.get_document(QUERY_EXISTING_USER)
    assert pre.get("visitCount") + 1 == pos.get("visitCount")


def test_check_invalid_request(mocked_controller):
    with raises(BadRequest):
        mocked_controller._check(INVALID_REQUEST)


def test_check_valid_request(mocked_controller):
    username, password = mocked_controller._check(VALID_REQUEST)
    assert username == VALID_REQUEST["username"]
    assert password == VALID_REQUEST["password"]


def test_return_token_with_username_claim(mocked_controller):
    token = mocked_controller.do_it(VALID_REQUEST)
    username = mocked_controller.jwt_helper.get_claim(token, "username")
    assert username == VALID_REQUEST["username"]
