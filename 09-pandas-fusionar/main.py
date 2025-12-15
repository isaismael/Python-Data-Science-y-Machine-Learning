import pandas as pd

#concatener dataframes
df1 = pd.DataFrame({
    'ID': [1, 2, 3],
    'Nombre': ['Ana', 'Luis', 'Carlos']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 4],
    'Edad': [25, 30, 42]
})

#on especifica la columna para unir
#osea solo nos va a unir las filas que tengan el mismo valor en la columna 'ID'
#fila con id 1 con fila con id 1 y asi sucesivamente
print("- - - 01 - DataFrames concatenados - - -")
df_combinado = pd.merge(df1, df2, on='ID')
print(df_combinado)