import numpy as np
import matplotlib.pyplot as plt

# Erzeugen der Daten
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))

# Erstellen des Konturdiagramms
plt.contour(X, Y, Z, levels=10)  # 10 Konturlinien
plt.colorbar()  # Farblegende
plt.title('Konturdiagramm')
plt.show()
