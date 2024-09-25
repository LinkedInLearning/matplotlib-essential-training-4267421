import numpy as np
import matplotlib.pyplot as plt

# Daten generieren
x = np.linspace(0, 2 * np.pi, 100)
y1 = np.sin(x)  # Hauptachse
y2 = np.cos(x)  # Nebenachse

# Diagramm erstellen
fig, ax1 = plt.subplots()

# Hauptachse (Sinus)
ax1.plot(x, y1, 'b-', label='Sinus')
ax1.set_xlabel('x (radians)')
ax1.set_ylabel('sin(x)', color='b')
ax1.tick_params(axis='y', labelcolor='b')

# Nebenachse (Kosinus)
ax2 = ax1.twinx()  # Erstelle eine zweite y-Achse
ax2.plot(x, y2, 'r-', label='Kosinus')
ax2.set_ylabel('cos(x)', color='r')
ax2.tick_params(axis='y', labelcolor='r')

# Minor ticks aktivieren
ax2.minorticks_on()

# Gitter nur für das Nebengitter aktivieren
ax2.grid(True, which='minor')  # Zeige nur das Nebengitter (minor)

# Diagramm anpassen
plt.title('Sinus und Kosinus mit Haupt- und Nebenachsen')
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')

# Diagramm anzeigen
plt.tight_layout()
plt.show()
