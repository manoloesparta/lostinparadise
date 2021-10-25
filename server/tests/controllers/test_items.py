import mongomock
from pytest import fixture, raises

from lostinp.utils.exceptions import BadRequest

from tests.helpers.mongo import insert_collection, empty_collection
from tests.controllers.mocks.items import (
    LOST_ITEMS_MOCK,
    VALID_REQUEST,
    INVALID_REQUEST,
)


@mongomock.patch(servers=(("mongo", 27107),))
@fixture
def mocked_controller():
    from lostinp.repos.items import LostItemsRepo
    from lostinp.utils.db_handler import MongoHandler
    from lostinp.controllers.items import GetLostItemsController

    handler = MongoHandler()
    repo = LostItemsRepo(handler)
    controller = GetLostItemsController(repo)

    insert_collection(handler, LOST_ITEMS_MOCK)
    yield controller
    empty_collection(handler)


def test_successfully_get_lost_items(mocked_controller):
    result = mocked_controller.do_it(VALID_REQUEST)
    print(result)
    assert len(result) == 12


def test_bad_request_when_items_requested(mocked_controller):
    with raises(BadRequest):
        mocked_controller.do_it(INVALID_REQUEST)
