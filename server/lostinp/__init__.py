from flask import Flask
from flask_cors import CORS
from werkzeug.serving import run_simple


def app_factory(env):
    app = Flask(__name__)
    CORS(app)

    from lostinp.routes.users import mod as users_module

    app.register_blueprint(users_module)

    def wrapper():
        if env.lower() in ["production", "prod"]:
            run_simple(
                hostname="0.0.0.0",
                port=80,
                application=app,
                use_debugger=False,
                use_reloader=False,
            )
        app.run(host="0.0.0.0", port=5000, debug=True)

    return wrapper
