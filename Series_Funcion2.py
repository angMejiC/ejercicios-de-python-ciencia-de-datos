import pandas as pd

serie = pd.Series({'matematica':8,'economia':6,'programacion':10,'fisica':5})

#filtrar el contenido apartir de alguna operacion logica
print(serie[serie > 6])

#ordenar los elementos
print(serie.sort_values())
print("")
#ordenar de forma asendente
print(serie.sort_index(ascending=False))