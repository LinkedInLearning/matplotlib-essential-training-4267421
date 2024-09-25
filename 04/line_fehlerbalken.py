
import matplotlib.pyplot as plt


x= [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024]
y= [36, 32, 35, 35, 32, 36, 32, 37, 39, 33, 30, 33, 36, 33, 35]



# Liniendiagramm erstellen
plt.plot(x, y, marker='o', linestyle='-', color='b')

# Beschriftung der Achsen
plt.xlabel('X-Achse')
plt.ylabel('Y-Achse')
plt.title('Fehlerbalken')

y_err = [0.5, 0.4, 0.3, 0.2, 0.1, 0.5, 0.4, 0.7, 0.2, 0.2,0.5, 0.4, 0.3, 0.2, 0.5]
plt.errorbar(x, y, yerr=y_err, fmt='-o', label='Mit Fehlerbalken')

# Diagramm anzeigen
plt.show()
