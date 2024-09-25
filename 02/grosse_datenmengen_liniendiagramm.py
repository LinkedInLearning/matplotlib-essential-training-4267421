import pandas as pd
import matplotlib.pyplot as plt

# CSV-Datei einlesen
df = pd.read_csv('temperaturen.csv', delimiter=';')
print(df.columns)
# Zeitstempel (Jahr-Monat) als neue Spalte hinzufügen
df['Datum'] = pd.to_datetime(df[['Jahr', 'Monat']].astype(str).agg('-'.join, axis=1), format='%Y-%m')
# Liste der Orte ermitteln (davon gehe ich aus, dass die Orte Spaltennamen sind)
orte = df.columns[3:-1]  # Die Annahme: Nach Jahr und Monat folgen die Orte bis zur letzten Spalte

# Plotten der Daten für jeden Ort
plt.figure(figsize=(14, 6))

for ort in orte:
    plt.plot(df['Datum'], df[ort], label=ort)
plt.title('Höchst- und Tiefsttemperaturen in verschiedenen Orten in allen Monaten von 2010-2024')
plt.xlabel('Jahr')
plt.ylabel('Temperatur (°C)')
plt.legend()
plt.grid(True)
plt.show()
