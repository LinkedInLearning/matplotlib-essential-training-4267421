import matplotlib.pyplot as plt

# Beispiel-Daten
werte = [25, 35, 15, 25]
labels = ['Äpfel', 'Birnen', 'Kirschen', 'Bananen']

# Erstellen des Kreisdiagramms
plt.pie(werte, labels=labels, autopct='%1.1f%%', startangle=45)

# Titel hinzufügen und anzeigen
plt.title('Einfaches Kreisdiagramm')
plt.show()
