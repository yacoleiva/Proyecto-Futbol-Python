import pandas as pd
import requests
import sqlite3
#1. extraccion: pedir datos a la API
url = "https://api.football-data.org/v4/competitions/BSA/standings" #Brasileirao
headers = {"X-Auth-Token": "b451344b939b4d078140274e8eef0061"}
response = requests.get(url, headers=headers)
data = response.json()
#2.Transformacion: limpiar con pandas
# Navegamos el JSON para extraer la tabla de posiciones
Posiciones = data["standings"][0]["table"]
# Convertimos la lista de diccionarios en un DataFrame de Pandas
df = pd.DataFrame(Posiciones)
# Extraemos el nombre del equipo dentro del diccionario 'team'
df["equipo"] = df["team"].apply(lambda x: x["name"])
# Seleccionamos y renombras las columnas en un solo paso limpio
df_limpio = df[["position","equipo","points"]].rename(
    columns={
        "position": "posicion",
        "points": "puntos"
    }
)
print(df_limpio.head())