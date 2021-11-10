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
            "ENV": environ.get("ENV", "dev"),
            "MONGO_STRING": environ.get("MONGO", "mongodb://root:toor@mongo:27017"),
            "AUTH_BASE_URL": environ.get("CETYS_AUTH", "http://auth:6666/auth"),
            "SECRET": environ.get("SECRET", "development-secret"),
            "SANIC_CONFIG": {
                "host": environ.get("HOST", "0.0.0.0"),
                "port": environ.get("PORT", 5000),
                "debug": environ.get("ENV", "dev") != "prod",
            },
        }


CONFIG = Configuration(environ.get("ENV", "dev"))
