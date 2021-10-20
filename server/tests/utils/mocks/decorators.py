from tests.helpers.jwt import create_token


USERS_REGISTERED = [
    {"username": "t030046", "visitCount": 1},
    {"username": "t042069", "visitCount": 3},
    {"username": "t012345", "visitCount": 2},
]

VALID_TOKEN = create_token("t030046")

VALID_HEADERS = {"X-Jwt-Key": VALID_TOKEN}

INVALID_TOKEN = "blah.blah.blah"

INVALID_TOKEN_HEADERS = {"X-Jwt-Key": INVALID_TOKEN}

NOT_REGISTERED_TOKEN = create_token("t066666")

NOT_REGISTERED_HEADERS = {"X-Jwt-Key": NOT_REGISTERED_TOKEN}
