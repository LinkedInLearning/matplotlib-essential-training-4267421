import matplotlib.pyplot as plt

# Beispiel-Daten
x = [1, 2, 3, 4, 5]
y = [5, 4, 3, 2, 1]

# Streudiagramm erstellen
plt.scatter(x, y, s=100, marker="^")
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Einfaches Streudiagramm')
plt.show()