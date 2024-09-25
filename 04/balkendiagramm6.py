import matplotlib.pyplot as plt
import numpy as np

categories=["A","B","C","D"]
# Beispiel-Daten für zwei Gruppen
group1 = [3, 5, 2, 6]
group2 = [4, 7, 3, 5]

# Balkendiagramm mit gestapelten Balken
plt.bar(categories, group1, color='blue', label='Gruppe 1')
plt.bar(categories, group2, bottom=group1, color='red', label='Gruppe 2')

# Legende und Achsenbeschriftung
plt.xlabel('Kategorien')
plt.ylabel('Werte')
plt.title('Gestapeltes Balkendiagramm')
plt.legend()
plt.show()
