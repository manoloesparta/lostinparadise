import mongomock
from pytest import fixture, raises

from tests.helpers.mongo import empty_collection, insert_collection
from lostinp.utils.exceptions import DuplicateException, NotFoundException
from tests.utils.mocks.dbhandler import (
    DATA_MOCK,
    EXISTING_DATA_MOCK,
    NON_EXISTING_DATA_MOCK,
    NON_EXISTING_QUERY_FILTER_MOCK,
    QUERY_FILTER_MOCK,
    UPDATE_DATA_MOCK,
    QUERY_FILTER_UPDATED_DATA_MOCK,
)


@fixture
def mocked_mongo():
    with mongomock.patch(servers=(("mongo", 27017),)):
        from lostinp.utils.dbhandler import DbHandler

        handler = DbHandler("random_collection")
        insert_collection(handler, DATA_MOCK)
        yield handler
        empty_collection(handler)


def test_get_existing_doc(mocked_mongo):
    response = mocked_mongo.get_document(EXISTING_DATA_MOCK)
    assert response["username"] == EXISTING_DATA_MOCK["username"]
    assert response["password"] == EXISTING_DATA_MOCK["password"]


def test_get_non_existing_doc(mocked_mongo):
    with raises(NotFoundException):
        mocked_mongo.get_document(NON_EXISTING_DATA_MOCK)


def test_insert_existing_doc(mocked_mongo):
    with raises(DuplicateException):
        mocked_mongo.insert_document(EXISTING_DATA_MOCK)


def test_insert_non_existing_doc(mocked_mongo):
    mocked_mongo.insert_document(NON_EXISTING_DATA_MOCK.copy())
    response = mocked_mongo.get_document(NON_EXISTING_DATA_MOCK)
    assert response["username"] == NON_EXISTING_DATA_MOCK["username"]
    assert response["password"] == NON_EXISTING_DATA_MOCK["password"]


def test_update_existing_doc(mocked_mongo):
    mocked_mongo.update_document(QUERY_FILTER_MOCK, UPDATE_DATA_MOCK)
    response = mocked_mongo.get_document(QUERY_FILTER_UPDATED_DATA_MOCK)
    assert response["username"] == UPDATE_DATA_MOCK["username"]
    assert response["password"] == UPDATE_DATA_MOCK["password"]


def test_update_non_existing_doc(mocked_mongo):
    with raises(NotFoundException):
        mocked_mongo.update_document(NON_EXISTING_QUERY_FILTER_MOCK, EXISTING_DATA_MOCK)


def test_upsert_existing_doc(mocked_mongo):
    mocked_mongo.upsert_document(QUERY_FILTER_MOCK, UPDATE_DATA_MOCK)
    response = mocked_mongo.get_document(QUERY_FILTER_UPDATED_DATA_MOCK)
    assert response["username"] == UPDATE_DATA_MOCK["username"]
    assert response["password"] == UPDATE_DATA_MOCK["password"]


def test_upsert_non_existing_doc(mocked_mongo):
    mocked_mongo.upsert_document(NON_EXISTING_QUERY_FILTER_MOCK, UPDATE_DATA_MOCK)
    response = mocked_mongo.get_document(QUERY_FILTER_UPDATED_DATA_MOCK)
    assert response["username"] == UPDATE_DATA_MOCK["username"]
    assert response["password"] == UPDATE_DATA_MOCK["password"]


def test_delete_existing_doc(mocked_mongo):
    mocked_mongo.delete_document(QUERY_FILTER_MOCK)
    with raises(NotFoundException):
        mocked_mongo.get_document(QUERY_FILTER_MOCK)


def test_delete_non_existing_doc(mocked_mongo):
    with raises(NotFoundException):
        mocked_mongo.delete_document(NON_EXISTING_QUERY_FILTER_MOCK)
