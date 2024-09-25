import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten: Normalverteilung
temperaturen = [8, 7, 6, 6, 5, 4, 4, 6, 9, 12, 16, 19, 21, 22, 23, 22, 21, 18, 15, 12, 10, 9, 8, 7]


# Histogramm erstellen
plt.hist(temperaturen)

plt.xlabel('Temperaturmesswerte über den Tag')
plt.ylabel('Häufigkeit')
plt.title('Histogramm der Verteilung')
plt.show()
