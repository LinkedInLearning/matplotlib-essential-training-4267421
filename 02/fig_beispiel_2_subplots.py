import matplotlib.pyplot as plt

# Erstelle eine neue Figur mit zwei Subplots (1 Zeile, 2 Spalten)
fig, ax = plt.subplots(1, 2, figsize=(10, 5))

# Erstes Diagramm in der linken Achse
ax[0].plot([1, 2, 3], [1, 4, 9], label="Quadrat")
ax[0].set_title('Linkes Diagramm')
ax[0].legend()

# Zweites Diagramm in der rechten Achse
ax[1].plot([1, 2, 3], [1, 2, 3], label="Linear", color='red')
ax[1].set_title('Rechtes Diagramm')
ax[1].legend()

# Zeige die Figur an
plt.show()
