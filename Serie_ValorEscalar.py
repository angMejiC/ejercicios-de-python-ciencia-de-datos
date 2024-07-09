import pandas as pd

data = 5

serie = pd.Series(data, index=[0,1,2,3,4,5])
print(serie)

#serie con indice definido

data_list = ['messi','cristiano ronaldo','benzema']
indices = ['PSG','Manchester united','Real Madrid']

futbol = pd.Series(index=indices,data=data_list)

print(futbol)