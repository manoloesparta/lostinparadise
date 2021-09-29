def insert_collection(handler, data):
    handler.collection.insert_many(data) 

def empty_collection(handler):
    handler.collection.delete_many({})