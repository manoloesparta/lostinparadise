from lostinp.models.user import User
from lostinp.utils.exceptions import BadRequest, Unauthorized


class LoginController:
    def __init__(self, auth_service, token_service, user_repo):
        self.auth_service = auth_service
        self.token_service = token_service
        self.user_repo = user_repo

    def do_it(self, request):
        """Main method to perform the whole login"""
        user = self._check(request)
        self._verify_user_exists(user)
        self._register_or_increment_count(user)
        token = self.token_service.create_user_token(user.username)
        return token

    def _verify_user_exists(self, user):
        """Check if the user is registered in the authentication service"""
        verfied = self.auth_service.verify(user.username, user.password)
        if not verfied:
            raise Unauthorized("No match for username and password")

    def _register_or_increment_count(self, user):
        """
        Check if this is the first login attempt to
        register into the database or increment the
        visit count
        """
        registered = self.user_repo.is_user_registered(user)
        if registered:
            self.user_repo.increment_visit_counter(user)
        else:
            self.user_repo.register_user(user)

    def _check(self, request):
        """Verify all needed data is in the request"""
        try:
            username = request.get("username")
            password = request.get("password")
            user = User(username, password)
            user.validate()
        except:
            raise BadRequest("Missing username or password in request")
        return user
