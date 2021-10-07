from lostinp.models.user import User
from lostinp.utils.dbhandler import DbHandler
from lostinp.utils.exceptions import DocumentNotFound


class UsersRepo:
    collection_name = "users_registered"

    def __init__(self, db_handler: DbHandler):
        self.db_handler = db_handler
        self.db_handler.set_collection(self.collection_name)

    def is_user_registered(self, user: User) -> bool:
        try:
            query = {"username": user.username}
            self.db_handler.get_document(query)
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
