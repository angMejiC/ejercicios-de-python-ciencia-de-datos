import pandas as pd

df = pd.read_csv('Book1.csv')

print(df)

#acceso mediante posisiones cordenadas con .iloc
print(df.iloc[1,3])
#por rango
print(df.iloc[2,:4])

#Accesos mediante posiciones

#Añadir columnas al dataFrame

df['TURNO'] = pd.Series(['tarde','noche','darde','noche','tarde','noche'])

print(df)

#eliminar columnas
print("")
SEMESTRE = df.pop('SEMESTRE')

print(df)

#añadir lilas a un DataFrame

#En lugar de usar append(), puedes usar pd.concat() 
#para concatenar el DataFrame existente con una nueva fila como una Serie:


new_fila = pd.Series(['carlos',27,'M','Sociologia','tarde'],
                         index=df.columns)

df =pd.concat([df,new_fila.to_frame().T], ignore_index=True)
print(df)

#eliminar una fila del DataFrame

print(df.drop([1]))
print(df)
print("")

#filtrado de filas de un DataFrame

print(df[(df['EDAD'] >= 25 )])

#ordenar 

print(df.sort_values('CARRERA'))

#para no imprimir los datos des
print(df.dropna())