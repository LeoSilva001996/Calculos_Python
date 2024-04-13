import numpy as np
import matplotlib.pyplot as plt

def f(x):
  return 2*x**3 - 11.7 * x ** 2 + 17.7 * x - 5

x_anterior = 0
x_depois = 4

lista_x = np.linspace(x_anterior, x_depois, 1001)
lista_y = f(lista_x)
#plt.style.use("seaborn-poster")
plt.style.use("dark_background")
#plt.style.use("grayscale")
plt.plot(lista_x, lista_y)
plt.grid(True)