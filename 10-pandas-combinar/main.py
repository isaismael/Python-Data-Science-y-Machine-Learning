#combinar != fusionar, suena parecido pero no lo es
#usando el metodo join, unir 2 df a partir de su indices
#o una columna clave y no de columnas compartidas
#por mas que no tengamos columnas similares lo podemos hacer, por el index
import pandas as pd

df1 = pd.DataFrame({
    'Salario': [30000, 45000, 38000],
    'Antiguedad': [9, 13, 12]},
     index=[1, 2, 3]);

df2 = pd.DataFrame({
    'Ciudad': ['Madrid', 'Barcelona', 'Valencia'],
    'Jerarquia': ['Baja', 'Alta', 'Media']},
     index=[1, 2, 4]);

print("- - - Dataframe unido - - -");
df_unido = df1.join(df2);
print(df_unido);

print("- - - Dataframe unido por index - - -");
df_unido_index = df1.join(df2, how='inner');
print(df_unido_index);