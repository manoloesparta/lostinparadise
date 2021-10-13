import logging
import traceback
from flask import Blueprint, jsonify, request

from lostinp.controllers.login import LoginController
from lostinp.services.token import JwtService
from lostinp.services.authentication import MockedAuthService
from lostinp.repos.users import UsersRepo
from lostinp.utils.dbhandler import MongoHandler
from lostinp.utils.exceptions import ControllerException
from lostinp.utils.utils import lower_dict_keys

mod = Blueprint("login", __name__)


@mod.route("/login", methods=["POST"])
def login_route():

    token = JwtService()
    auth = MockedAuthService()
    mongo = MongoHandler()
    users = UsersRepo(mongo)

    controller = LoginController(auth, token, users)
    response = {}

    try:
        data = lower_dict_keys(request.get_json())
        token = controller.do_it(data)
        response = {
            "statusCode": 201,
            "message": {"X-Jwt-Key": token},
        }
    except ControllerException as e:
        logging.error(str(e))
        traceback.print_exc()
        response = {
            "statusCode": e.status_code,
            "message": {"error": str(e)},
        }
    except Exception as e:
        logging.error(str(e))
        traceback.print_exc()
        response = {
            "statusCode": 500,
            "message": {"error": "Internal Server error"},
        }

    return jsonify(response)
