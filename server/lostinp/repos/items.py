from lostinp.utils.db_handler import DbHandler
from lostinp.models.item import LostItem
from lostinp.utils.utils import normalize_string


class LostItemsRepo:
    collection_name = "lost_items"

    def __init__(self, db_handler: DbHandler):
        self.db_handler = db_handler
        self.db_handler.set_collection(self.collection_name)

    def get_lost_items_by_query(self, query: str) -> list[LostItem]:
        norm_query = normalize_string(query)
        all_items = self.db_handler.get_all()

        result = []

        for item in all_items:
            is_reported = item["status"] == "Reportado"
            query_match = norm_query in item["searchString"]

            if query_match and is_reported:
                del item["_id"]
                del item["searchString"]

                lost = LostItem(item)
                lost.validate()
                result.append(lost)

        return result
