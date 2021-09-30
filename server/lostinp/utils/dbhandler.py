import pymongo
from lostinp.utils.config import CONFIG
from lostinp.utils.exceptions import DocumentNotFound, DuplicateDocumentId


class DbHandler:

    client = pymongo.MongoClient(CONFIG.get_value("MONGO_CONN_STRING"))
    database = client["lost_in_paradise"]

    def __init__(self, collection):
        self.collection = self.database[collection]

    def get_document(self, query):
        result = self.collection.find_one(query)
        if not result:
            raise DocumentNotFound("No document found with query filter: %s" % query)
        return result

    def insert_document(self, insert):
        try:
            print(insert)
            self.collection.insert_one(insert)
            print(insert)
        except:
            raise DuplicateDocumentId("Document %s already exists" % insert)

    def update_document(self, query, update):
        update_doc = {"$set": update}
        result = self.collection.update_one(query, update_doc)
        if result.matched_count == 0:
            raise DocumentNotFound("No document found with query filter: %s" % query)

    def upsert_document(self, query, upsert):
        upsert_doc = {"$set": upsert}
        self.collection.update_one(query, upsert_doc, upsert=True)

    def delete_document(self, query):
        result = self.collection.delete_one(query)
        if result.deleted_count == 0:
            raise DocumentNotFound("No document found with query filter: %s" % query)
