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
            raise EnvironmentValueNotFound("Value does not exist")
        return res

    def _check_environment(self, env):
        valid_envs = ["dev", "int", "prod"]
        if env not in valid_envs:
            raise InvalidEnvironment("Invalid environment")

    def _build_env_dict(self):
        self.env_dict = {
            "SERVER_PORT": 5000,
            "MONGO_CONN_STRING": "mongodb://root:toor@mongo:27017",
            "AUTH_SERVICE_BASE_URL": "http://localhost:5000/auth",
            "SECRET": "development-secret",
        }


CONFIG = Configuration(environ.get("ENV", "dev"))
