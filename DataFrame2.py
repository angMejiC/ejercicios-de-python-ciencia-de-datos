import pandas as pd
import numpy as np

#generar un DataFrame apartir de una array
df = pd.DataFrame(np.random.randn(4,3), columns= ['a','b','c'])

print(df)