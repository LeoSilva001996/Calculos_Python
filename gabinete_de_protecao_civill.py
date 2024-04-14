import numpy as np

def f(x):
    return -7 * (2 - 0.9 ** x) - 10

def df(x):
    return -7 * (0.9 ** x) * np.log(0.9)

def newtonRaphson(x, tol=1.0e-3):
    for i in range(30):
        dx = -f(x) / df(x)
        x = x + dx
        if abs(dx) < tol:
            return x, i
    return None, None

print("Muitas interações\n")

x, numIter = newtonRaphson(5.0)

if x is not None:
    print("x =", "{:6.4f}".format(x))
    print("Numero de interações =", numIter)
else:
    print("Muitas interações\n")