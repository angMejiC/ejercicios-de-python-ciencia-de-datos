#concatenacion por filas
import pandas as pd

DF1 = pd.DataFrame({'NOMBRE':['JOSE','MAX'],
                    'CARRERAS':['Economia','Arquitectura'],
                    'Edad':[23,26]}).set_index('NOMBRE')

DF2 = pd.DataFrame({'NOMBRE':['aurora','Maria'],
                    'CARRERAS':['Medicina','informatica'],
                    'Edad':[22,28]}).set_index('NOMBRE')

DF =pd.concat([DF1,DF2])
print(DF)