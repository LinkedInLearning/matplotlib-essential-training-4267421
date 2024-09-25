
import matplotlib.pyplot as plt


x= [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
y= [36, 32, 35, 35, 32, 36, 32, 37, 39, 33, 30, 33, 36, 33, 35]



# Liniendiagramm erstellen
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Beschriftung der Achsen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Gefüllter Bereich unter der Linie')

plt.fill_between(x, y, color='blue', alpha=0.2)
# Diagramm anzeigen
plt.show()
