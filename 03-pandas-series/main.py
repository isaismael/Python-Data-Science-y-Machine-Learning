import pandas as pd

df = pd.read_excel(r"03-pandas-series\test.xlsx");

print("- - - Series en Pandas - - -")
#print(df.head());  

serie = df["CODIGO"]
print(serie.head())

# tmb podemos crear nuestra propia serie
print("- - - Serie creada - - -")
datos = ["100", "200", "300", "400", "500"]
serie2 = pd.Series(datos)
print(serie2)

#tmb podemos personalizar nuestros indices
print("- - - Serie con indices personalizados - - -")
indices = ["a", "b", "c", "d", "e"]
serie3 = pd.Series(datos, index=indices)
print(serie3)

#puedo seleccionar elementos usando mis indices personalizados
print("- - - Elemento seleccionado - - -")
print(serie3["d"])

#creando serie con indice personalizado a partir de un diccionario
print("- - - Serie creada a partir de un diccionario - - -")
capitales = {"Estados unidos": "Washintong", "Argentina": "Buenos Aires", "España": "Madrid"}
serie4 = pd.Series(capitales)
print(serie4)

