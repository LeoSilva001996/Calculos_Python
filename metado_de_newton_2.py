def df(x):
    return (6*x**2 - 23.4 * x + 17.7)

def newton(chute, iteracoes):
    raiz = chute
    for i in range(iteracoes):
        raiz = raiz - f(raiz) / df(raiz)
    return raiz

print(newton(3, 3))