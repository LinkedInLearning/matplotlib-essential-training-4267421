import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# CSV-Datei einlesen
df = pd.read_csv('temperaturen.csv', delimiter=';')
# Monatsweise mittlere Temperatur berechnen
df['Durchschnitt Bodenheim'] = (df['Bodenheim Höchsttemp (°C)'] + df['Bodenheim Tiefsttemp (°C)']) / 2

# Pivot-Tabelle für die Heatmap
pivot = df.pivot_table(values='Durchschnitt Bodenheim', index='Jahr', columns='Monat')

# Heatmap erstellen
plt.figure(figsize=(10, 6))
sns.heatmap(pivot, cmap='coolwarm', annot=True, fmt=".1f", cbar_kws={'label': 'Temperatur (°C)'})
plt.title('Monatliche Durchschnittstemperaturen in Bodenheim (2010-2024)')
plt.show()
