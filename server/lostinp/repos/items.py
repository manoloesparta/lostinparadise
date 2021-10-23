from lostinp.utils.db_handler import DbHandler
from lostinp.models.item import LostItem


class LostItemsRepo:
    collection_name = "lost_items"

    def __init__(self, db_handler: DbHandler):
        self.db_handler = db_handler
        self.db_handler.set_collection(self.collection_name)

    def get_lost_items_by_query(self, query: str) -> list[LostItem]:
        pass
