from os import environ
from lostinp.utils.exceptions import EnvironmentValueNotFound, InvalidEnvironment


class Configuration:

    env_dict = {}

    def __init__(self, env):
        self.env_name = env
        self._check_environment(env)
        self._build_env_dict()

    def get_value(self, key):
        res = self.env_dict.get(key)
        if not res:
            raise EnvironmentValueNotFound("Value does not exist for key: %s" % key)
        return res

    def _check_environment(self, env):
        valid_envs = ["dev", "int", "prod"]
        if env not in valid_envs:
            raise InvalidEnvironment("Invalid environment")

    def _build_env_dict(self):
        self.env_dict = {
            "ENV": environ.get("ENV"),
            "MONGO_STRING": environ.get("MONGO"),
            "AUTH_BASE_URL": environ.get("CETYS_AUTH"),
            "SECRET": environ.get("SECRET"),
            "SANIC_CONFIG": {
                "host": environ.get("HOST"),
                "port": environ.get("PORT"),
                "debug": environ.get("ENV") != "prod",
            },
        }


CONFIG = Configuration(environ.get("ENV"))
