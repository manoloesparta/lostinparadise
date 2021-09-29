import mongomock
from unittest import TestCase
from lostinp.utils.dbhandler import DbHandler


@mongomock.patch
class TestDbHandler(TestCase):
    def setUp(self):
        pass

    def test_get(self):
        pass

    def test_insert(self):
        pass

    def test_update(self):
        pass

    def test_upsert(self):
        pass

    def test_delete(self):
        pass
