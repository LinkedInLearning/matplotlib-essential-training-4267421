import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Beispiel-Daten für das 3D-Diagramm
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Erstellen von Datenpunkten
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.sin(np.sqrt(x**2 + y**2))

# 3D-Oberflächenplot
ax.plot_surface(x, y, z, cmap='viridis')

# Beschriftungen der Achsen
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')
ax.set_zlabel('Z-Achse')

# Anzeige des Plots
plt.show()
