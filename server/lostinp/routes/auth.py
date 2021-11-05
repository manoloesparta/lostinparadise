from sanic import Blueprint
from sanic.response import json

bp = Blueprint("mocked_auth")


@bp.get("/auth")
def mocked_auth_route(request):
    body = request.json
    username = body.get("Username")
    password = body.get("Password")

    strong_password = len(username) == 7 and len(password) > 8

    if not strong_password:
        return json({}, 400)

    return json({}, 200)
