import matplotlib.pyplot as plt
plt.plot([1, 2, 3], label='Linie 1')
plt.plot([4, 2, 1], label='Linie 2')
plt.legend(fontsize=12, title='Legende Titel')  # angepasste, automatische Legende für beide Linien aufgrund label
plt.show()