import pandas as pd

#loc selecciona filas y columnas que tengan etiquetas especificas

df = pd.DataFrame({
    'Col1': [100, 200, 300, 400, 500],
    'Col2': ['a', 'b', 'c', 'd', 'e'],
    'Col3': [0.1, 0.2, 0.3, 0.4, 0.5]
}, index=['fila1', 'fila2', 'fila3', 'fila4', 'fila5'])

print(df)

print("- - - usando loc - - -")
loc_seleccionado = df.loc['fila1'];
print(loc_seleccionado)

print("- - - usando loc - - -")
loc_seleccionado = df.loc[['fila1', 'fila3']];
print(loc_seleccionado)

print("- - - usando loc con segmentacion - - -")
loc_seleccionado = df.loc['fila2':'fila3'];
print(loc_seleccionado);

print("- - - usando loc con segmentacion con bool - - -");
print(df.loc[[False, True, False, True, False]]);

print("- - - usando loc comparando valores - - -");
print(df.loc[df['Col1'] > 150]);

print("- - - trayendo columnas en ves de filas - - -");
# los : segmenta todo, es como decir pasame todo 
print(df.loc[:, ['Col1', 'Col2']]);

"""
en resumen loc nos permite seleccionar filas y columnas basandonos en sus etiquetas
"""

# iloc hace lo mismo pero pero basando en sus 
# posiciones numericas, osea el index

print("- - - usando iloc - - -")
iloc_seleccionado = df.iloc[0];
print(iloc_seleccionado)

print("- - - usando iloc seleccionando varias columnas- - -")
iloc_seleccionado = df.iloc[:, [0, 1]];
print(iloc_seleccionado)

print("- - - usando iloc seleccionando un rango de filas - - -")
iloc_seleccionado = df.iloc[1:3];
print(iloc_seleccionado);