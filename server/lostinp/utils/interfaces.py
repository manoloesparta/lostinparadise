from abc import abstractmethod


class DbHandler:
    @abstractmethod
    def get_document(self):
        pass

    @abstractmethod
    def insert_document(self):
        pass

    @abstractmethod
    def update_document(self):
        pass

    @abstractmethod
    def upsert_document(self):
        pass

    @abstractmethod
    def delete_document(self):
        pass


class AuthenticationService:
    @abstractmethod
    def verify(self, username, password):
        pass
