from lostinp.utils.jwt_helper import JwtHelper

jwt = JwtHelper()


def get_claim_from_jwt(token, key):
    return jwt.get_claim(token, key)


def create_token(username):
    return jwt.create_user_token(username)
