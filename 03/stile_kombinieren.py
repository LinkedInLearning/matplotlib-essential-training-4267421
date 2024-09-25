import matplotlib.pyplot as plt

# Stil kombinieren: Stile werden in der Reihenfolge angewendet
plt.style.use(['seaborn-v0_8-darkgrid','ggplot', 'tableau-colorblind10'])

# Beispielplot
plt.plot([1, 2, 3], [4, 5, 3])
plt.show()