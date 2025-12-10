import pandas as pd

df = pd.read_excel(r"02-pandas-xlsx\test.xlsx")

print(df)
# con head podemos ver las primeros 5 filas
print("- - head - -")
print(df.head())
# pero tmb podemos pasarle el parametro asi vemos la cantidad que queremos
print("- - head con parametro - -")
print(df.head(3))

#tmb tenemos el metodo tail, muestra los ultimos 5 registros
print("- - tail - -")
print(df.tail()) 

#shape es un atributo que nos devuelve informacion del dataframe (numero filas, numero columnas)
print("- - shape - -")
print(df.shape)

#atributo columns, nos devuelve una lista con todos los encabezados
#cando vemos dtype='object' se refiere que es string
print("- - columns - -")
print(df.columns)

#el metodo info() nos devuelve tipo de datos que tiene el data frame, como el indice, rango, etc
print("- - info - -")
print(df.info())

#describe es un metodo que nos trae info resumida lo que contiene las celdas numericas
print("- - describe - -")
print(df.describe())