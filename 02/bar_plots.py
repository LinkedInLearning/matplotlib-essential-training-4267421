import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# CSV-Daten als DataFrame laden
data = {
    "Jahr": [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    "Bodenheim Höchsttemp (°C)": [36, 32, 35, 35, 32, 36, 32, 37, 39, 33, 30, 33, 36, 33, 35],
    "Bodenheim Tiefsttemp (°C)": [-2, -10, -6, -4, -10, -7, -5, -9, -1, -6, -1, -10, -5, -5, -7],
    "Eppstein Höchsttemp (°C)": [39, 35, 39, 39, 36, 35, 33, 34, 34, 35, 35, 41, 36, 35, 41],
    "Eppstein Tiefsttemp (°C)": [-5, -7, -7, -5, -6, -3, -3, -5, -11, -4, -12, -5, -9, -9, -8],
    "Wiesbaden Höchsttemp (°C)": [41, 38, 41, 43, 34, 43, 42, 39, 36, 41, 42, 39, 40, 34, 38],
    "Wiesbaden Tiefsttemp (°C)": [-7, -2, -8, -6, -5, -3, -11, -6, -5, -9, -4, -7, -3, -7, -3],
    "Graz Höchsttemp (°C)": [44, 38, 43, 39, 44, 43, 37, 38, 43, 44, 40, 36, 41, 36, 36],
    "Graz Tiefsttemp (°C)": [-13, -11, -8, -6, -5, -7, -10, -8, -9, -6, -13, -13, -8, -4, -12],
    "Frankfurt Höchsttemp (°C)": [40, 36, 42, 36, 39, 44, 36, 39, 41, 41, 43, 36, 42, 36, 42],
    "Frankfurt Tiefsttemp (°C)": [-12, -7, -12, -14, -7, -12, -13, -14, -12, -13, -13, -9, -14, -13, -9]
}

df = pd.DataFrame(data)

# Breite der Balken und Versatz für jede Stadt
bar_width = 0.15
x = np.arange(len(df["Jahr"]))  # Positionen der Jahre auf der X-Achse

# Erstellen einer Figur mit zwei Subplots (für Höchst- und Tiefsttemperaturen)
fig, ax = plt.subplots(2, 1, figsize=(12, 10))

# Balkendiagramm für die Höchsttemperaturen
ax[0].bar(x - 2*bar_width, df["Bodenheim Höchsttemp (°C)"], bar_width, label="Bodenheim Höchsttemp", color='blue')
ax[0].bar(x - bar_width, df["Eppstein Höchsttemp (°C)"], bar_width, label="Eppstein Höchsttemp", color='green')
ax[0].bar(x, df["Wiesbaden Höchsttemp (°C)"], bar_width, label="Wiesbaden Höchsttemp", color='red')
ax[0].bar(x + bar_width, df["Graz Höchsttemp (°C)"], bar_width, label="Graz Höchsttemp", color='purple')
ax[0].bar(x + 2*bar_width, df["Frankfurt Höchsttemp (°C)"], bar_width, label="Frankfurt Höchsttemp", color='orange')

# Titel und Beschriftungen für Höchsttemperaturen
ax[0].set_title("Höchsttemperaturen in verschiedenen Städten")
ax[0].set_xlabel("Jahr")
ax[0].set_ylabel("Höchsttemperatur (°C)")
ax[0].set_xticks(x)
ax[0].set_xticklabels(df["Jahr"])
ax[0].legend()

# Balkendiagramm für die Tiefsttemperaturen
ax[1].bar(x - 2*bar_width, df["Bodenheim Tiefsttemp (°C)"], bar_width, label="Bodenheim Tiefsttemp", color='blue')
ax[1].bar(x - bar_width, df["Eppstein Tiefsttemp (°C)"], bar_width, label="Eppstein Tiefsttemp", color='green')
ax[1].bar(x, df["Wiesbaden Tiefsttemp (°C)"], bar_width, label="Wiesbaden Tiefsttemp", color='red')
ax[1].bar(x + bar_width, df["Graz Tiefsttemp (°C)"], bar_width, label="Graz Tiefsttemp", color='purple')
ax[1].bar(x + 2*bar_width, df["Frankfurt Tiefsttemp (°C)"], bar_width, label="Frankfurt Tiefsttemp", color='orange')

# Titel und Beschriftungen für Tiefsttemperaturen
ax[1].set_title("Tiefsttemperaturen in verschiedenen Städten")
ax[1].set_xlabel("Jahr")
ax[1].set_ylabel("Tiefsttemperatur (°C)")
ax[1].set_xticks(x)
ax[1].set_xticklabels(df["Jahr"])
ax[1].legend()

# Layout anpassen und Plot anzeigen
plt.tight_layout()
plt.show()
