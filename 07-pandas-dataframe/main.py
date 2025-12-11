#vamos a trabajar con dataframe

import pandas as pd

data = {
    'Nombre': ['Juan', 'María', 'Pedro', 'Ana', 'Luis'],
    'Edad': [25, 30, 35, 20, 45],
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia', 'Sevilla', 'Bilbao']
}

df = pd.DataFrame(data)
print("- - - Dataframe - - -")
print(df)

#agregar una columana nueva a nuestro df
print("- - - Insertar una columna - - -")
df["Salario"] = [5000, 6000, 7000, 8000, 9000];
print(df)

#modificar los valores de una columna, es parecido a una serie
print("- - - Modificar los valores de una columna - - -")
df["Salario"] = df["Salario"] + 1500
print(df)

#almacenar una columna en una variable independiente
print("- - - Almacenar una columna en una variable independiente - - -")
salarios = df["Nombre"]
print(salarios)

#aplicar filtrados para ver solo las filas o registros que cumplen con ese filtro
print("- - - Aplicar un filtro - - -")
mayores_25 = df[df['Edad'] > 25];
print(mayores_25)

#almacenar una columan en una variable
print("- - - Almacenar una columna en una variable - - -")
edades = df["Edad"]
print(edades)

#realizamos comparacion con la edad
print("- - - Comparacion con la edad almacenada en una variable - - -")
mayores_25 = df[edades > 25]
print(mayores_25)