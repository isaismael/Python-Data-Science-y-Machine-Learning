import pandas as pd

datos = {
    "nombres": ["ismael", "juan", "jorge"],
    "edades": [33, 36, 22]
}

df = pd.DataFrame(datos);

# imprimo todo el df completo
print(df)
# tmb puedo acceder que quiera
print(df["nombres"])
print(df["edades"])
# para ver que tipo es el dataframe
print(type(df))

# repaso: un df es una tabla bidimensional, que tiene filas y columnas
# si tomo una columna del df se llama series
# las series solo tiene una dimension
# el df tiene index, filas y columnas