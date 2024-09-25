import matplotlib.pyplot as plt


# Beispiel-Daten -  Hypothetische Temperaturen eines Tages (in °C)
temperaturen1 = [8, 7, 6, 6, 5, 4, 4, 6, 10, 12, 14, 15, 15, 19, 23, 22, 22, 16, 15, 12, 10, 8, 4, 2]
temperaturen2 = [2, 9, 7, 6, 8, 5, 2, 7, 9, 14, 15, 16, 17, 18, 21, 21, 21, 12, 10, 7, 6, 9, 8, 4]
temperaturen3 = [5, 7, 6, 6, 8,8, 4, 6, 9, 11, 14, 15, 15, 19, 23, 21, 21, 16, 15, 12, 10, 9, 9, 7]

stunden = list(range(24))  # Stunden von 0 bis 23 Uhr

plt.fill_between(stunden, temperaturen1, alpha=0.5)
plt.fill_between(stunden, temperaturen2, alpha=0.5)
plt.fill_between(stunden, temperaturen3, alpha=0.5)

plt.title('Mehrere Flächen in einem Diagramm')
plt.show()