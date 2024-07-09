import pandas as pd
import matplotlib.pyplot as plt

# Datos proporcionados
datos = """Tipo de Préstamo,Fecha,Prestamo_banco,Interes_mensual,Cota_mensual,Nº_Cotas,Total_interes,Total_deuda,No_abono,Abonando,Ahorrado,cadena,P_Mes
Banco,02/02/24,20000000,0.0287,995000,48,27552000,47552000,,,,,
Banco,02/03/24,,,995000,47,,46557000,,,,,
Banco,02/04/24,,,995000,46,,45562000,,,,800000,1795000
Banco,02/05/24,,,995000,45,,44567000,,,,800000,1795000
Banco,02/06/24,,,995000,44,,43572000,,,,800000,1795000
Abono_capital,02/07/24,8000000,0.0287,623469.76744186052,43,14809200,26809200,8995000,,,800000,1795000
Banco,02/08/24,12000000,,623470,42,,26185730,,,,800000,1423470
Banco,02/09/24,,,623470,41,,25562260,,,,800000,1423470
Banco,02/10/24,,,623470,40,,24938790,,,,800000,1423470
Banco,02/11/24,,,623470,39,,24315320,,,,800000,1423470
Banco,02/12/24,,,623470,38,,23691850,10945000,9087350,1857650,800000,1423470
Ah_Cot,,,,,,,Ah_Cot,371530
Prestamo_juan,Fecha,Prestamo_banco,Interes_mensual,Cota_mensual,Nº_Cotas,Total_interes,Total_deuda,G_Prestamo,Abonado,Ahorrado,patrimonio,-371530
Banco,02/02/24,20000000,0.0287,995000,48,27552000,47552000,,,,,1795000,"""

# Convertir los datos en un DataFrame
df = pd.read_csv(pd.compat.StringIO(datos))

# Filtrar solo las filas correspondientes a préstamos bancarios
df_banco = df[df['Tipo de Préstamo'] == 'Banco']

# Convertir la columna 'Fecha' a tipo datetime
df_banco['Fecha'] = pd.to_datetime(df_banco['Fecha'])

# Ordenar el DataFrame por fecha
df_banco = df_banco.sort_values(by='Fecha')

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(df_banco['Fecha'], df_banco['Total_deuda'], marker='o', linestyle='-', color='blue', label='Banco')

# Resaltar los abonos de capital
abonos_capital = df[df['Tipo de Préstamo'] == 'Abono_capital']
plt.scatter(abonos_capital['Fecha'], abonos_capital['Total_deuda'], color='red', label='Abono de capital')

plt.title('Evolución de la deuda total')
plt.xlabel('Fecha')
plt.ylabel('Deuda Total')
plt.grid(True)
plt.xticks(rotation=45)  # Rotar etiquetas del eje x para mejor visualización
plt.legend()
plt.tight_layout()
plt.show()
