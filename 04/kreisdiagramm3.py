import matplotlib.pyplot as plt

# Beispiel-Daten
werte = [25, 35, 15, 25]
labels = ['Äpfel', 'Birnen', 'Kirschen', 'Bananen']
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']


# Erstellen des Kreisdiagramms
plt.pie(werte, labels=labels, autopct='%1.1f%%',  colors=colors)

# Titel hinzufügen und anzeigen
plt.title('Einfaches Kreisdiagramm')
plt.show()
