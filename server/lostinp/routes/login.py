import logging
from flask import Blueprint, jsonify, request

from lostinp.controllers.login import login_controller

mod = Blueprint("login", __name__)


@mod.route("/login", methods=["POST"])
def login():

    response = {}

    try:
        data = request.json
        response = login_controller(data)
    except Exception as e:
        logging.error(str(e))
        response = {
            "statusCode": 500,
            "message": {
                "error": "Internal Server error",
            },
        }

    return jsonify(response)
