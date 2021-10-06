import json
from schematics import Model
from schematics.types import StringType, IntType


class User(Model):

    username = StringType(required=True, min_length=5, max_length=12)
    visitCount = IntType(required=True, default=0)

    def to_json(self):
        return json.dumps(self.to_primitive())
