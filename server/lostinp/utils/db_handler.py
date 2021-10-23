import pymongo
from lostinp.utils.interfaces import DbHandler
from lostinp.utils.config import CONFIG
from lostinp.utils.exceptions import (
    DocumentNotFound,
    DuplicateDocumentId,
    CollectionNotSpecified,
)


class MongoHandler(DbHandler):

    client = pymongo.MongoClient(CONFIG.get_value("MONGO_CONN_STRING"))
    database = client["lost_in_paradise"]
    collection = None

    def set_collection(self, collection):
        self.collection = self.database[collection]

    def check_collection(self):
        if self.collection is None:
            raise CollectionNotSpecified(
                "A collection must be specified before doing any operation"
            )

    def get_document(self, query):
        self.check_collection()
        result = self.collection.find_one(query)
        if not result:
            raise DocumentNotFound("No document found with query filter: %s" % query)
        return result

    def get_all(self):
        self.check_collection()
        result = self.collection.find({})
        return list(result)

    def insert_document(self, insert):
        self.check_collection()
        try:
            self.collection.insert_one(insert)
        except:
            raise DuplicateDocumentId("Document %s already exists" % insert)

    def update_document(self, query, update):
        self.check_collection()
        update_doc = {"$set": update}
        result = self.collection.update_one(query, update_doc)
        if result.matched_count == 0:
            raise DocumentNotFound("No document found with query filter: %s" % query)

    def upsert_document(self, query, upsert):
        self.check_collection()
        upsert_doc = {"$set": upsert}
        self.collection.update_one(query, upsert_doc, upsert=True)

    def delete_document(self, query):
        self.check_collection()
        result = self.collection.delete_one(query)
        if result.deleted_count == 0:
            raise DocumentNotFound("No document found with query filter: %s" % query)
