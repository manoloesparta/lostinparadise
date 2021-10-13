from os import environ
from lostinp import app_factory

env = environ.get("ENV", "development")
app = app_factory(env)

if __name__ == "__main__":
    app()
