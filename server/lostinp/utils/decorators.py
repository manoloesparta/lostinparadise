import logging
import traceback
from functools import wraps
from sanic.response import json

from lostinp.models.user import User
from lostinp.repos.users import UsersRepo
from lostinp.utils.db_handler import MongoHandler
from lostinp.utils.jwt_helper import JwtHelper
from lostinp.utils.exceptions import Unauthorized


handler = MongoHandler()
repo = UsersRepo(handler)
jwt_helper = JwtHelper()


def user_must_be_registered(func):
    @wraps(func)
    def inner(request):
        try:
            token = request.headers.get("X-Jwt-Key")
            validate_token(token)
        except Exception as e:
            logging.error(str(e))
            traceback.print_exc()
            response = {
                "status": 400,
                "error": "username in jwt is not valid",
            }
            return json(response)
        return func(request)

    return inner


def validate_token(token):
    username = jwt_helper.get_claim(token, "username")
    user = User({"username": username})
    user.validate()
    if not repo.is_user_registered(user):
        raise Unauthorized()
