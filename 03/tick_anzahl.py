import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()
from matplotlib.ticker import MaxNLocator
ax.yaxis.set_major_locator(MaxNLocator(5))  # Zeigt maximal 5 Haupt-Ticks an



# Beispielplot
plt.plot([1, 2, 3,4,5,6,7,8], [4, 5, 3,10,4,5,1,6])
plt.show()