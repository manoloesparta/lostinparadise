from lostinp.models.user import User


USERS_REGISTERED = [
    {"username": "t30046", "visitCount": 0},
    {"username": "t30047", "visitCount": 2},
    {"username": "t30048", "visitCount": 6},
    {"username": "t30049", "visitCount": 1},
    {"username": "t30050", "visitCount": 3},
]

EXISTING_CRENDENTIALS = {"username": "t30046", "password": "ultrasecretpassword"}

NON_EXISTING_CRENDENTIALS = {"username": "t30045", "password": "invalid"}

EXISTING_USER = User(USERS_REGISTERED[0])

NON_EXISTING_USER = User({"username": "t30045"})

QUERY_EXISTING_USER = {"username": EXISTING_USER.username}

INVALID_REQUEST = {"username": "t30046"}

VALID_REQUEST = {"username": "t30046", "password": "ultrasecretpassword"}
