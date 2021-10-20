from flask import Flask
from flask_cors import CORS
from gevent.pywsgi import WSGIServer

from lostinp.utils.config import CONFIG


def app_factory(env):
    app = Flask(__name__)
    CORS(app)

    from lostinp.routes.login import mod as login_module
    from lostinp.routes.validate import mod as validate_module

    app.register_blueprint(login_module)
    app.register_blueprint(validate_module)

    def app_runner():
        port = CONFIG.get_value("SERVER_PORT")

        if env.lower() == "prod":
            http_server = WSGIServer(
                listener=("0.0.0.0", port),
                application=app,
            )
            return http_server.serve_forever()

        return app.run(host="0.0.0.0", port=port, debug=True)

    return app_runner
