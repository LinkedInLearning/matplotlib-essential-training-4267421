import pandas as pd
import matplotlib.pyplot as plt

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

# Erstellen einer Figur mit zwei Subplots (für Höchst- und Tiefsttemperaturen)
fig, ax = plt.subplots(2, 1, figsize=(10, 8))

# Multiline-Plot für die Höchsttemperaturen
ax[0].plot(df["Jahr"], df["Bodenheim Höchsttemp (°C)"], label="Bodenheim Höchst", color='blue', marker='o')
ax[0].plot(df["Jahr"], df["Eppstein Höchsttemp (°C)"], label="Eppstein Höchsttemp", color='green', marker='o')
ax[0].plot(df["Jahr"], df["Wiesbaden Höchsttemp (°C)"], label="Wiesbaden Höchsttemp", color='red', marker='o')
ax[0].plot(df["Jahr"], df["Graz Höchsttemp (°C)"], label="Graz Höchsttemp", color='purple', marker='o')
ax[0].plot(df["Jahr"], df["Frankfurt Höchsttemp (°C)"], label="Frankfurt Höchsttemp", color='orange', marker='o')

# Titel und Beschriftungen für Höchsttemperaturen
ax[0].set_title("Höchsttemperaturen in verschiedenen Städten")
ax[0].set_xlabel("Jahr")
ax[0].set_ylabel("Höchsttemperatur (°C)")
ax[0].legend()

# Multiline-Plot für die Tiefsttemperaturen
ax[1].plot(df["Jahr"], df["Bodenheim Tiefsttemp (°C)"], label="Bodenheim Tiefsttemp", color='blue', marker='o')
ax[1].plot(df["Jahr"], df["Eppstein Tiefsttemp (°C)"], label="Eppstein Tiefsttemp", color='green', marker='o')
ax[1].plot(df["Jahr"], df["Wiesbaden Tiefsttemp (°C)"], label="Wiesbaden Tiefsttemp", color='red', marker='o')
ax[1].plot(df["Jahr"], df["Graz Tiefsttemp (°C)"], label="Graz Tiefsttemp", color='purple', marker='o')
ax[1].plot(df["Jahr"], df["Frankfurt Tiefsttemp (°C)"], label="Frankfurt Tiefsttemp", color='orange', marker='o')

# Titel und Beschriftungen für Tiefsttemperaturen
ax[1].set_title("Tiefsttemperaturen in verschiedenen Städten")
ax[1].set_xlabel("Jahr")
ax[1].set_ylabel("Tiefsttemperatur (°C)")
ax[1].legend()

# Layout anpassen und Plot anzeigen
plt.tight_layout()
plt.show()
