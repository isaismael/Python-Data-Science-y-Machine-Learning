# datos temporales: fechas y horas
import pandas as pd

#creamos rango de fechas
#por defecto saltea los dias
#va a hacer 6 dias | 6 dilas
fechas = pd.Series(pd.date_range('1992-09-26', periods=6));
print(fechas)

print("- - - Dataframe con freq dias - - -");
fechas = pd.Series(pd.date_range('1992-09-26', periods=6, freq='D'));
print(fechas)

print("- - - Dataframe con freq meses - - -");
fechas = pd.Series(pd.date_range('1992-09-26', periods=6, freq='M'));
print(fechas)


print("- - - Dataframe con freq años - - -");
fechas = pd.Series(pd.date_range('1992-09-26', periods=6, freq='Y'));
print(fechas)


print("- - - Dataframe con freq horas - - -");
fechas = pd.Series(pd.date_range('1992-09-26', periods=6, freq='H'));
print(fechas)


print("- - - Dataframe con freq minutos - - -");
fechas = pd.Series(pd.date_range('1992-09-26', periods=6, freq='MIN'));
print(fechas)


print("- - - Dataframe con freq entre 5 dias - - -");
fechas = pd.Series(pd.date_range('1992-09-26', periods=6, freq='5D'));
print(fechas)

# - - -
print("- - - Dataframe con csv - - -");
route = f"12-pandas-datos-temporales\Mercado+de+Valores+España.csv"
