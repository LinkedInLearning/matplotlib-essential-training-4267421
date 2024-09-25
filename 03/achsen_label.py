import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()
ax.set_xlabel('x-Achse Beschriftung')
ax.set_ylabel('y-Achse Beschriftung')
# Beispielplot
plt.plot([1, 2, 3], [4, 5, 3])
plt.show()