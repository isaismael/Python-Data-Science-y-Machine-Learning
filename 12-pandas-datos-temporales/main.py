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
route = r"12-pandas-datos-temporales\Mercado+de+Valores+España.csv"
df_csv = pd.read_csv(route);
print(df_csv)

print("- - - Dataframe con csv - - -");
test = df_csv['Fecha'][0];
print(type(test))

print("- - - Dataframe con csv convertir str a fecha - - -");
df_csv['Fecha'] = pd.to_datetime(df_csv['Fecha'], format='%d/%m/%Y');
print(df_csv);
print(type(df_csv['Fecha'][0]));

print("- - - Dataframe con csv traer info de fecha - - -")
print(df_csv['Fecha'][44].year);
print(df_csv['Fecha'][44].month);
print(df_csv['Fecha'][44].day);

print("- - - modificar datos de fecha del df - - -");
df_mas_5_dias = df_csv['Fecha'] + pd.Timedelta(days=5);
print(f"fecha modificada: \n{df_mas_5_dias}");