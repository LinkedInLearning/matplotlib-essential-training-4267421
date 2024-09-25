import matplotlib.pyplot as plt

# Hypothetische Temperaturen eines Tages (in °C)
stunden = list(range(24))  # Stunden von 0 bis 23 Uhr
temperaturen = [8, 7, 6, 6, 5, 4, 4, 6, 9, 12, 16, 19, 21, 22, 23, 22, 21, 18, 15, 12, 10, 9, 8, 7]

# Erstellung des Plots
plt.figure(figsize=(10, 5))
plt.plot(stunden, temperaturen, marker='o', linestyle='-', color='b')

# Titel und Achsenbeschriftung
plt.title('Temperaturverlauf eines Tages in Eppstein', fontsize=16)
plt.xlabel('Stunden', fontsize=12)
plt.ylabel('Temperatur (°C)', fontsize=12)

# Gitter hinzufügen
plt.grid(True)

# Achsenbereiche anpassen
plt.xticks(stunden)  # Stunden als x-Achse
plt.yticks(range(0, 26, 2))  # Temperatur von 0°C bis 24°C

# Zeige den Plot
plt.show()
