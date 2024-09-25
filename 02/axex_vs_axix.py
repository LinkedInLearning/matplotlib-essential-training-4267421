import matplotlib.pyplot as plt
import numpy as np

# Erstellen von Daten
x = np.linspace(0, 10, 100)  # 100 Werte von 0 bis 10
y = np.cos(x)                 # Cosinusfunktion

# Erstellen einer Figur und einer Achse
fig, ax = plt.subplots()      # 'fig' ist die Figur, 'ax' ist die Achse (Axes)

# Plotten der Daten
ax.plot(x, y, label='cosinus(x)') # Plotte cos(x) auf der Achse 'ax'

# Anpassung der Achsen
ax.set_title('Cosinusfunktion')  # Titel für die Achse
ax.set_xlabel('x-Werte')         # Beschriftung der X-Achse
ax.set_ylabel('cos(x)')          # Beschriftung der Y-Achse

# Hinzufügen einer Legende
ax.legend()

# Anpassen der Y-Achse
ax.set_ylim(-1.5, 1.5)         # Setzt die Grenzen der Y-Achse

# Ausgabe der Typen 
print(f"Der Typ von fig: {type(fig)},\nax:  {type(ax)} ") 


# Anzeigen des Plots
plt.show()

print(f"Der Typ von ax.xaxis: {type(ax.xaxis)}, Wert von ax.xaxis:  {ax.xaxis} ")
print(f"Der Typ von ax.yaxis: {type(ax.yaxis)}, Wert von ax.yaxis:  {ax.yaxis} ") 
