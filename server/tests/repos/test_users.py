import mongomock
from pytest import fixture

from tests.helpers.mongo import insert_collection, empty_collection
from tests.repos.mocks.users import USERS_DICT_MOCK, UNREGISTERED_USER


def test_first_time_login_with_unregistered_user():
    pass


def test_first_time_login_with_registered_user():
    pass


def test_register_user_with_non_existing_user():
    pass


def test_increment_visit_counter():
    pass
