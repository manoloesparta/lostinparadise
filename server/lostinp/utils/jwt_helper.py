import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta

from lostinp.utils.config import CONFIG
from lostinp.utils.exceptions import InvalidToken, ClaimNotFound


class JwtHelper:
    def __init__(self, secret=CONFIG.get_value("SECRET")):
        self.secret = secret

    def create_user_token(self, username):
        now = datetime.now()
        claims = {
            "iat": now,
            "exp": now + timedelta(days=1),
            "username": username,
        }
        token = jwt.encode(claims, self.secret, algorithm="HS256")
        return token

    def get_claim(self, token, key):
        try:
            claims = jwt.decode(token, self.secret, algorithms=["HS256"])
            return claims[key]
        except InvalidTokenError:
            raise InvalidToken("Token provided is invalid")
        except KeyError:
            raise ClaimNotFound("Claim %s not found in token" % key)
