from algoritmo import secant

def f(x):
    return x**2 - 9

x0 = 1000
x1 = x0 - 1
solucao, no_iteracao = secant(f, x0, x1, eps=1.0e-6)
if no_iteracao >  0: # Solução achada
        print('Numero de funções calculadas {:d}'.format(2 + no_iteracao))
        print('A solução é: {:f}'.format(solucao))
else:
        print('Solução não achada!')
#Número de funções calculadas: 19
