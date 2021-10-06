from lostinp.models.user import User


USERS_DICT_MOCK = [
    {"username": "diego", "visitCount": 0},
    {"username": "miza", "visitCount": 1},
    {"username": "juampi", "visitCount": 2},
    {"username": "deivid", "visitCount": 4},
    {"username": "oscar", "visitCount": 8},
    {"username": "isaac", "visitCount": 16},
]

REGISTERED_USER = User(USERS_DICT_MOCK[1])

UNREGISTERED_USER = User({"username": "manolo"})
