import logging
import traceback
from flask import Blueprint, request

from lostinp.controllers.login import LoginController
from lostinp.utils.jwt_helper import JwtHelper
from lostinp.services.authentication import MockedAuthService
from lostinp.repos.users import UsersRepo
from lostinp.utils.db_handler import MongoHandler
from lostinp.utils.exceptions import ControllerException
from lostinp.utils.utils import lower_dict_keys

mod = Blueprint("login", __name__)


@mod.route("/login", methods=["POST"])
def login_route():

    token = JwtHelper()
    auth = MockedAuthService()
    mongo = MongoHandler()
    users = UsersRepo(mongo)

    controller = LoginController(auth, token, users)
    response = {}

    try:
        data = lower_dict_keys(request.get_json())
        token = controller.do_it(data)
        response = {
            "status": 201,
            "data": {"x-jwt-key": token},
        }
    except ControllerException as e:
        logging.error(str(e))
        traceback.print_exc()
        response = {
            "status": e.status_code,
            "error": str(e),
        }
    except Exception as e:
        logging.error(str(e))
        traceback.print_exc()
        response = {
            "status": 500,
            "error": "Internal Server error",
        }

    return response
