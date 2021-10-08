from lostinp.utils.dbhandler import MongoHandler
from lostinp.repos.users import UsersRepo
from lostinp.services.authentication import MockedAuthService
from lostinp.services.token import JwtService


DB_HANDLER = MongoHandler()

USER_REPO = UsersRepo(DB_HANDLER)

AUTH_SERVICE = MockedAuthService()

TOKEN_SERVICE = JwtService()
