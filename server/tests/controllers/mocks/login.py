from lostinp.models.user import User


USERS_REGISTERED = [
    {"username": "t030046", "visitCount": 0},
    {"username": "t030047", "visitCount": 2},
    {"username": "t030048", "visitCount": 6},
    {"username": "t030049", "visitCount": 1},
    {"username": "t030050", "visitCount": 3},
]

EXISTING_CRENDENTIALS = {"username": "t030046", "password": "ultrasecretpassword"}

NON_EXISTING_CRENDENTIALS = {"username": "t030045", "password": "invalid"}

EXISTING_USER = User(USERS_REGISTERED[0])

NON_EXISTING_USER = User({"username": "t030045"})

QUERY_EXISTING_USER = {"username": EXISTING_USER.username}

INVALID_REQUEST = {"username": "t030046"}

VALID_REQUEST = {"username": "t030046", "password": "ultrasecretpassword"}
