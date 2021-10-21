from lostinp import create_app
from lostinp.utils.config import CONFIG

if __name__ == "__main__":
    app = create_app()
    conf = CONFIG.get_value("SANIC_CONFIG")
    app.run(**conf)
