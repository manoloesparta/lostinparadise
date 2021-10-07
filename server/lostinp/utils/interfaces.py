from abc import abstractmethod


class DbHandler:
    @abstractmethod
    def set_collection(self, collection):
        pass

    @abstractmethod
    def get_document(self, query):
        pass

    @abstractmethod
    def insert_document(self, insert):
        pass

    @abstractmethod
    def update_document(self, query, update):
        pass

    @abstractmethod
    def upsert_document(self, query, upsert):
        pass

    @abstractmethod
    def delete_document(self, query):
        pass


class AuthenticationService:
    @abstractmethod
    def verify(self, username, password):
        pass


class TokenService:
    @abstractmethod
    def create_user_token(self, username):
        pass

    @abstractmethod
    def get_username_claim(self, token):
        pass
