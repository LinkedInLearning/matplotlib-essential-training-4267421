import matplotlib.pyplot as plt

# Beispiel-Daten
werte = [25, 35, 15, 25]
labels = ['Äpfel', 'Birnen', 'Kirschen', 'Bananen']
colors = ['red', 'green', 'blue', 'purple']
explode = [0, 0.1, 0, 0]  # Nur das zweite Segment wird hervorgehoben



# Erstellen des Kreisdiagramms
plt.pie(werte, explode=explode, labels=labels, autopct='%1.1f%%',  colors=colors)

# Titel hinzufügen und anzeigen
plt.title('Einfaches Kreisdiagramm')
plt.show()
