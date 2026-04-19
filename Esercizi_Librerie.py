import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Crea una serie di 30 date consecutive
# Partiamo da oggi (puoi cambiare start con una data specifica)
date_index = pd.date_range(start=pd.Timestamp.today().normalize(), periods=30, freq='D') #freq = D => giornaliera

# 2. Genera valori casuali associati alle date
# Usiamo numpy per creare 30 valori casuali 
valori = np.random.randn(30)  

# 3. Crea un DataFrame con indice temporale
df = pd.DataFrame({'valore': valori}, index=date_index)

print(df)

# 4. Fai un grafico a linea con i valori nel tempo
plt.figure(figsize=(10, 4))
plt.plot(df.index, df['valore'], marker='o', linestyle='-')
plt.title('Valori casuali su 30 giorni consecutivi')
plt.xlabel('Data')
plt.ylabel('Valore')
plt.grid(True)
plt.tight_layout()
plt.show()
