import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]

plt.plot(x, y1, color='red', label='Rot')       # Farbname
plt.plot(x, y2, color='#1f77b4', label='Blau-Ton')  # HEX-Code
plt.show()