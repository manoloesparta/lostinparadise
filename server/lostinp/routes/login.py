import logging
import traceback
from sanic import Blueprint
from sanic.response import json

from lostinp.controllers.login import LoginController
from lostinp.utils.jwt_helper import JwtHelper
from lostinp.services.authentication import MockedAuthService
from lostinp.repos.users import UsersRepo
from lostinp.utils.db_handler import MongoHandler
from lostinp.utils.exceptions import ControllerException
from lostinp.utils.utils import lower_dict_keys

bp = Blueprint("login")


@bp.route("/login", methods=["POST"])
def login_route(request):

    token = JwtHelper()
    auth = MockedAuthService()
    mongo = MongoHandler()
    users = UsersRepo(mongo)

    controller = LoginController(auth, token, users)
    response = json({}, 200)

    try:
        body = request.json
        data = lower_dict_keys(body)
        token = controller.do_it(data)
        out = {"data": {"x-jwt-key": token}}
        response = json(out, 201)
    except ControllerException as e:
        logging.error(str(e))
        traceback.print_exc()
        out = {"error": str(e)}
        response = json(out, e.status_code)
    except Exception as e:
        logging.error(str(e))
        traceback.print_exc()
        out = {"error": "Internal Server error"}
        response = json(out, 500)

    return response
