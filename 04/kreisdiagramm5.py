import matplotlib.pyplot as plt

# Beispiel-Daten
werte = [25, 35, 15, 25]
labels = ['Äpfel', 'Birnen', 'Kirschen', 'Bananen']
colors = ['red', '#00dd11', 'blue', 'purple']
explode = [0, 0.1, 0, 0.3]  # das zweite und vierte Segment werden hervorgehoben



# Erstellen des Kreisdiagramms
plt.pie(werte, explode=explode, labels=labels, autopct='%1.1f%%',  colors=colors, startangle=120, shadow=True)

# Titel hinzufügen und anzeigen
plt.title('Kreisdiagramm mit Schatten', loc="left")
plt.show()
