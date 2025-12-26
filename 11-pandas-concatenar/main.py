import pandas as pd;

d1 = pd.DataFrame(
    {
        'Nombre': ["Juan", "Gabriel", "Elena"],
        "Edad": [23, 31, 21]
    }
);

d2 = pd.DataFrame(
    {
        'Nombre': ["Carmela", "Max", "Laura"],
        "Edad": [34, 25, 29]
    }
);

#con axis 0 es el que mas se usa siempre
print("- - - Dataframe concatenado - - -")
df_concatenado = pd.concat([d1, d2]);
print(df_concatenado);

#podemos modificar el axis que es el eje
#por defecto viene en 0
#pero si ponemos en 1 que es el eje de las filas
#concatena horizontalmente
print("- - - Dataframe concatenado axis - - -")
df_concatenado = pd.concat([d1, d2], axis=1);
print(df_concatenado);


print("- - - Dataframe concatenado ignorar indice - - -")
df_concatenado = pd.concat([d1, d2], ignore_index=True);
print(df_concatenado);



print("- - - Dataframe concatenado marcas de grupos (key) - - -")
df_concatenado = pd.concat([d1, d2], keys=['df1', 'df2']);
print(df_concatenado);