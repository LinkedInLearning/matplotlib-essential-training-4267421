import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()
ax.set_ylim([-2, 10])
# Definiere feste x-Tick-Positionen
fixed_positions = [0, 2.5, 5, 7.5, 10]
ax.set_yticks(fixed_positions)
ax.set_yticklabels(['A', 'B', 'C', 'D','E'])  # Benutzerdefinierte Labels für die x-Achse


# Beispielplot
plt.plot([0,1, 2, 3,4,5,6,7,8], [7,4, 5, 3,1,4,5,1,6])
plt.show()