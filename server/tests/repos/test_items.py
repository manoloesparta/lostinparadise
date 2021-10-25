import mongomock
from pytest import fixture

from tests.helpers.mongo import insert_collection, empty_collection
from tests.repos.mocks.items import LOST_ITEMS_MOCK


@mongomock.patch(servers=(("mongo", 27017),))
@fixture
def mocked_repo():
    from lostinp.repos.items import LostItemsRepo
    from lostinp.utils.db_handler import MongoHandler

    handler = MongoHandler()
    repo = LostItemsRepo(handler)

    insert_collection(handler, LOST_ITEMS_MOCK)
    yield repo
    empty_collection(handler)


def test_get_lost_items(mocked_repo):
    result = mocked_repo.get_lost_items_by_query("computo")
    assert len(result) == 2

    result = mocked_repo.get_lost_items_by_query("cargador")
    assert len(result) == 12

    result = mocked_repo.get_lost_items_by_query("iphone")
    assert len(result) == 4

    result = mocked_repo.get_lost_items_by_query("no existe esto")
    assert len(result) == 0
