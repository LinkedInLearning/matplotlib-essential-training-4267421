import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Beispiel-Daten für die Animation
fig, ax = plt.subplots()
x = np.linspace(0, 2 * np.pi, 100)
line, = ax.plot(x, np.sin(x))

# Funktion zur Aktualisierung der Daten für jedes Frame
def update(frame):
    line.set_ydata(np.sin(x + frame / 10.0))  # Verschieben der Sinuskurve
    return line,

# Animation erstellen
ani = FuncAnimation(fig, update, frames=100, interval=50, blit=True)

# Animation anzeigen
plt.show()
