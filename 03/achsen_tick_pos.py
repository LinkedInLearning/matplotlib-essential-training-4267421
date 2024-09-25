import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()
ax.set_xticks([1.1, 1.2, 3])  # Manuelle Positionierung der Ticks
ax.set_yticks([4, 4.7, 4.9,6.1])
# Beispielplot
plt.plot([1, 2, 3], [4, 5, 3])
plt.show()