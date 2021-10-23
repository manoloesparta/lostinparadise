from sanic import Blueprint
from sanic.response import json
from lostinp.utils.decorators import user_must_be_registered

bp = Blueprint("validate")


@bp.post("/validate")
@user_must_be_registered
def validate_route(request):
    response = {"message": "user is registered"}
    return json(response, 200)
