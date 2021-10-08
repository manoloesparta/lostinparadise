from lostinp.models.user import User
from lostinp.controllers import AUTH_SERVICE, TOKEN_SERVICE, USER_REPO


def login_controller(request: dict):
    username = request.get("username")
    password = request.get("password")

    user = User(**request, strict=False)
    user.validate()

    verfied = AUTH_SERVICE.verify(username, password)

    if verfied:
        registered = USER_REPO.is_user_registered(user)
        if registered:
            USER_REPO.increment_visit_counter(user)
        else:
            USER_REPO.register_user(user)

        token = TOKEN_SERVICE.create_user_token(username)
        response = {
            "statusCode": 201,
            "message": {
                "X-Jwt-Key": token,
            },
        }
        return response

    response = {
        "statusCode": 400,
        "message": {
            "error": "No match for username or password",
        },
    }
    return response
