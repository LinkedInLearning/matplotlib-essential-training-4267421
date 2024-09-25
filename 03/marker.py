import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]
y3 = [2, 1,5, 1]
y4 = [6, 4, 2,1]
y5 = [5, 8,5, 2]
y6 = [6, 0, 4,1]

plt.plot(x, y1, marker='o', label='Kreise')  
plt.plot(x, y2, marker='s', label='Quadrate')  
plt.plot(x, y3, marker='*', label='Stern')  
plt.plot(x, y4, marker='+', label='Pluszeichen')  
plt.plot(x, y5, marker='D', label='Diamant')  
plt.plot(x, y6, marker='X', label='X')  
plt.legend()
plt.show()