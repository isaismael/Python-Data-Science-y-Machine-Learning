import pandas as pd
# hacer limpieza de datos implica hacer procedimientos, como 
# detectar si hay valores faltantes o nulos, el manejo de esos valores
# eliminacion de duplicados, entre otras tareas más

data = {
    "Id_producto": [1001, 1002, 1003, 1003],
    "Cantidad_vendida": [30, None, 25, 25],
    "Precio": [20.5, 15.0, None, 22.5]
}

df = pd.DataFrame(data)
print("- - - Data Frame - - -")

# info nos da datos importantes para nuestra limpieza, por ejemplo ver si hay valores nulos
print("- - - Info - - -")
print(df.info())

# filtramos con el metodo isnull en bool para ver cuales estan vacios
print("- - - Null - - -")
print(df.isnull())

# sumamos los nulos de cada columna
print("- - - Sum Null - - -")
print(df.isnull().sum())

# eliminamos los registros que contengan null
print("- - - Delete Null - - -")
df_deleted = df.dropna()
print(df_deleted)

# cambiamos los valores de los null
print("- - - Change Null - - -")
df_changed = df.fillna(0)
print(df_changed)

# aplicando cambios de valores null a columnas
data_null = {
    "Cantidad_vendida": 0,
    "Precio": df["Precio"].mean()
    # mean es el promedio, en este caso promedio de lo que haya en la columna en general
}
df_filled = df.fillna(data_null)
print(df_filled)

# - - -
# correcion de tipo de datos
print("- - - Change Type - - -")
df_filled["Cantidad_vendida"] = df_filled["Cantidad_vendida"].astype(int)
print(df_filled)


# - - -
# verificamos si tenemos duplicamos, los eliminamos
# si no pasamos un parametro no hace ningun drop
print("- - - Delete Duplicates - - -")
# df_unique = df_filled.drop_duplicates()
df_unique = df_filled.drop_duplicates(subset=["Id_producto"])
print(df_unique)