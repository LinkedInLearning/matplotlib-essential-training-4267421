import matplotlib.pyplot as plt
import numpy as np

# Erstelle eine Figur und Achsen (Container-Artists)
fig, ax = plt.subplots(figsize=(8, 6))

# 1. Line2D Artist: Ein einfacher Plot
x = np.linspace(0, 10, 100)
y = x ** 2
line, = ax.plot(x, y, label="Quadrat", color='blue', linewidth=2)

# 2. Scatter Collection Artist: Eine Punktwolke (Scatterplot)
x_scatter = np.random.rand(50) * 10
y_scatter = np.random.rand(50) * 100
scatter = ax.scatter(x_scatter, y_scatter, color='red', label='Punkte')

# 3. Patch Artist: Ein Kreis in der Grafik
from matplotlib.patches import Circle
circle = Circle((5, 50), 2, color='green', fill=True, label='Kreis')
ax.add_patch(circle)

# 4. Text Artist: Titel, Achsenbeschriftungen und Anmerkung
ax.set_title('Beispiel für verschiedene Artists', fontsize=14)  # Titel-Text
ax.set_xlabel('X-Achse', fontsize=12)  # X-Achse Text
ax.set_ylabel('Y-Achse', fontsize=12)  # Y-Achse Text
ax.text(7, 80, 'Text Annotation', color='purple', fontsize=12)  # Anmerkung im Plot

# 5. Legend Artist: Eine Legende für die verschiedenen Elemente
legend = ax.legend()

# Layout und Anzeige
plt.grid(True)
plt.show()
