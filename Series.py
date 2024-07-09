import pandas as pd

#lista a series
colores = pd.Series(['rojo','azul','amarillo','verde','morado'])
print(colores)
print("")
#diccionarios a series
materias =pd.Series({'Matematicas':60, 'fisica':100,'qimica':78})
print(materias)
print("")

#propiedades de las series

numeros =pd.Series([1,2,3,4,5,6,7,8,9])
#devuelve el numero de elementos de la serie 
print(numeros.size)
print("")
#devuelve una lista con los nombres de las filas con DataFrame
print(numeros.index)
print("")
#Devuelve el tipo de datos de los elementos de la serie
print(numeros.dtype)

#extraer datos de una serie 

#colores[1:2]
#print(colores)

#extraer diccionarios de uan serie
#materias[['fisica','quimica']]

#podemos hacer algunas operaciones basicas 
numeros1 = pd.Series([1,2,3,4,5,6])
print(numeros1*2)
