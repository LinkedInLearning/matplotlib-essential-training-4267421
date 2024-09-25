import matplotlib.pyplot as plt

# Beispiel-Daten -  Hypothetische Temperaturen eines Tages (in °C)
stunden = list(range(24))  # Stunden von 0 bis 23 Uhr
temperaturen = [8, 7, 6, 6, 5, 4, 4, 6, 9, 12, 14, 15, 15, 19, 23, 21, 21, 16, 15, 12, 10, 9, 8, 7]
errors = [0.5, 1.0, 0.2, 0.8,0.5, 1.0, 0.2, 0.8,0.5, 1.0, 0.2, 0.8,0.5, 1.0, 0.2, 0.8,0.5, 1.0, 0.2, 0.8,0.5, 1.0, 0.2, 0.8]
# Vertikales Balkendiagramm
plt.bar(stunden, temperaturen, yerr=errors, capsize=5, color='orange', edgecolor='green', linewidth=5, alpha=0.4)
plt.xlabel('Stunden')
plt.ylabel('Temperaturen')
plt.title('Einfaches Balkendiagramm')
plt.show()
