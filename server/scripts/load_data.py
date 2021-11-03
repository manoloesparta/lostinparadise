import pymongo
import pandas as pd
from uuid import uuid4
from unidecode import unidecode


def normalize(string):
    accents = unidecode(str(string).lower())
    return accents


def remove_time_from_date(date):
    if date == "Pending":
        return date
    string = str(date)
    return string.split(" ")[0]


client = pymongo.MongoClient("mongodb://root:toor@localhost:27017/")
db = client["lost_in_paradise"]
col = db["lost_items"]

data = pd.read_excel("scripts/data.xlsx")
data = data.fillna("Pendiente")

insert = []

for index, row in data.iterrows():
    normal_category = normalize(row["Catergoria"])
    normal_description = normalize(row["Descripcion"])

    one = {
        "uuid": str(uuid4()),
        "status": row["Status"],
        # What?
        "category": row["Catergoria"],
        "description": row["Descripcion"],
        # Where?
        "buildingName": row["Nombre_Edificio"],
        "roomNumber": row["Nombre_Espacio"],
        "deliveredAt": row["DondeEntrego"],
        # Who?
        "foundBy": row["QuienEncontro"],
        "receivedBy": row["QuienRecibio"],
        "claimedBy": row["QuienReclamo"],
        "deliveredBy": row["QuienEntrego"],
        # When?
        "foundOn": remove_time_from_date(row["FechaEntrada"]),
        "deliveredOn": remove_time_from_date(row["FechaSalida"]),
        # Observations
        "receivedObservations": row["ObservacionesEntrada"],
        "deliveredObservations": row["ObservacionesSalida"],
        # Search
        "searchString": "%s %s" % (normal_category, normal_description),
    }

    if row["Status"] != "Entregado":
        del one["claimedBy"]
        del one["deliveredAt"]
        del one["deliveredBy"]
        del one["deliveredOn"]
        del one["deliveredObservations"]

    insert.append(one)

col.insert_many(insert)
