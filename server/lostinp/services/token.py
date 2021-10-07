import jwt
from jwt.exceptions import InvalidTokenError
from datetime import datetime, timedelta

from lostinp.utils.config import CONFIG
from lostinp.utils.interfaces import TokenService
from lostinp.utils.exceptions import InvalidToken, ClaimNotFound


class JwtService(TokenService):
    def create_user_token(self, username):
        now = datetime.now()
        claims = {
            "iat": now,
            "exp": now + timedelta(days=1),
            "username": username,
        }
        token = jwt.encode(claims, CONFIG.get_value("SECRET"))
        return token

    def get_claim(self, token, key):
        try:
            claims = jwt.decode(token, CONFIG.get_value("SECRET"))
            return claims[key]
        except InvalidTokenError:
            raise InvalidToken("Token provided is invalid")
        except KeyError:
            raise ClaimNotFound("Claim %s not found in token" % key)
