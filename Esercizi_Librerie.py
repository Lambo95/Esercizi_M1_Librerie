import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 1. Crea una serie di 30 date consecutive
# Partiamo da oggi 
date_index = pd.date_range(start=pd.Timestamp.today().normalize(), periods=30, freq='D') #freq = D => giornaliera

# 2. Genera valori casuali associati alle date
# Usiamo numpy per creare 30 valori casuali 
valori = np.random.randn(30)  

# 3. Crea un DataFrame con indice temporale
df = pd.DataFrame({'valore': valori}, index=date_index)

print(df)

# 4. Grafico a linea con i valori nel tempo
plt.figure(figsize=(10, 4))
plt.plot(df.index, df['valore'], marker='o', linestyle='-')
plt.title('Valori casuali su 30 giorni consecutivi')
plt.xlabel('Data')
plt.ylabel('Valore')
plt.grid(True)
plt.tight_layout()
plt.show()


""" Creazione e Stampa dell'Array
Generiamo dati per sei studenti in cinque materie.
Creiamo una matrice 6x5 con valori casuali tra 10 e 100.
Stampiamo i dati originali. """

""" dati = np.random.randint(10, 100, size=(6, 5))  # 6 righe (studenti) x 5 colonne (voti)
print("Dati originali:\n", dati) """

""" 
Analisi dell'Array
Utilizziamo shape per determinare le dimensioni dell'array.
Controlliamo il tipo di dati con dtype. """

""" print(dati.shape)
print(dati.dtype)
 """
""" Indicizzazione e Slicing
Accediamo a singole righe e colonne.
Effettuiamo slicing per creare sub-matrici.
Differenziamo tra view e copy per capire le modifiche sugli array. """

""" print("\nPrima riga:", dati[0])
print("Prima colonna:", dati[:, 0])
print("Sub-matrice (prime 2 righe, prime 3 colonne):\n", dati[:2, :3])

view = dati[:2, :2]
copy = dati[:2, :2].copy()
view[0, 0] = 999
print("\nDopo modifica della view:\n", dati)
print("La copy resta invariata:\n", copy)
 """
""" Reshape e Iterazione
Ristrutturiamo l'array in una forma differente.
Utilizziamo nditer per iterare su ogni elemento """

""" reshaped = dati.reshape(3, 10)
print("\nArray reshaped (3x10):\n", reshaped)

print("\nIterazione su ogni elemento con nditer:")
for x in np.nditer(dati):
    print(int(x), end=" ")
print()
 """
""" Concatenazione e Divisione
Aggiungiamo nuove colonne simulando materie extra.
Dividiamo l'array in blocchi. """

""" extra = np.random.randint(10, 100, size=(6, 1))
unito = np.hstack((dati, extra))
print("\nArray unito con nuove colonne:\n", unito)

split = np.hsplit(unito, 2)
print("\nArray diviso in due blocchi:\n", split[0], "\n", split[1])
 """
""" Filtraggio e Ordinamento
Filtriamo i valori maggiori di 50.
Ordiniamo le righe."""
""" mask = dati > 50
print("\nValori > 50:\n", dati[mask])

ordinati = np.sort(dati, axis=1)
print("\nOgni riga ordinata:\n", ordinati) """


"""Uso di UFUNC
Applichiamo funzioni universali per calcolare le radici quadrate di ogni elemento. """
""" radici = np.sqrt(dati)
print("\nRadici quadrate di ogni elemento:\n", radici)

print("\nMedia per colonna:", np.mean(dati, axis=0))
print("Deviazione standard totale:", np.std(dati)) """ 