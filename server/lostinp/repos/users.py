from lostinp.models.user import User
from lostinp.utils.dbhandler import DbHandler
from lostinp.utils.exceptions import DocumentNotFound


class UsersRepo:
    collection_name = "users_registered"

    def __init__(self, db_handler: DbHandler):
        self.db_handler = db_handler
    
    def first_time_login(self, user: User) -> bool:
        try:
            self.db_handler.get_document(user.username)
            return False
        except DocumentNotFound:
            return True

    def register_user(self, user: User):
        self.db_handler.insert_document(user.to_native())

    def increment_visit_counter(self, user):
        query = {"username": user.username}
        update = user.to_native()
        update["visitCount"] += 1

        self.db_handler.update_document(query, update)
