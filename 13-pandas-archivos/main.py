import pandas as pd

ruta_xlsx = "13-pandas-archivos\Compras_desde_ads.xlsx"
ruta_xml = "Valores_de_acciones.xml"

print("- - - Lectura de xlsx - - -")
df1 = pd.read_excel(ruta_xlsx);
print(df1);

"""
print("- - - Lectura de xml - - -")
df2 = pd.read_xml(ruta_xml)
print(df2)
"""

print("- - - creando 1 csv a partir de df- - -")
numeros = {
    []
}