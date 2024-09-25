import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten
x = np.random.rand(10)  # Zufällige x-Werte
y = np.random.rand(10)  # Zufällige y-Werte

sizes = np.random.rand(10) * 1000  # Größen der Punkte (Skalierung auf größere Werte)
colors = np.random.rand(10)  # Zufällige Farben (numerisch)

# Streudiagramm erstellen
plt.scatter(x, y, s=sizes, c=colors, alpha=0.5, cmap='viridis')

# Farbskala hinzufügen
plt.colorbar()

plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Scatter Plot mit variabler Größe und Farbe')
plt.show()
