import pandas as pd

df = pd.read_csv(r"08-pandas-ordenar-agrupar\Top-Películas.csv")

# si no podemos ascending por defecto es True (ascendente)
df_ordenado = df.sort_values(by="rating", ascending=False)
print("- - - 01 DataFrame ordenado por rating: - - -")
print(df_ordenado.head(10))

# hacer sort por mas de una columna
print("- - - 02 Dataframe ordenado por rating y recaudación: - - -")
df_ordenado_multiple = df.sort_values(by=["rating", "recaudación(M)"], ascending=False)
print(df_ordenado_multiple.head(10))


#agrupamos de dataframe, sirve para un analisis comparativo
print("- - - 03 DataFrame agrupado groupby: - - -")
df_agrupado = df.groupby("género")['rating'].mean()
print(df_agrupado) 

#agrupado agrupados recaudación por año
print("- - - 04 DataFrame agrupado groupby: - - -")
df_agrupado_año = df.groupby("año")['recaudación(M)'].sum()
print(df_agrupado_año.sort_values(ascending=False).head(10));