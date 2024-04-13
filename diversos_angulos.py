def sinal_numerico(a):
    if a < 0.0:         # Se a menor que zero
        sinal = 'negativo'
    elif a > 0.0:       #Se a maior que zero
        sinal = 'positivo'
    else:               # Senão, ou seja, se a não é maior,nem menor que zero (a igual a zero)
        sinal = 'zero'
    return sinal
    a = 1.5
print('a é ' + sinal_numerico(1.5))