import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()

ax.set_xlabel('x-Achse Beschriftung')
ax.set_ylabel('y-Achse Beschriftung')
ax.xaxis.set_label_coords(0.9, 0.2)  # Position der x-Achsen-Beschriftung ändern

ax.set_title('Werte über eine Einheit', fontsize=14, fontweight='bold')


# Beispielplot
plt.plot([0,1, 2, 3,4,5,6,7,8], [7,4, 5, 3,1,4,5,1,6])
plt.show()