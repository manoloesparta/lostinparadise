from sanic import Sanic
from sanic_cors import CORS
from sanic.response import json


app = Sanic(__name__)
CORS(app)


@app.post("/auth")
def mocked_auth_route(request):
    body = request.json
    username = body.get("Username")
    password = body.get("Password")

    strong_password = len(username) == 7 and len(password) > 8

    if not strong_password:
        return json({}, 400)

    return json({}, 200)


app.run(host="0.0.0.0", port=6666, debug=True)
