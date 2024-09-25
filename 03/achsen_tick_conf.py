import matplotlib.pyplot as plt
# Diagramm erstellen
fig, ax = plt.subplots()
ax.tick_params(axis='both', which='major', length=20, direction='inout')


# Beispielplot
plt.plot([1, 2, 3], [4, 5, 3])
plt.show()