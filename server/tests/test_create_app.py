import mongomock
from pytest import fixture

from sanic_testing import TestManager


@fixture
@mongomock.patch(servers=(("mongo", 27017),))
def mocked_app():
    from lostinp import create_app
    from lostinp.routes.health import bp as healt_blueprint

    app = create_app()
    app.blueprint(healt_blueprint)
    test = TestManager(app)

    return test


def test_create_app(mocked_app):
    _, response = mocked_app.test_client.get("/health")
    assert response.status == 200
