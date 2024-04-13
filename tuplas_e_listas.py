from numpy import rec

dados = ('Gomes', 'Roberto', (31,10,73))
sobrenome, nome, data_de_nascimento = dados
print(nome)

Ano_de_nascimento = data_de_nascimento [2]
print(Ano_de_nascimento)

nome_completo = dados [1] + ' ' + dados [0]
print(nome_completo)

rec_array = rec.array([(1, 2, 3), (4, 5, 6)], dtype=[('a', int), ('b', int), ('c', int)])
print(rec_array)
