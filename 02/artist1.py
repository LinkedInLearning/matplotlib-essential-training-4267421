import matplotlib.pyplot as plt

# Erstelle eine leere Figur mit der figure-Methode
fig = plt.figure(figsize=(6, 4))

# Füge eine Achse hinzu mit add_axes([left, bottom, width, height])
# Die Werte sind relative Koordinaten zwischen 0 und 1
ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])  # [left, bottom, width, height]

# Zeichne eine Linie (Line2D Artist)
line, = ax.plot([1, 2, 3], [1, 8, 27],marker='o', label="3er-Potenzen", color='red')

# Füge Titel und Achsenbeschriftungen hinzu (Text Artists)
ax.set_title('Plot mit figure() und add_axes() und Artists')  # Text Artist
ax.set_xlabel('X-Achse')  # Text Artist
ax.set_ylabel('Y-Achse')  # Text Artist

# Füge eine Legende hinzu (Legend Artist)
legend = ax.legend()

# Überprüfe den Typ von "line" (es ist ein Artist)
print(f"Der Typ von 'line' ist: {type(line)}")  # Zeigt, dass es ein Line2D-Artist ist

# Zeige die Figur an
plt.show()