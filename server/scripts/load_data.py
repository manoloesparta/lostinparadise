import pymongo
import pandas as pd


client = pymongo.MongoClient("mongodb://root:toor@localhost:27017/")
db = client["lost_in_paradise"]
col = db["lost_items"]

data = pd.read_excel("scripts/data.xlsx")
data = data.fillna("none")

insert = []

for index, row in data.iterrows():
    one = {
        "status": row["Status"],
        # What?
        "category": row["Catergoria"],
        "description": row["Descripcion"],
        # Where?
        "buldingName": row["Nombre_Edificio"],
        "roomNumber": row["Nombre_Espacio"],
        "deliveredAt": row["DondeEntrego"],
        # Who?
        "foundBy": row["QuienEncontro"],
        "recievedBy": row["QuienRecibio"],
        "claimedBy": row["QuienReclamo"],
        "deliveredBy": row["QuienEntrego"],
        # When?
        "recievedOn": row["FechaEntrada"],
        "deliveredOn": row["FechaSalida"],
        # Observations
        "recievedObservations": row["ObservacionesEntrada"],
        "deliveredObservations": row["ObservacionesSalida"],
    }
    insert.append(one)

col.insert_many(insert)
