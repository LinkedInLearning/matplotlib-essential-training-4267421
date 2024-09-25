import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]
y3 = [2, 1,5, 1]
y4 = [6, 4, 2,1]

plt.plot(x, y1, linestyle='--', label='Gestrichelt')
plt.plot(x, y2, linestyle=':', label='Gepunktet')
plt.plot(x, y3, linestyle='-', label='Durchgezogene Linie (Standard)')
plt.plot(x, y4, linestyle='-.', label='Strich-Punkt-Linie')
plt.legend()
plt.show()