from jwt import encode
from datetime import datetime, timedelta

SECRET = "secret"

USERNAME = "t030046"

TOKEN_WITHOUT_USERNAME = encode({"claim": "value"}, SECRET, "HS256")


EXPIRED_TOKEN = encode(
    payload={"username": "t030046", "exp": datetime.now() - timedelta(days=1)},
    key=SECRET,
    algorithm="HS256",
)
