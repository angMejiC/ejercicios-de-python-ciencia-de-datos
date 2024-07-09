import pandas as pd

data = {'NOMBRES':['maria','jose','david','ivan'],
        'CARRERA': ['auditoria','informatica','derecho','idiomas'],
        'CORREO':['maria@gmail.com','jose@gmail.com','david@gmail.com','ivan@gmail.com']}

studens =pd.DataFrame(data)

print(studens)
