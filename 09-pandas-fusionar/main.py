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
print(df_combinado);
# en merge tiene un metodo llamado how que trae por defecto el valor inner how='inner'
# mezcla los registros de ambos lados que tienen datos

#tenemos otros paramos, outer (externo)
#tenemos todos los registros, rellena los datos faltos con NaN
print("- - - 02 - DataFrames concatenados - - -")
df_combinado = pd.merge(df1, df2, on='ID', how='outer')
print(df_combinado);


#parametro left
#incluye todos los registro con el df de la izquierda 
# y los rellena con todos los datos que coincida de la derecha
print("- - - 03 - DataFrames concatenados - - -");
df_combinado = pd.merge(df1, df2, on='ID', how='left')
print(df_combinado);


#parametro right , similiar a left
print("- - - 04 - DataFrames concatenados - - -");
df_combinado = pd.merge(df1, df2, on='ID', how='right')
print(df_combinado);


#otra posibilidad es unir todos los datos sin dejar nada afuera
#pero manteniendo los indices originales
#left_index y right_index
print("- - - 05 - DataFrames concatenados - - -")
df_combinado = pd.merge(df1, df2, left_index=True, right_index=True);
print(df_combinado);