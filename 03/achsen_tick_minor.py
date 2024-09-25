import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()
ax.minorticks_on()  # Aktiviert Minor-Ticks

# Beispielplot
plt.plot([1, 2, 3], [4, 5, 3])
plt.show()