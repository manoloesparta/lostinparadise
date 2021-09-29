import pymongo


class DbHandler:

    client = pymongo.MongoClient("mongodb://root:toor@mongo:27017/lost_in_paradise")
    database = client.lost_in_paradise

    def __init__(self, collection):
        self.collection = self.database[collection]

    def get_document(self, query):
        return self.collection.find_one(query)

    def insert_document(self, insert):
        self.collection.insert_one(insert)

    def update_document(self, query, update):
        result = self.collection.update_one(query, update)
        if result.matched_counts == 0:
            raise Exception("No document found with query filter: %s" % query)

    def upsert_document(self, query, update):
        result = self.collection.update_one(query, update, upsert=True)
        if result.matched_counts == 0:
            raise Exception("No document found with query filter: %s" % query)

    def delete_document(self, query):
        result = self.collection.delete_one(query)
        if result.matched_counts == 0:
            raise Exception("No document found with query filter: %s" % query)
