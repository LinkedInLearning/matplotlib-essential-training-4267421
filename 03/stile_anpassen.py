import matplotlib.pyplot as plt

# Stil 'fivethirtyeight' verwenden
plt.style.use('fivethirtyeight')
plt.rcParams['lines.linewidth'] = 1.0
plt.rcParams['axes.labelsize'] = 'large'
plt.rcParams['axes.grid'] = True
# Beispielplot
plt.plot([1, 2, 3], [4, 5, 3])
plt.show()