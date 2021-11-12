from tests.helpers.jwt import create_token


REGISTERED_USER = {"username": "t030046"}

VALID_HEADERS = {"x-jwt-key": create_token("t030046")}

INVALID_HEADERS = {"x-jwt-key": create_token("t012345")}
