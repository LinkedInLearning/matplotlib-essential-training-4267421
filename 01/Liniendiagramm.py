import matplotlib.pyplot as plt

# Hypothetische Temperaturen eines Tages (in °C)
stunden = list(range(24))  # Stunden von 0 bis 23 Uhr
temperaturen = [8, 7, 6, 6, 5, 4, 4, 6, 9, 12, 16, 19, 21, 22, 23, 22, 21, 18, 15, 12, 10, 9, 8, 7]

# Erstelle ein Liniendiagramm
plt.plot(stunden, temperaturen, marker='x', color='green')

# Diagramm beschriften
plt.title('Temperaturverlauf über die Stunden')
plt.xlabel('Stunden')
plt.ylabel('Temperatur (°C)')

# Diagramm anzeigen
plt.show()
