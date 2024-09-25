import matplotlib.pyplot as plt

# Beispiel-Daten
werte = [25, 35, 15, 25]
labels = ['Äpfel', 'Birnen', 'Kirschen', 'Bananen']
colors = ['red', '#00dd11', 'blue', 'purple']
explode = [0, 0.1, 0, 0.3]  # das zweite und vierte Segment werden hervorgehoben



# Erstellen des Kreisdiagramms
plt.pie(werte, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops={'width': 0.4})

plt.title('Donut-Diagramm')

plt.show()
