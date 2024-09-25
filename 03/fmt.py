import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y1 = [1, 4, 9, 16]
y2 = [1, 2, 3, 4]
y3 = [2, 1,5, 1]
y4 = [6, 4, 2,1]
y5 = [5, 8,5, 2]
y6 = [6, 0, 4,1]

plt.plot(x, y1, 'o-r')  # Marker 'o', Farbe 'r' (rot), durchgezogene Linie '-'
plt.plot(x, y2, '--b')  # Gestrichelte Linie '--', Farbe 'b' (blau)  
plt.plot(x, y3, ':gx')  # Gepunktete Linie ':', Farbe 'g' (grün), Marker 'x' (Kreuze) 
plt.plot(x, y4, '--g')  # Gestrichelte grüne Linie 
plt.plot(x, y5,  '-.m')  # Strich-Punkt-Linie in Magenta  
plt.plot(x, y6, '*:r')  # Sterne '*' als Marker, rote gepunktete Linie ':'  
plt.legend()
plt.show()