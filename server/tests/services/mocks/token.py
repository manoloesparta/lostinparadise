from jwt import encode
from datetime import datetime

SECRET = "secret"

USERNAME = "t030046"

TOKEN_WITHOUT_USERNAME = encode({"claim": "value"}, SECRET, "HS256")

EXPIRED_TOKEN = encode({"username": "t030046", "exp": datetime.now()}, SECRET, "HS256")
