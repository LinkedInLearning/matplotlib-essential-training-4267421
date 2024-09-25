import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()
ax.grid(True, linestyle='-', color='blue', alpha=0.3)
# Beispielplot
plt.plot([1, 2, 3], [4, 5, 3])
plt.show()