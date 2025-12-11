# filtrado de serie es como hacerle preguntas a nuestros datos
# basicamente es seleccionar elemento que cumplan con ciertos elementos
import pandas as pd

serie = pd.Series([5, 10, 15, 20, 25]);

print("- - - Data Frame - - -");
print(serie);

print("- - - Filtro - - -");
# acá nos daran bool si se cumple la condicion es True, sino False
filtro = serie > 15;
serie_filtrada = serie[filtro];
print(serie_filtrada);

# se puede hacer filtros en series con valores de texto
serie2 = pd.Series(["Manzana", "Banana", "Cereza", "Durazno", "Fresa", "Melón"]);
# acá vemos todos los metodos que podemos acceder a series2
print("- - - Metodos - - -")
#print(dir(serie2));
print("- - - Info del método - - -");
#help(serie2.str)

#usamos el metodo contains de str
print("- - - Filtro 2- - -");
filtro2 = serie2.str.contains("M");
print(filtro2);