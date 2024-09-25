import matplotlib.pyplot as plt
plt.plot([1, 2, 3])
plt.plot([3, 2, 1], label='Linie 2')
plt.legend()  # automatische Legende aufgrund label - nur 2. Linie bekommt Legende
plt.show()