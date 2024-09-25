import matplotlib.pyplot as plt


# Beispiel-Daten -  Hypothetische Temperaturen eines Tages (in °C)
temperaturen1 = [8, 7, 6, 6, 5, 4, 4, 6, 10, 12, 14, 15, 15, 19, 23, 22, 22, 16, 15, 12, 10, 8, 4, 2]
temperaturen2 = [2, 9, 7, 6, 8, 5, 2, 7, 9, 14, 15, 16, 17, 18, 21, 21, 21, 12, 10, 7, 6, 9, 8, 4]
stunden = list(range(24))  # Stunden von 0 bis 23 Uhr

# Fläche zwischen zwei Kurven
plt.fill_between(stunden, temperaturen1, temperaturen2, color="green", alpha=0.8)

plt.title('Fläche zwischen zwei Linien')
plt.legend()
plt.show()