import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()
ax.grid(True, axis='y')  # Raster nur auf der y-Achse
# Beispielplot
plt.plot([1, 2, 3], [4, 5, 3])
plt.show()