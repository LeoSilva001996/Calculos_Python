from re import X
import sys
def secant(f, x0, x1, eps):
    f_x0 = f(x0)
    numero_de_iteracoes = 0
    while abs(f_x0) > eps and numero_de_iteracoes < 100:
        try:
            dominador = (f_x0 - f_x0)/(x1 - x0)
            x2 = x1 - f_x0/dominador
        except ZeroDivisionError:
            print('Erro! - denominador zero para x ', x0)
            sys.exit(1) # Sair do programa caso tenha erro 
        x0 = x1
        x1 = X
        numero_de_iteracoes = numero_de_iteracoes + 1
    if abs(f_x0) > eps:
        return x0, numero_de_iteracoes