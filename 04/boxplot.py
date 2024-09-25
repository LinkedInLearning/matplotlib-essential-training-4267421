import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei einlesen
df = pd.read_csv('temperaturen.csv', delimiter=';')
data = [df['Bodenheim Höchsttemp (°C)'], df['Eppstein Höchsttemp (°C)'], df['Wiesbaden Höchsttemp (°C)'], 
        df['Graz Höchsttemp (°C)'], df['Frankfurt Höchsttemp (°C)']]

plt.boxplot(data, labels=['Bodenheim', 'Eppstein', 'Wiesbaden', 'Graz', 'Frankfurt'])
plt.title('Verteilung der Höchsttemperaturen (2010-2024)')
plt.ylabel('Temperatur (°C)')
plt.grid(True)
plt.show()
