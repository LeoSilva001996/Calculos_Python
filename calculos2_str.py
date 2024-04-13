# Constante e igual a 0,5, o valor exatp é 15000;

# soma 2
n = 30000
lista1 = [0.5] * n
print('sum(lista1) = '',sum(lista1)')  # Observe que temos uma erro, a falta de str na função print. 

# soma 2 
n = 30000
lista1 = [0.5] * n                      # Vejamos que o erro foi corrigido por str junto com parêntes.

print('sum(lista1) = ' + str(sum(lista1))) # Observe o terminal obtemos um resultados diferentes entre os print. 

