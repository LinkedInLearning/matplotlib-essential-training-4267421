import matplotlib.pyplot as plt


# Beispiel-Daten -  Hypothetische Temperaturen eines Tages (in °C)
temperaturen1 = [8, 7, 6, 6, 5, 4, 4, 6, 10, 12, 14, 15, 15, 19, 23, 22, 22, 16, 15, 12, 10, 8, 4, 2]
temperaturen2 = [2, 9, 7, 6, 8, 5, 2, 7, 9, 14, 15, 16, 17, 18, 21, 21, 21, 12, 10, 7, 6, 9, 8, 4]
temperaturen3 = [5, 7, 6, 6, 8,8, 4, 6, 9, 11, 14, 15, 15, 19, 23, 21, 21, 16, 15, 12, 10, 9, 9, 7]

stunden = list(range(24))  # Stunden von 0 bis 23 Uhr

plt.stackplot(stunden, temperaturen1, temperaturen2, temperaturen3, 
labels=['Wiesbaden', 'Graz', 'Mainz'], 
colors=['skyblue', 'lightgreen', 'lightcoral'])

plt.title('Gestapeltes Flächendiagramm')
plt.legend(loc='upper left')
plt.show()