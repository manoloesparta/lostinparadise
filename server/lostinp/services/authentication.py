import json
import requests

from lostinp.utils.config import CONFIG
from lostinp.utils.interfaces import AuthenticationService


class CetysAuthentication(AuthenticationService):
    def verify(self, username: str, password: str) -> bool:
        url = CONFIG.get_value("AUTH_BASE_URL")
        body = {"Username": username, "Password": password}
        response = requests.post(url, data=json.dumps(body))
        return response.status_code == 200


class MockedAuthService(AuthenticationService):
    def verify(self, username: str, password: str) -> bool:
        strong_password = len(username) == 7 and len(password) > 8
        return strong_password
