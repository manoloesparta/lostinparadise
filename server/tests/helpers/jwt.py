from lostinp.utils.jwt_helper import JwtHelper


def get_claim_from_jwt(token, key):
    jwt = JwtHelper()
    return jwt.get_claim(token, key)
