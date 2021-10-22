import mongomock
from pytest import fixture
from sanic_testing import TestManager

from tests.routes.mocks.validate import REGISTERED_USER, VALID_HEADERS, INVALID_HEADERS


@mongomock.patch(servers=(("mongo", 27017),))
@fixture
def mocked_app():
    from sanic import Sanic
    from lostinp.routes.validate import bp as validate_blueprint
    from lostinp.models.user import User
    from lostinp.utils.db_handler import MongoHandler
    from lostinp.repos.users import UsersRepo

    handler = MongoHandler()
    repo = UsersRepo(handler)
    repo.register_user(User(REGISTERED_USER))

    app = Sanic("test_validate_route")
    app.blueprint(validate_blueprint)

    test = TestManager(app)
    client = test.test_client
    return client


def test_validated_user(mocked_app):
    pass


def test_invalidated_user(mocked_app):
    pass
