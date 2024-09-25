import matplotlib.pyplot as plt

# Hypothetische Temperaturen eines Tages (in °C)

temperaturen = [8, 7, 6, 6, 5, 4, 4, 6, 9, 12, 16, 19, 21, 22, 23, 22, 21, 18, 15, 12, 10, 9, 8, 7]

# Erstelle ein Kreisdiagramm

plt.pie(temperaturen)
# Diagramm beschriften
plt.title('Temperaturen im Vergleich')
plt.xlabel('Temperatur (°C)')

# Diagramm anzeigen
plt.show()
