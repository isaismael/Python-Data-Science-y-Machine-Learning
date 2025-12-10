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

#info nos da datos importantes para nuestra limpieza, por ejemplo ver si hay valores nulos
print("- - - Info - - -")
print(df.info())

#filtramos con el metodo isnull en bool para ver cuales estan vacios
print("- - - Null - - -")
print(df.isnull())



