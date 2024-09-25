import matplotlib.pyplot as plt

# Erstelle die Subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Verwende den Stil 'ggplot' für den ersten Subplot
with plt.style.context('ggplot'):
    ax1.plot([1, 2, 3], [4, 5, 6], label='Plot 1')
    ax1.set_title('ggplot Stil')
    ax1.legend()

# Verwende den Stil 'seaborn-v0_8' für den zweiten Subplot
with plt.style.context('seaborn-v0_8'):
    ax2.plot([1, 2, 3], [6, 5, 4], label='Plot 2', color='green')
    ax2.set_title('seaborn-v0_8 Stil')
    ax2.legend()

# Zeige das Diagramm an
plt.tight_layout()
plt.show()
