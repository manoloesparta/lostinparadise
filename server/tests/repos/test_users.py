import mongomock
from pytest import fixture

from tests.helpers.mongo import insert_collection, empty_collection
from tests.repos.mocks.users import REGISTERED_USER, USERS_DICT_MOCK, UNREGISTERED_USER


@mongomock.patch(servers=(("mongo", 27017),))
@fixture
def mocked_repo():
    from lostinp.utils.dbhandler import MongoHandler
    from lostinp.repos.users import UsersRepo

    handler = MongoHandler()
    repo = UsersRepo(handler)

    insert_collection(handler, USERS_DICT_MOCK)
    yield repo
    empty_collection(handler)


def test_is_user_registered_with_unregistered_user(mocked_repo):
    response = mocked_repo.is_user_registered(UNREGISTERED_USER)
    assert not response


def test_is_user_registered_with_registered_user(mocked_repo):
    response = mocked_repo.is_user_registered(REGISTERED_USER)
    assert response


def test_register_user_with_non_existing_user(mocked_repo):
    mocked_repo.register_user(UNREGISTERED_USER)
    query = {"username": UNREGISTERED_USER.username}
    user = mocked_repo.db_handler.get_document(query)
    assert user.get("username") == UNREGISTERED_USER.username
    assert user.get("visitCount") == 0


def test_increment_visit_counter(mocked_repo):
    query = {"username": REGISTERED_USER.username}
    before = mocked_repo.db_handler.get_document(query)
    mocked_repo.increment_visit_counter(REGISTERED_USER)
    after = mocked_repo.db_handler.get_document(query)
    assert before["visitCount"] + 1 == after["visitCount"]
