import matplotlib.pyplot as plt


# Beispiel-Daten -  Hypothetische Temperaturen eines Tages (in °C)
temperaturen1 = [8, 7, 6, 6, 5, 4, 4, 6, 10, 12, 14, 15, 15, 19, 23, 22, 22, 16, 15, 12, 10, 8, 4, 2]

plt.boxplot(temperaturen1)
plt.title('Boxplot mit mehreren Gruppen')
plt.ylabel('Temperaturwerte')
plt.show()