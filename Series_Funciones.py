import pandas as pd

number = pd.Series([1,2,3,4,5,6,7,8,9])

#suma todos los numeros de la lista
print(number.sum())

#imprime el numero mayor de la lista
print(number.max())

#imprime el numero menor
print(number.min())

#encontrar la desviacion estandar
print(number.std())

#resumen del contenido de nuestra serie 
print(number.describe())