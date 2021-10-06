from unittest import mock
import mongomock
from pytest import fixture, raises

from tests.helpers.mongo import insert_collection, empty_collection
from tests.repos.mocks.users import REGISTERED_USER, USERS_DICT_MOCK, UNREGISTERED_USER


@fixture()
def mocked_repo():
    with mongomock.patch(servers=(("mongo", 27017),)):
        from lostinp.utils.dbhandler import DbHandler
        from lostinp.repos.users import UsersRepo

        handler = DbHandler()
        handler.set_collection(UsersRepo.collection_name)
        insert_collection(handler, USERS_DICT_MOCK)
        yield UsersRepo(handler)
        empty_collection(handler)


def test_first_time_login_with_unregistered_user(mocked_repo):
    response = mocked_repo.first_time_login(UNREGISTERED_USER)
    assert response 

def test_first_time_login_with_registered_user(mocked_repo):
    response = mocked_repo.first_time_login(REGISTERED_USER)
    assert not response 


def test_register_user_with_non_existing_user(mocked_repo):
    mocked_repo.register_user(UNREGISTERED_USER) 
    query = { "username": UNREGISTERED_USER.username }
    user = mocked_repo.db_handler.get_document(query)
    assert user.get("username") == UNREGISTERED_USER.username
    assert user.get("visitCount") == 0


def test_increment_visit_counter(mocked_repo):
    query = {"username": REGISTERED_USER.username}
    before = mocked_repo.db_handler.get_document(query)
    mocked_repo.increment_visit_counter(REGISTERED_USER)
    after = mocked_repo.db_handler.get_document(query)
    assert before["visitCount"] + 1 == after["visitCount"]
