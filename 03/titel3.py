import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()
ax.set_title('Absolut wichtiger Titel',loc="left")

# Beispielplot
plt.plot([0,1, 2, 3,4,5,6,7,8], [7,4, 5, 3,1,4,5,1,6])
plt.show()