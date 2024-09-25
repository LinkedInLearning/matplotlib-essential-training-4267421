import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten: Normalverteilung
data = np.random.randn(10000)

# Histogramm erstellen
plt.hist(data, bins=30, color="green", alpha=0.3, cumulative=True)

plt.xlabel('Werte')
plt.ylabel('Häufigkeit')
plt.title('Kumulierte Verteilung')
plt.show()
