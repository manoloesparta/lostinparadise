from lostinp.services.token import JwtService


def get_claim_from_jwt(token, key):
    jwt = JwtService()
    return jwt._get_claim(token, key)
