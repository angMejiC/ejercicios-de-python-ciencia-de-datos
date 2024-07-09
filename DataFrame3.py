import pandas as pd

#funcion para leer archivo csv
df = pd.read_csv('ModalidadVirtual.csv')
print(df)


#filtrar los datos de edad  mayores a 23
print(df['edad'] > 23)

filtrar = df['edad'] > 23

df_filtar = df[filtrar]
print(df_filtar)

#imprimimos los 10 primeros elementos con el metodo head
print(df.head(10))

