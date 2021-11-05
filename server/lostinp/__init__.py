from sanic import Sanic
from sanic_cors import CORS

from lostinp.utils.config import CONFIG


def create_app():
    app = Sanic(__name__)
    CORS(app)

    from lostinp.routes.login import bp as login_blueprint
    from lostinp.routes.validate import bp as validate_blueprint
    from lostinp.routes.items import bp as search_items_blueprint

    app.blueprint(login_blueprint)
    app.blueprint(validate_blueprint)
    app.blueprint(search_items_blueprint)

    if CONFIG.get_value("ENV") == "dev":
        from lostinp.routes.auth import bp as auth_blueprint

        app.blueprint(auth_blueprint)

    return app
