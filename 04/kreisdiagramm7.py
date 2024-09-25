import matplotlib.pyplot as plt
# Beispiel-Daten für zwei Ringe
outer_sizes = [30, 20, 50]
inner_sizes = [15, 15, 20, 30, 10, 10]

# Erstes (äußeres) Ringdiagramm
plt.pie(outer_sizes, radius=1, labels=['A', 'B', 'C'], autopct='%1.1f%%',
        wedgeprops=dict(width=0.3, edgecolor='w'))

# Zweites (inneres) Ringdiagramm
plt.pie(inner_sizes, radius=0.4, labels=['A1', 'A2', 'B1', 'C1', 'C2', 'C3'], autopct='%1.1f%%',
        wedgeprops=dict(width=0.3, edgecolor='w'))

plt.title('Verschachteltes Donut-Diagramm')
plt.show()

