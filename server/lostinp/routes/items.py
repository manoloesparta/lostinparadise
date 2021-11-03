import logging
import traceback
from sanic import Blueprint
from sanic.response import json

from lostinp.utils.decorators import user_must_be_registered
from lostinp.repos.items import LostItemsRepo
from lostinp.controllers.items import GetLostItemsController
from lostinp.utils.db_handler import MongoHandler
from lostinp.utils.exceptions import ControllerException
from lostinp.utils.utils import lower_dict_keys

bp = Blueprint("search")


@bp.post("/search")
@user_must_be_registered
def search_items_route(request):

    mongo = MongoHandler()
    items = LostItemsRepo(mongo)

    controller = GetLostItemsController(items)
    response = json({}, 200)

    try:
        body = request.json
        data = lower_dict_keys(body)
        items = controller.do_it(data)
        out = {"data": {"items": items}}
        response = json(out, 200, default=str)
    except ControllerException as e:
        logging.error(str(e))
        traceback.print_exc()
        out = {"error": str(e)}
        response = json(out, e.status_code)
    except Exception as e:
        logging.error(str(e))
        traceback.print_exc()
        out = {"error": "Internal Server error"}
        response = json(out, 500)

    return response
