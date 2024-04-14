import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.sqrt(x) + np.sqrt(x - 1) - 3

def df(x):
    return 1/2 * ((1 / np.sqrt(x)) + (1 / np.sqrt(x - 1)))

x = np.linspace(1, 10, 1001)
y = f(x)
plt.plot(x, y)

def newton(chute, interacoes=10):
    raiz = chute
    for i in range(interacoes):
        raiz = raiz - f(raiz) / df(raiz)
    return raiz

print('x =', newton(6, 5))
