from pytest import fixture

from lostinp.services.authentication import MockedAuthService
from tests.services.mocks.authentication import VALID_CREDENTIALS, INVALID_CREDENTIALS


@fixture
def service():
    yield MockedAuthService()


def test_valid_credentials(service):
    print(VALID_CREDENTIALS)
    res = service.verify(**VALID_CREDENTIALS)
    assert res


def test_invalid_credentials(service):
    res = service.verify(**INVALID_CREDENTIALS)
    assert not res
