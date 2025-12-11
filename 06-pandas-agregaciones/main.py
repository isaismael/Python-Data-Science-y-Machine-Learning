# Agrecaciones en pandas, es una operacion que conbinan varios valores de datos en un solo valor representativo
# puede ser un promedio o una suma total
import pandas as pd

numeros = pd.Series([10, 20, 30, 40, 50]);

# promedio
print("- - - Promedio - - -")
promedio = numeros.mean();
print(f"El promedio es: {promedio}");

# total
print("- - - Total - - -")
total = numeros.sum();
print(f"El total es: {total}");

#numero maximo
print("- - - Numero maximo - - -")
maximo = numeros.max();
print(f"El numero maximo es: {maximo}");

#numero minimo
print("- - - Numero minimo - - -")
minimo = numeros.min();
print(f"El numero minimo es: {minimo}");


