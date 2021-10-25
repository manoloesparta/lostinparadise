import mongomock
from pytest import fixture
from unittest.mock import patch
from sanic_testing import TestManager

from tests.helpers.mongo import insert_collection, empty_collection
from tests.routes.mocks.search import (
    REGISTERED_USER,
    VALID_REQUEST,
    INVALID_REQUEST,
    LOST_ITEMS_MOCK,
)


@mongomock.patch(servers=(("mongo", 27017),))
@fixture
def mocked_app():
    from sanic import Sanic
    from lostinp.routes.items import bp as search_items_blueprint
    from lostinp.models.user import User
    from lostinp.utils.db_handler import MongoHandler
    from lostinp.repos.users import UsersRepo

    handler = MongoHandler()
    repo = UsersRepo(handler)
    repo.register_user(User(REGISTERED_USER))

    handler.set_collection("lost_items")
    insert_collection(handler, LOST_ITEMS_MOCK)

    app = Sanic("test_search_items")
    app.blueprint(search_items_blueprint)

    test = TestManager(app)
    client = test.test_client
    yield client
    empty_collection(handler)


def test_succesfully_get_lost_items(mocked_app):
    _, response = mocked_app.post(
        "/search",
        headers=VALID_REQUEST["headers"],
        json=VALID_REQUEST["body"],
    )
    assert response.status == 200


def test_failed_get_lost_items(mocked_app):
    _, response = mocked_app.post(
        "/search",
        headers=VALID_REQUEST["headers"],
        json=INVALID_REQUEST["body"],
    )
    assert response.status == 400


@patch("lostinp.routes.items.GetLostItemsController.do_it", side_effect=Exception())
def test_internal_server_error(controller, mocked_app):
    _, response = mocked_app.post(
        "/search",
        headers=VALID_REQUEST["headers"],
        json=VALID_REQUEST["body"],
    )
    assert response.status == 500
