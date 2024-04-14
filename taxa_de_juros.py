import math 
from numpy import sign
def biss(f, x1, x2, switch =1, tol=1.0e-9):
    f1 = f(x1)
    if f1 == 0.0:
        return x1
    f2 = f(x2)
    if f2 == 00.0:
        return x2
    if sign(f1) == sign(f2):
        print("Raiz não existe nesse intervalo")
    n = int(math.ceil(math.log(abs(x2 - x1) / tol) / math.log(2.0)))
    for i in range(n):
        x3 = 0.5 * (x1 + x2)
        f3 = f(x3)
    if (switch == 1) and (abs(f3) > abs(f1)) and (abs(f3) > abs(f2)):
        return None
    if f3 == 0.0:
        return x3
    if sign(f2)!= sign(f3): x1 = x3; f1 = f3
    else:
        x2 = x3; f2 = f3
        return (x1 + x2)/2.0
def f(x):
    return (1250 / x) * (1- (1 + x) ** (-10)) - 1000
x = biss(f, 0.01, 0.05, tol=1.0e-4)
print('x =', '{:6.4f}'.format(x))