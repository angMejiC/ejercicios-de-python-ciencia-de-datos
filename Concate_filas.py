import pandas as pd

DF1 = pd.DataFrame({'AUTOS':['nissan','ford','audi'],
                    'COLOR':['blanco','azul','rojo']}).set_index('AUTOS')

DF2 = pd.DataFrame({'AUTOS':['nissan','ford','audi'],
                    'MODELO':[2018,2020,2022]}).set_index('AUTOS')

DF = pd.concat([DF1,DF2], axis=1) 


print(DF1)
print("")
print(DF2)
print("")
print(DF)