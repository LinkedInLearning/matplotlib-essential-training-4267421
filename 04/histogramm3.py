import matplotlib.pyplot as plt
import numpy as np

# Beispiel-Daten: Normalverteilung
data = np.random.randn(10000)

# Histogramm erstellen
plt.hist(data, bins=30, color="red",  density=True,alpha=0.5)

plt.xlabel('Werte')
plt.ylabel('Häufigkeit')
plt.title('Histogramm einer Normalverteilung')
plt.show()
