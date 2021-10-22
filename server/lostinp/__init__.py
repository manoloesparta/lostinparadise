from sanic import Sanic
from sanic_cors import CORS


def create_app():
    app = Sanic(__name__)
    CORS(app)

    from lostinp.routes.login import bp as login_blueprint
    from lostinp.routes.validate import bp as validate_blueprint

    app.blueprint(login_blueprint)
    app.blueprint(validate_blueprint)

    return app
