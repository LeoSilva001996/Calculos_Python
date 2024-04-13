import math
from numpy import sign

def bisection(f, x1, x2, switch=1, tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0: return x1
    f2 = f(x2)
    if f2 == 0.0: return x2
    if sign(f1) == sign(f2):
        print('Raiz não se encontra no intervalo informado')
        return None
    n = int(math.ceil(math.log(abs(x2 - x1)/tol)/math.log(2.0)))
    for i in range(n):
        x3 = 0.5*(x1 + x2); f3 = f(x3)
        if (switch == 1) and (abs(f3) > abs(f1)) and (abs(f3) > abs(f2)):
            return None
        if f3 == 0.0: return x3
        if sign(f2)!= sign(f3): x1 = x3; f1 = f3
        else: x2 = x3; f2 = f3
    return (x1 + x2)/2.0
        
def f(x): return math.cos(x) + x

x = bisection(f, -5.0, 4.0, tol = 1.0e-4)

if x is not None:
    print("x = {}".format(x))
else:
    print("A raiz não foi encontrada no intervalo fornecido.")