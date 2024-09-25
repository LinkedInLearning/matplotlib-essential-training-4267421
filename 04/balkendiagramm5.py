import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten -  Hypothetische Temperaturen eines Tages (in °C)
stunden = np.arange(24)  # Stunden von 0 bis 23 Uhr
temperaturen1 = [8, 7, 6, 6, 5, 4, 4, 6, 10, 12, 14, 15, 15, 19, 23, 22, 22, 16, 15, 12, 10, 8, 4, 2]
temperaturen2 = [2, 7, 7, 6, 5, 5, 4, 7, 9, 14, 15, 16, 17, 18, 21, 21, 21, 12, 10, 7, 6, 9, 8, 4]
temperaturen3 = [5, 7, 6, 6, 8,8, 4, 6, 9, 11, 14, 15, 15, 19, 23, 21, 21, 16, 15, 12, 10, 9, 9, 7]
bar_width = 0.35  # Breite der Balken

# Vertikales Balkendiagramm
plt.bar(stunden, temperaturen1,bar_width, label='Graz')
plt.bar(stunden+bar_width, temperaturen2,bar_width, label='Eppstein')
plt.bar(stunden+(bar_width*2), temperaturen3,bar_width, label='Bodenheim')
plt.xlabel('Stunden')
plt.ylabel('Temperaturen')
plt.title('Mehrere Balken')
plt.show()
