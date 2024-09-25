import matplotlib.pyplot as plt

# Erstelle eine neue Figur mit 4 Subplots (2 Zeilen, 2 Spalten)
fig, axs = plt.subplots(2, 2, figsize=(10, 8))

# Plot 1: Quadratfunktion
axs[0, 0].plot([1, 2, 3], [1, 4, 9], label="Quadrat", color='blue')
axs[0, 0].set_title('Quadrat')
axs[0, 0].legend()

# Plot 2: Lineare Funktion
axs[0, 1].plot([1, 2, 3], [1, 2, 3], label="Linear", color='green')
axs[0, 1].set_title('Linear')
axs[0, 1].legend()

# Plot 3: Kubische Funktion
axs[1, 0].plot([1, 2, 3], [1, 8, 27], label="Kubisch", color='red')
axs[1, 0].set_title('Kubisch')
axs[1, 0].legend()

# Plot 4: Exponentielle Funktion
axs[1, 1].plot([1, 2, 3], [2, 4, 8], label="Exponentiell", color='purple')
axs[1, 1].set_title('Exponentiell')
axs[1, 1].legend()

# Layout-Anpassung, um Überlappungen zu vermeiden
plt.tight_layout()

# Zeige die Figur an
plt.show()
