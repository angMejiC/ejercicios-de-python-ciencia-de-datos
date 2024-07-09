import pandas as pd

DF1 = pd.DataFrame({'AUTOS':['nissan','ford','audi'],
                    'COLOR':['blanco','azul','rojo']})

DF2 = pd.DataFrame({'AUTOS':['toyota','ford','audi'],
                    'MODELO':[2018,2020,2022]})

#con merge vamos a mezclar tienen que tener datos en comun
DF = pd.merge(DF1,DF2, on='AUTOS', how='outer')

print(DF1)
print("")
print(DF2)
print("")
print(DF)