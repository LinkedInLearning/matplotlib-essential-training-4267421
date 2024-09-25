import matplotlib.pyplot as plt
import threading
import numpy as np

# Berechnungen in einem separaten Thread ausführen
def compute_data():
    # Beispiel: Erzeugen von Daten
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    return x, y

def plot_data(x, y):
    plt.plot(x, y)
    plt.show()

# Hauptthread für Matplotlib verwenden
def main():
    # Daten in einem separaten Thread berechnen
    thread = threading.Thread(target=lambda: plot_data(*compute_data()))
    thread.start()
    thread.join()

main()
