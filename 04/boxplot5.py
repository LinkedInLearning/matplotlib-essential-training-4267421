import matplotlib.pyplot as plt
# Farben und Darstellungen anpassen
boxprops = dict(facecolor='lightblue', color='blue')
medianprops = dict(color='red', linewidth=4)
meanprops = dict(marker='o', markerfacecolor='yellow', markeredgecolor='black', markersize=12)


# Beispiel-Daten -  Hypothetische Temperaturen eines Tages (in °C)
temperaturen1 = [8, 7, 6, 6, 5, 4, 4, 6, 10, 12, 14, 15, 15, 19, 23, 22, 22, 16, 15, 12, 10, 8, 4, 2]
temperaturen2 = [2, 7, 7, 6, 5, 5, 4, 7, 9, 14, 15, 16, 17, 18, 21, 21, 21, 12, 10, 7, 6, 9, 8, 4]
temperaturen3 = [5, 7, 6, 8, 8,8, 4, 6, 9, 41, 14, 15, 15, 19, 23, 21, 21, 16, 15, 12, 10, 9, 9, 7]

plt.boxplot([temperaturen1,temperaturen2,temperaturen3],
tick_labels=['Eppstein', 'Bodenheim','Frankfurt'],
patch_artist=True, boxprops=boxprops, medianprops=medianprops, showmeans=True, meanprops=meanprops)
plt.title('Angepasstes Boxplot')
plt.ylabel('Temperaturwerte')
plt.show()