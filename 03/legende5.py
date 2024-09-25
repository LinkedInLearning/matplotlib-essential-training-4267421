import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.plot([4, 2, 1])
plt.legend(['Linie 1', 'Linie 2'],fontsize=12, title='Legende Titel')  # angepasste, manuelle Legende für beide Linien aufgrund label
plt.show()