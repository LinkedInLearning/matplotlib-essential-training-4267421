import matplotlib.pyplot as plt

# Einfache Plot-Erstellung ohne explizites Figure-Objekt
plt.plot([1, 2, 3], [1, 4, 9], label='Quadrat')
plt.title('Einfacher Plot ohne Figure')
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')

# Zeige das Diagramm an
plt.show()
