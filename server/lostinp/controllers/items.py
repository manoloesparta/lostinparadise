from lostinp.utils.exceptions import BadRequest


class GetLostItemsController:
    def __init__(self, items_repo):
        self.items_repo = items_repo

    def do_it(self, request):
        """Main method to perform the whole search"""
        query = self._check(request)
        result = self._get_lost_items(query)
        return result

    def _get_lost_items(self, query):
        """Search the items with the query"""
        return self.items_repo.get_lost_items_by_query(query)

    def _check(self, request):
        """Check that the request contains the query"""
        query = request.get("query")
        if not query:
            raise BadRequest("Query is not included in request")
        return query
