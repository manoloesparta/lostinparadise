from os import environ
from lostinp import app_factory


if __name__ == "__main__":
    env = environ.get("ENV", "development")
    app = app_factory(env)
    app()
