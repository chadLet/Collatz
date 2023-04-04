# Import de matplotlib
import matplotlib.pyplot as plt

# Entrée du nombre à évaluer
n = int(input('Entrez un nombre: '))

y = [n]
x = []

# Calcul des valeurs de y en fonction de n
while n != 1:
    if n % 2 == 0:
        n = int(n/2)
    else:
        n = 3*n+1
    y.append(n)

# Associe une valeur de x à chaques valeurs de y
for i in range(len(y)):
    x.append(i)

# Tracer de la fonction
plt.grid(visible=True, which='major', axis='both')
plt.plot(x, y, markeredgecolor="red", markerfacecolor="black")
# Sauvegarde de la représentation
plt.savefig('3n+1.png')
