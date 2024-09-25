import matplotlib.pyplot as plt

# Erstelle eine neue Figur
fig, ax = plt.subplots(figsize=(6, 4))

# Plot-Daten
ax.plot([1, 2, 3], [1, 4, 9], label="Quadrat")

# Hinzufügen von Titeln und Legenden
ax.set_title('Einzelner Subplot')
ax.set_xlabel('X-Achse')
ax.set_ylabel('Y-Achse')
ax.legend()

# Zeige die Figur an
plt.show()
