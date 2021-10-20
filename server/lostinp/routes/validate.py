from flask import Blueprint, request
from lostinp.utils.decorators import user_must_be_registered

mod = Blueprint("login", __name__)


@mod.route("/validate", methods=["POST"])
@user_must_be_registered(request.headers)
def validate_route():
    return {
        "status": 200,
        "message": "user is registered",
    } 
