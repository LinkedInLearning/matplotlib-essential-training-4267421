import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Schritt 1: Generiere zufällige Daten für den Wasserstand
np.random.seed(42)  # Für Reproduzierbarkeit
tage_pro_jahr = 365

# Simuliere tägliche Wasserstandswerte (in cm) für ein Jahr
# Mittelwert: 500 cm, Standardabweichung: 100 cm
wasserstand_daten = np.random.normal(loc=500, scale=100, size=tage_pro_jahr)

# Erstelle ein Datum für jeden Tag des Jahres
datum = pd.date_range(start='2023-01-01', periods=tage_pro_jahr, freq='D')

# Erstelle ein DataFrame mit den Wasserstandsdaten
df = pd.DataFrame({'Datum': datum, 'Wasserstand (cm)': wasserstand_daten})

# Schritt 2: Verarbeite die Daten
# Extrahiere die Monate aus dem Datum
df['Monat'] = df['Datum'].dt.month

# Berechne die monatlichen Höchst- und Tiefstwerte
monatsstatistik = df.groupby('Monat')['Wasserstand (cm)'].agg(['max', 'min']).reset_index()

# Schritt 3: Visualisiere die Daten
plt.figure(figsize=(10, 6))

# Scatter Plot für Höchstwerte
plt.scatter(monatsstatistik['Monat'], monatsstatistik['max'], color='blue', label='Höchststände', s=100, alpha=0.7)

# Scatter Plot für Tiefstwerte
plt.scatter(monatsstatistik['Monat'], monatsstatistik['min'], color='red', label='Tiefststände', s=100, alpha=0.7)

# Diagramm-Details
plt.title('Monatliche Höchst- und Tiefststände des Rhein-Wasserstands (2023)')
plt.xlabel('Monat')
plt.ylabel('Wasserstand (cm)')
plt.xticks(ticks=np.arange(1, 13), labels=['Jan', 'Feb', 'Mär', 'Apr', 'Mai', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dez'])
plt.grid(True)
plt.legend()

# Zeige das Diagramm
plt.show()
