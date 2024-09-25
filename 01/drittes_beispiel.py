import matplotlib.pyplot as plt
import numpy as np

# Hypothetische Temperaturdaten für zwei Orte
stunden = np.arange(0, 24, 1)  # Stunden von 0 bis 23 Uhr
temperaturen_ort1 = [8, 7, 6, 6, 5, 4, 4, 6, 9, 12, 16, 19, 21, 22, 23, 22, 21, 18, 15, 12, 10, 9, 8, 7]
temperaturen_ort2 = [10, 9, 8, 8, 7, 6, 6, 8, 11, 15, 18, 21, 23, 24, 25, 24, 23, 20, 17, 14, 12, 11, 10, 9]

# Balkenbreite und Positionen für die Balkendiagramme
bar_width = 0.35
index = np.arange(len(stunden))

# Erstellung des Plots
plt.figure(figsize=(12, 6))

# Balkendiagramme für die beiden Orte
plt.bar(index, temperaturen_ort1, bar_width, label='Eppstein', color='b')
plt.bar(index + bar_width, temperaturen_ort2, bar_width, label='Bodenheim', color='g')

# Titel und Achsenbeschriftung
plt.title('Temperaturverlauf eines Tages in zwei Orten in Deutschland', fontsize=16)
plt.xlabel('Stunden', fontsize=12)
plt.ylabel('Temperatur (°C)', fontsize=12)

# Stunden auf der x-Achse
plt.xticks(index + bar_width / 2, stunden)

# Gitter hinzufügen
plt.grid(True)

# Legende anzeigen
plt.legend()

# Zeige den Plot
plt.show()
