import json
from schematics import Model
from schematics.types import StringType, DateType


class LostItem(Model):

    uuid = StringType(required=True)
    status = StringType(required=True, choices=["Entregado", "Reportado"])
    category = StringType(required=True)
    description = StringType(required=True)

    # Where
    buildingName = StringType(required=True)
    roomNumber = StringType(required=True)
    deliveredAt = StringType()

    # Who
    foundBy = StringType(required=True)
    receivedBy = StringType(required=True)
    claimedBy = StringType()
    deliveredBy = StringType()

    # When
    foundOn = DateType(required=True)
    deliveredOn = DateType()

    # Observation
    receivedObservations = StringType()
    deliveredObservations = StringType()

    def to_json(self):
        return json.dumps(self.to_native(), default=str)
