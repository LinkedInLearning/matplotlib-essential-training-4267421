import matplotlib.pyplot as plt
import numpy as np

data1 = np.random.randn(1000)
data2 = np.random.randn(1000) + 2  # Verschiebung der Normalverteilung

# Histogramm für beide Datensätze
plt.hist([data1, data2], bins=30, alpha=0.7, label=['Datensatz 1', 'Datensatz 2'])

# Legende hinzufügen
plt.legend(loc='upper right')
plt.show()
