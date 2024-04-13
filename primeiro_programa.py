a = 2                            # variável a recebe o valor (int)
b = 1.99                         # variável b recebe o valor 1.99 (float)
c = '2'                          # variável c recebe o valor 2 em forma de um string
print(a > b)

print(a == c)                    # note que c recebeu um sring ('2') e a um int (2),

print((a > b) and (a != c))      # os dois precisam ser verdadeiros para retornar true

print((a > b) or (a == b))       # apenas um precisa ser verdadeiro para retornar true