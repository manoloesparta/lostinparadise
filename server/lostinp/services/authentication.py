from re import match

from lostinp.utils.interfaces import AuthenticationService


class MockedAuthService(AuthenticationService):
    def verify(self, username: str, password: str) -> bool:
        return self.username_valid(username) and self.password_strong(password)

    def username_valid(self, username: str) -> bool:
        regex = r"^t[0-9]{6}$"
        result = match(regex, username)
        return bool(result)

    def password_strong(self, password: str) -> bool:
        return len(password) > 8
