import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV-Datei einlesen
df = pd.read_csv('temperaturen.csv', delimiter=';')
# Datumsspalte erstellen: Jahr und Monat kombinieren
df['Datum'] = pd.to_datetime(df[['Jahr', 'Monat']].astype(str).agg('-'.join, axis=1), format='%Y-%m')

# Liste der Orte ermitteln (Annahme: Orte beginnen nach den Spalten 'Jahr' und 'Monat')
orte = df.columns[3:-1]

# Heatmap-Daten zusammenstellen (wir transponieren, damit Orte auf der Y-Achse liegen)
heatmap_data = df[orte].transpose()

# Heatmap erstellen
plt.figure(figsize=(10, 6))

# Benutze imshow von matplotlib für die Heatmap
plt.imshow(heatmap_data, aspect='auto', cmap='hot', interpolation='nearest')

# Beschriftungen hinzufügen
plt.colorbar(label='Messwerte')
plt.xticks(ticks=np.arange(len(df['Datum'])), labels=df['Datum'].dt.strftime('%Y-%m'), rotation=90)
plt.yticks(ticks=np.arange(len(orte)), labels=orte)

# Achsen beschriften und Titel hinzufügen
plt.xlabel('Datum')
plt.ylabel('Orte')
plt.title('Heatmap der Messwerte über Zeit und Orte')

# Layout anpassen und Diagramm anzeigen
plt.tight_layout()
plt.show()